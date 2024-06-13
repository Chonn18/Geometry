# import os
# import subprocess

# problem = 'a b c = triangle; h = on_tline b a c, on_tline c a b ? perp a h b c'

# # Thiết lập đường dẫn cần thiết
# # project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
# project_root = os.path.abspath(os.path.join(os.getcwd(), '../'))
# alphageometry_dir = os.path.join(project_root, 'alphageometry')
# data_dir = os.path.join('/home/duongvanchon/Documents/project/ag_ckpt_vocab')
# meliad_dir = os.path.join(alphageometry_dir, 'meliad_lib/meliad')

# # Thiết lập các biến môi trường
# env = os.environ.copy()
# # env['PYTHONPATH'] = f"{alphageometry_dir}:{meliad_dir}:{env.get('PYTHONPATH', '')}"
# env['PYTHONPATH'] = f"{alphageometry_dir}:{meliad_dir}"
# env['DEFS_FILE'] = os.path.join(alphageometry_dir, 'defs.txt')
# env['RULES_FILE'] = os.path.join(alphageometry_dir, 'rules.txt')
# env['PROBLEMS_FILE'] = os.path.join(alphageometry_dir, 'examples.txt')
# env['CKPT_PATH'] = os.path.join(data_dir)
# env['VOCAB_PATH'] = os.path.join(data_dir, 'geometry.757.model')
# env['OUT_FILE'] = os.path.join(alphageometry_dir, 'output.txt')

# # Thiết lập các đối số cho alphageometry
# ddar_args = [
#     '--defs_file', env['DEFS_FILE'],
#     '--rules_file', env['RULES_FILE'],
# ]
# search_args = [
#     '--beam_size', '2',
#     '--search_depth', '2',
# ]
# lm_args = [
#     '--ckpt_path', env['CKPT_PATH'],
#     '--vocab_path', env['VOCAB_PATH'],
#     '--gin_search_paths', os.path.join(meliad_dir, 'transformer/configs/'),
#     '--gin_file', 'base_htrans.gin',
#     '--gin_file', 'size/medium_150M.gin',
#     '--gin_file', 'options/positions_t5.gin',
#     '--gin_file', 'options/lr_cosine_decay.gin',
#     '--gin_file', 'options/seq_1024_nocache.gin',
#     '--gin_file', 'geometry_150M_generate.gin',
#     '--gin_param', 'DecoderOnlyLanguageModelGenerate.output_token_losses=True',
#     '--gin_param', 'TransformerTaskConfig.batch_size=2',
#     '--gin_param', 'TransformerTaskConfig.sequence_length=128',
#     '--gin_param', 'Trainer.restore_state_variables=False'
# ]

# # Chạy lệnh alphageometry bằng subprocess

#     # '--problems_file', env['PROBLEMS_FILE'],
#     # '--problem_name', 'orthocenter',
# cmd = [
#     'python', '-m', 'alphageometry',
#     '--alsologtostderr',
#     '--problem' , problem,
#     '--mode', 'alphageometry',
#     '--out_file', env['OUT_FILE'],
# ] + ddar_args + search_args + lm_args

# try:
#     subprocess.run(cmd, env=env, check=True)
# except subprocess.CalledProcessError as e:
#     print(f"Error occurred: {e}")

import os
import subprocess

output_file = '/home/duongvanchon/Documents/project/Geometry/backend/api/output/output_image.png'
def run_alphageometry(problem: str, output_file: str) -> None:
    # Thiết lập đường dẫn cần thiết
    project_root = os.path.abspath(os.path.join(os.getcwd(), '../'))
    alphageometry_dir = os.path.join(project_root, 'alphageometry')
    data_dir = os.path.join('/home/duongvanchon/Documents/project/ag_ckpt_vocab')
    meliad_dir = os.path.join(alphageometry_dir, 'meliad_lib/meliad')

    # Thiết lập các biến môi trường
    env = os.environ.copy()
    env['PYTHONPATH'] = f"{alphageometry_dir}:{meliad_dir}"
    env['DEFS_FILE'] = os.path.join(alphageometry_dir, 'defs.txt')
    env['RULES_FILE'] = os.path.join(alphageometry_dir, 'rules.txt')
    env['PROBLEMS_FILE'] = os.path.join(alphageometry_dir, 'examples.txt')
    env['CKPT_PATH'] = os.path.join(data_dir)
    env['VOCAB_PATH'] = os.path.join(data_dir, 'geometry.757.model')
    env['OUT_FILE'] = output_file

    # Thiết lập các đối số cho alphageometry
    ddar_args = [
        '--defs_file', env['DEFS_FILE'],
        '--rules_file', env['RULES_FILE'],
    ]
    search_args = [
        '--beam_size', '2',
        '--search_depth', '2',
    ]
    lm_args = [
        '--ckpt_path', env['CKPT_PATH'],
        '--vocab_path', env['VOCAB_PATH'],
        '--gin_search_paths', os.path.join(meliad_dir, 'transformer/configs/'),
        '--gin_file', 'base_htrans.gin',
        '--gin_file', 'size/medium_150M.gin',
        '--gin_file', 'options/positions_t5.gin',
        '--gin_file', 'options/lr_cosine_decay.gin',
        '--gin_file', 'options/seq_1024_nocache.gin',
        '--gin_file', 'geometry_150M_generate.gin',
        '--gin_param', 'DecoderOnlyLanguageModelGenerate.output_token_losses=True',
        '--gin_param', 'TransformerTaskConfig.batch_size=2',
        '--gin_param', 'TransformerTaskConfig.sequence_length=128',
        '--gin_param', 'Trainer.restore_state_variables=False'
    ]

    # Chạy lệnh alphageometry bằng subprocess
    cmd = [
        'python', '-m', 'alphageometry',
        '--alsologtostderr',
        '--problem' , problem,
        '--mode', 'alphageometry',
        '--out_file', env['OUT_FILE'],
    ] + ddar_args + search_args + lm_args

    try:
        subprocess.run(cmd, env=env, check=True)
        # return output_file
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        # return e

# Sử dụng hàm
# problem = 'a b c = triangle; h = on_tline b a c, on_tline c a b ? perp a h b c'
# output_file = os.path.join(alphageometry_dir, 'output.txt')
# run_alphageometry(problem, output_file)
