import multiprocessing
import sys
sys.path.append('..')
import random
import ddar
import graph as gh
import problem as pr
from clause_generation import CompoundClauseGen
import signal
from generate_random_proofs import TimeoutException
from utils.loading_utils import load_definitions_and_rules
from prettier_print.pretty_problem_statement import get_nl_problem_statement
from pretty import pretty_nl
from prettier_print.prettier_proof_statements import translate_step
from utils.get_rand_gen_states import get_random_states
from verb.verbalize import IndependentStatementVerbalization

import csv


def main(run_id, interactive):
    dataset_length = 2000
    # filename = f'../../datasets/nl_fl_dataset_{run_id}.csv'
    filename = f'/is/cluster/fast/pghosh/datasets/alpha_geo/nl_fl_dataset_{run_id}.csv'
    # filename = '../data/nl_fl_dataset_2.csv'
    random.seed(run_id)
    defs_path = '../defs.txt'
    rules_path = '../rules.txt'

    # Load definitions and rules
    definitions, rules = load_definitions_and_rules(defs_path, rules_path)

    # field_names = ['sl_n', 'num_clauses', 'nl_statement', 'fl_statement', 'goal_nl', 'goal_fl', 'rnd_states']
    field_names = ['sl_n', 'num_clauses', 'nl_statement', 'fl_statement', 'goal_nl', 'goal_fl']

    # Write data to the CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        # writer = csv.DictWriter(csvfile, fieldnames=field_names,)# delimiter='#')
        # this is necessary for the inspect to work
        writer = csv.DictWriter(csvfile, fieldnames=field_names, quoting=csv.QUOTE_MINIMAL, quotechar='"')
        writer.writeheader()
        serial_num = run_id * dataset_length
        cc_gen = CompoundClauseGen(definitions, 2, 3, 2)
        verbalizer = IndependentStatementVerbalization(None)

        for i in range(dataset_length):
            num_clauses = random.randint(3, 10)
            fl_statement = cc_gen.generate_clauses()

            if interactive: print(fl_statement)

            try:
                p = pr.Problem.from_txt(fl_statement)
            except KeyError as e:
                print(e)
                continue

            if interactive: print(f'Problem created, Building graph ...')
            try:
                # Set an alarm for 10 seconds
                signal.alarm(10)

                # Code block to execute with timeout
                g, _ = gh.Graph.build_problem(p, definitions)

                # Disable the alarm
                signal.alarm(0)
            except TimeoutException as e:
                print("Graph couldn't be create in reasonable time. Perhaps problem with the premises. Continuing ...")
                continue
            except KeyError:
                print("Key error while building graph. Continuing ...")
                continue
            except ValueError:
                print("Value error while building graph. Continuing ...")
                continue
            except AttributeError as e:
                print(e)
                # TODO(Partha, Max, Felix): This is a hack to avoid the AttributeError. We should fix this.
                continue

            if interactive: print(f'Solving ...')

            ddar.solve(g, rules, p, max_level=1)

            # Randomly select a cache node to be the goal. #TODO: Is this right can we do better? Consider coverage!
            possible_goals = list(g.cache.keys())
            if len(possible_goals) > 0:
                goal_fl = list(random.choice(possible_goals))  # comment this line
                # goal_fl = random.choice(possible_goals + [''])  # uncomment this line to get goal less problems
                if goal_fl == '':
                    goal_nl = ''
                else:
                    capitalized_pt_names = [point_name.capitalize() for point_name in goal_fl[1:]]
                    goal_fl[1:] = capitalized_pt_names
                    pretty_goal = pretty_nl(goal_fl[0], goal_fl[1:])
                    if pretty_goal is None:
                        raise ValueError(f'Could not pretty print goal: {goal_fl}')
                    goal_nl = translate_step(pretty_goal)
                    goal_fl = ' '.join(goal_fl)
                # Now we know that the generated premises are not contradictory
                # nl_prob = get_nl_problem_statement(fl_statement)
                nl_prob = verbalizer.problem_fl_2_nl(fl_statement)
                # dump this row
                row = {
                    'sl_n': serial_num,
                    'num_clauses': num_clauses,
                    'nl_statement': nl_prob,
                    'fl_statement': fl_statement,
                    'goal_nl': goal_nl,
                    'goal_fl': goal_fl
                }
                writer.writerow(row)
                serial_num += 1


def str_to_bool(value):
    if value.lower() in ['true', 't', 'yes', '1']:
        return True
    elif value.lower() in ['false', 'f', 'no', '0', 'flase']:  # Including common typo
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Create problem fl - nl dataset')
    parser.add_argument('--run_id', required=True, type=int, help='An integer positional argument')
    parser.add_argument('--interactive', required=True, type=str_to_bool, help='A boolean value (true/false)')
    args = parser.parse_args()

    n_processes = 16

    with multiprocessing.Pool(n_processes) as pool:
        pool.starmap(main, [(args.run_id * n_processes + i, args.interactive) for i in range(n_processes)])
