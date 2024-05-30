#<premise> <conclusion> <proofs>

GEN_PATH =/random_generation 
export PYTHONPATH=$PYTHONPATH:$GEN_PATH

echo $PYTHONPATH

python generate_random_proofs.py

