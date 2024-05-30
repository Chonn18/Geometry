import sys
sys.path.append('..')
from utils.loading_utils import load_definitions_and_rules
# sys.path.append('..')
import random
import ddar
from alphageometry import write_solution
import graph as gh
import problem as pr
from clause_generation import CompoundClauseGen
import signal

class TimeoutException(Exception):
    """Custom exception to indicate a timeout."""
    pass


def signal_handler(signum, frame):
    """Signal handler that raises a TimeoutException."""
    raise TimeoutException("Operation timed out due to signal 14 (SIGALRM)")


# Register the signal handler for SIGALRM
signal.signal(signal.SIGALRM, signal_handler)


def generate_data_from_problem(problem_txt):
    
    defs_path = '../defs.txt'
    rules_path = '../rules.txt'

    # Load definitions and rules
    definitions, rules = load_definitions_and_rules(defs_path, rules_path)
    definitions, rules = load_definitions_and_rules(defs_path, rules_path)
    # cc_gen = CompoundClauseGen(definitions, 2, 3, 2)
    # problem_txt = cc_gen.generate_clauses()
    
    # Tạo bài toán từ đoạn mã txt
    p = pr.Problem.from_txt(problem_txt)

    # Xây dựng đồ thị hình học từ bài toán
    g, _ = gh.Graph.build_problem(p, definitions)

    # Giải quyết bài toán
    ddar.solve(g, rules, p, max_level=1000)

    # Trích xuất các điều kiện, kết luận và bước chứng minh
    premises = []  # Danh sách các điều kiện
    conclusions = []  # Danh sách các kết luận
    proofs = []  # Danh sách các bước chứng minh

    # Lặp qua các node trong đồ thị để trích xuất thông tin
    for node in g.cache:
        # Xác định các điều kiện và kết luận từ node
        if isinstance(node, pr.Problem):
            premises.append(node.premises)
            conclusions.append(node.conclusion)
            proofs.append(node.proofs)

    # Định dạng dữ liệu thành "<premise> <conclusion> <proofs>"
    data = []
    for premise, conclusion, proof in zip(premises, conclusions, proofs):
        data.append(f"{premise} {conclusion} {proof}")

    return data

# Sử dụng hàm generate_data_from_problem để sinh dữ liệu từ một đoạn mã bài toán
problem_txt = "a b = segment a b; g1 = on_tline g1 a a b; g2 = on_tline g2 b b a; m = on_circle m g1 a, " \
              "on_circle m g2 b; n = on_circle n g1 a, on_circle n g2 b; c = on_pline c m a b, on_circle c g1 a; " \
              "d = on_pline d m a b, on_circle d g2 b; e = on_line e a c, on_line e b d; " \
              "p = on_line p a n, on_line p c d; " \
              "q = on_line q b n, on_line q c d"
generated_data = generate_data_from_problem(problem_txt)

# In ra các dữ liệu đã sinh
for data_item in generated_data:
    print(data_item)
