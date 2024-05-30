from .imports import *

from .common import ArgumentGenerator
from .rules import Point, Line, Angle
from .rules import Conjunction
from .rules import Rule

from .common import repo_root
import yaml

from .definitions import Definition, load_patterns




def test_arg_sampling():

	random.seed(11)

	ctx = Controller(ArgumentGenerator(5))

	assert ctx['arguments'] == ('I', 'W', 'P', 'Y', 'Q')

	assert ctx['arg0'] == 'I'
	assert ctx['arg4'] == 'Q'

	assert ctx['selection'] == ('I', 'P', 'Q', 'W', 'Y') # (unshuffled)
	assert ctx['selection_id'] == 59294

	assert ctx['order'] == (0, 3, 1, 4, 2)
	assert ctx['order_id'] == 13



def test_rules():

	num_args = 5

	# treat like a dict which lazily evaluates values that haven't been cached
	ctx = Controller(ArgumentGenerator(num_args, shuffle=False))
	ctx['selection_id'] = 0 # manually set the selection to A, B, C, D, E instead of sampling

	# populate the context with points (should be done by default)
	ctx.extend([Point(f'p{i}', [i]) for i in range(num_args)])

	# optionally include any relevant lines or angles
	ctx.include(Line('line1', [0, 2]), Line('line2', [1, 3]))
	ctx.include(Angle('angle1', [0, 1, 2]), Angle('angle2', [1, 2, 3]))


	assert ctx['line1'] == 'line AC' # 'line1' is evaluated using the corresponding Line object
	assert ctx['line2'] == 'line BD'

	assert ctx['angle1'] == '∠ABC'
	assert ctx['angle2'] == '∠BCD'

	assert ctx['p3'] == 'D'
	assert ctx['p4'] == 'E'




def test_conjunction():

	random.seed(19)

	ctx = Controller(ArgumentGenerator(5), Conjunction('conj', ['arg1', 'arg2', 'arg0']))

	ctx['arg1']

	print()

	cases = []
	for case in ctx.consider():
		print(case['conj'])
		cases.append(case)

	print(len(cases))



def test_abstracting_rules():

	num_args = 5

	# treat like a dict which lazily evaluates values that haven't been cached
	ctx = Controller(ArgumentGenerator(num_args, shuffle=False))
	ctx['selection_id'] = 0 # manually set the selection to A, B, C, D, E instead of sampling

	# populate the context with points (should be done by default)
	ctx.extend([Point(f'p{i}', [i]) for i in range(num_args)])

	# optionally include any relevant lines or angles
	ctx.include(Line('line1', [0, 2]), Line('line2', [1, 3]))
	ctx.include(Angle('angle1', [0, 1, 2]), Angle('angle2', [1, 2, 3]))

	ctx.include(Conjunction('conj', ['line1', 'angle2', 'arg0']))
	ctx['conj_term'] = ' and '

	assert Rule.set_abstraction() # toggles

	assert ctx['line1'] == 'line {p0}{p2}'
	assert ctx['conj'] == '{line1}, {angle2}, and {arg0}'

	del ctx['conj'], ctx['line1'], ctx['angle2'], ctx['arg0']

	Conjunction.set_abstraction(False)

	assert ctx['conj'] == 'line {p0}{p2}, ∠{p1}{p2}{p3}, and A'


def test_definition():

	path = repo_root() / 'assets' / 'def-patterns.yml'
	raw = yaml.safe_load(path.read_text())

	print()

	key, data = raw.popitem()

	my_def = Definition.from_data(key, data)

	args = 'X A B C D'
	manual_args = {f'arg{i}': a for i, a in enumerate(args.split())}

	ctx = Controller(my_def)
	ctx.include(DictGadget(manual_args))
	ctx.include(DictGadget({'selection_id': 0, 'order_id': 0})) # use A, B, C ...
	print(ctx['formal'])


	random.seed(11)
	for _ in range(10):
		print(ctx['clause'])
		ctx.clear_cache()

	print()
	Rule.set_abstraction()

	random.seed(11)
	for _ in range(10):
		print(ctx['clause'])
		ctx.clear_cache()


def test_generate_all():
	path = repo_root() / 'assets' / 'def-patterns.yml'
	raw = yaml.safe_load(path.read_text())

	print()

	# key, data = raw.popitem()
	key = 'circle'
	data = raw[key]
	my_def = Definition.from_data(key, data)

	args = 'X A B C D'
	manual_args = {f'arg{i}': a for i, a in enumerate(args.split())}

	ctx = Controller(my_def)
	# ctx.include(DictGadget(manual_args))
	ctx.include(DictGadget({
		# 'selection_id': 0, # fixes the selection of letters that gets used
		# 'order_id': 0, # fixes the order of letters that gets used
		# 'arg0': 'A',
	}))  # use A, B, C ...
	# print(ctx['formal'])

	# Conjunction.set_abstraction()
	# Rule.set_abstraction()

	clauses = []

	cap = 100
	for i, case in enumerate(ctx.consider()):
		if i == cap:
			clauses = None
			break
		clauses.append([case['clause'], case['formal']])

	if clauses is None:
		clauses = []
		for _ in range(cap):
			ctx.clear_cache()
			# clauses.append(ctx['clause'])
			clauses.append([ctx['clause'], ctx['formal']])

	print(f'Generated {i} cases{"" if i < cap else " (but there are more possible)"}')

	from tabulate import tabulate
	print(tabulate(clauses))
	# print('\n'.join(map(lambda s:,clauses)))


import re
from .definitions import ClauseGenerator

def test_all_clauses():
	base_path = repo_root() / 'defs.txt'

	unique_function_names = list(re.findall(r'\n\n\s*(\w+)', base_path.read_text(), re.MULTILINE))

	path = repo_root() / 'assets' / 'def-patterns.yml'
	defs = load_patterns(path)

	print()

	for d in unique_function_names:

	# d = 'eq_quadrangle'

		ctx = Controller(ClauseGenerator(d))
		out = ctx['statement']
		print(out)













