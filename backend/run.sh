#!/bin/bash

DATA=/home/duongvanchon/Documents/project/ag_ckpt_vocab
MELIAD_PATH=/home/duongvanchon/Documents/project/Geometry/alphageometry/meliad_lib/meliad
ALPHA_PATH=/home/duongvanchon/Documents/project/Geometry/alphageometry
OUT_PUT=/home/duongvanchon/Documents/project/Geometry/backend/api/output

# Ensure paths are absolute and correctly referenced
export PYTHONPATH=$ALPHA_PATH:$MELIAD_PATH:$PYTHONPATH

DDAR_ARGS=(
  --defs_file=$ALPHA_PATH/defs.txt
  --rules_file=$ALPHA_PATH/rules.txt
)

BATCH_SIZE=2
BEAM_SIZE=2
DEPTH=2

SEARCH_ARGS=(
  --beam_size=$BEAM_SIZE
  --search_depth=$DEPTH
)

LM_ARGS=(
  --ckpt_path=$DATA
  --vocab_path=$DATA/geometry.757.model
  --gin_search_paths=$MELIAD_PATH/transformer/configs
  --gin_file=base_htrans.gin
  --gin_file=size/medium_150M.gin
  --gin_file=options/positions_t5.gin
  --gin_file=options/lr_cosine_decay.gin
  --gin_file=options/seq_1024_nocache.gin
  --gin_file=geometry_150M_generate.gin
  --gin_param=DecoderOnlyLanguageModelGenerate.output_token_losses=True
  --gin_param=TransformerTaskConfig.batch_size=$BATCH_SIZE
  --gin_param=TransformerTaskConfig.sequence_length=128
  --gin_param=Trainer.restore_state_variables=False
)

echo "PYTHONPATH: $PYTHONPATH"


#   --problems_file=$ALPHA_PATH/examples.txt \
#   --problem_name=orthocenter \

python -m alphageometry \
  --alsologtostderr \
  --problem = "a b c = triangle; h = on_tline b a c, on_tline c a b ? perp a h b c"\
  --mode=alphageometry \
  --out_file=$OUT_PUT/output.txt \
  "${DDAR_ARGS[@]}" \
  "${SEARCH_ARGS[@]}" \
  "${LM_ARGS[@]}"
