# Generated via
# trl sft > filename.txt
# trl sft | pbcopy

usage: sft.py [-h] [--dataset_name DATASET_NAME]
              [--dataset_text_field DATASET_TEXT_FIELD]
              [--dataset_train_name DATASET_TRAIN_NAME]
              [--dataset_test_name DATASET_TEST_NAME]
              [--max_seq_length MAX_SEQ_LENGTH] [--packing [PACKING]]
              [--config CONFIG]
              [--gradient_checkpointing_use_reentrant [GRADIENT_CHECKPOINTING_USE_REENTRANT]]
              --output_dir OUTPUT_DIR
              [--overwrite_output_dir [OVERWRITE_OUTPUT_DIR]]
              [--do_train [DO_TRAIN]] [--do_eval [DO_EVAL]]
              [--do_predict [DO_PREDICT]]
              [--evaluation_strategy {no,steps,epoch}]
              [--prediction_loss_only [PREDICTION_LOSS_ONLY]]
              [--per_device_train_batch_size PER_DEVICE_TRAIN_BATCH_SIZE]
              [--per_device_eval_batch_size PER_DEVICE_EVAL_BATCH_SIZE]
              [--per_gpu_train_batch_size PER_GPU_TRAIN_BATCH_SIZE]
              [--per_gpu_eval_batch_size PER_GPU_EVAL_BATCH_SIZE]
              [--gradient_accumulation_steps GRADIENT_ACCUMULATION_STEPS]
              [--eval_accumulation_steps EVAL_ACCUMULATION_STEPS]
              [--eval_delay EVAL_DELAY] [--learning_rate LEARNING_RATE]
              [--weight_decay WEIGHT_DECAY] [--adam_beta1 ADAM_BETA1]
              [--adam_beta2 ADAM_BETA2] [--adam_epsilon ADAM_EPSILON]
              [--max_grad_norm MAX_GRAD_NORM]
              [--num_train_epochs NUM_TRAIN_EPOCHS] [--max_steps MAX_STEPS]
              [--lr_scheduler_type {linear,cosine,cosine_with_restarts,polynomial,constant,constant_with_warmup,inverse_sqrt,reduce_lr_on_plateau,cosine_with_min_lr}]
              [--lr_scheduler_kwargs LR_SCHEDULER_KWARGS]
              [--warmup_ratio WARMUP_RATIO] [--warmup_steps WARMUP_STEPS]
              [--log_level {detail,debug,info,warning,error,critical,passive}]
              [--log_level_replica {detail,debug,info,warning,error,critical,passive}]
              [--log_on_each_node [LOG_ON_EACH_NODE]] [--no_log_on_each_node]
              [--logging_dir LOGGING_DIR]
              [--logging_strategy {no,steps,epoch}]
              [--logging_first_step [LOGGING_FIRST_STEP]]
              [--logging_steps LOGGING_STEPS]
              [--logging_nan_inf_filter [LOGGING_NAN_INF_FILTER]]
              [--no_logging_nan_inf_filter] [--save_strategy {no,steps,epoch}]
              [--save_steps SAVE_STEPS] [--save_total_limit SAVE_TOTAL_LIMIT]
              [--save_safetensors [SAVE_SAFETENSORS]] [--no_save_safetensors]
              [--save_on_each_node [SAVE_ON_EACH_NODE]]
              [--save_only_model [SAVE_ONLY_MODEL]] [--no_cuda [NO_CUDA]]
              [--use_cpu [USE_CPU]] [--use_mps_device [USE_MPS_DEVICE]]
              [--seed SEED] [--data_seed DATA_SEED]
              [--jit_mode_eval [JIT_MODE_EVAL]] [--use_ipex [USE_IPEX]]
              [--bf16 [BF16]] [--fp16 [FP16]]
              [--fp16_opt_level FP16_OPT_LEVEL]
              [--half_precision_backend {auto,apex,cpu_amp}]
              [--bf16_full_eval [BF16_FULL_EVAL]]
              [--fp16_full_eval [FP16_FULL_EVAL]] [--tf32 TF32]
              [--local_rank LOCAL_RANK]
              [--ddp_backend {nccl,gloo,mpi,ccl,hccl,cncl}]
              [--tpu_num_cores TPU_NUM_CORES]
              [--tpu_metrics_debug [TPU_METRICS_DEBUG]]
              [--debug DEBUG [DEBUG ...]]
              [--dataloader_drop_last [DATALOADER_DROP_LAST]]
              [--eval_steps EVAL_STEPS]
              [--dataloader_num_workers DATALOADER_NUM_WORKERS]
              [--dataloader_prefetch_factor DATALOADER_PREFETCH_FACTOR]
              [--past_index PAST_INDEX] [--run_name RUN_NAME]
              [--disable_tqdm DISABLE_TQDM]
              [--remove_unused_columns [REMOVE_UNUSED_COLUMNS]]
              [--no_remove_unused_columns]
              [--label_names LABEL_NAMES [LABEL_NAMES ...]]
              [--load_best_model_at_end [LOAD_BEST_MODEL_AT_END]]
              [--metric_for_best_model METRIC_FOR_BEST_MODEL]
              [--greater_is_better GREATER_IS_BETTER]
              [--ignore_data_skip [IGNORE_DATA_SKIP]] [--fsdp FSDP]
              [--fsdp_min_num_params FSDP_MIN_NUM_PARAMS]
              [--fsdp_config FSDP_CONFIG]
              [--fsdp_transformer_layer_cls_to_wrap FSDP_TRANSFORMER_LAYER_CLS_TO_WRAP]
              [--accelerator_config ACCELERATOR_CONFIG]
              [--deepspeed DEEPSPEED]
              [--label_smoothing_factor LABEL_SMOOTHING_FACTOR]
              [--optim {adamw_hf,adamw_torch,adamw_torch_fused,adamw_torch_xla,adamw_torch_npu_fused,adamw_apex_fused,adafactor,adamw_anyprecision,sgd,adagrad,adamw_bnb_8bit,adamw_8bit,lion_8bit,lion_32bit,paged_adamw_32bit,paged_adamw_8bit,paged_lion_32bit,paged_lion_8bit,rmsprop,rmsprop_bnb,rmsprop_bnb_8bit,rmsprop_bnb_32bit,galore_adamw,galore_adamw_8bit,galore_adafactor,galore_adamw_layerwise,galore_adamw_8bit_layerwise,galore_adafactor_layerwise}]
              [--optim_args OPTIM_ARGS] [--adafactor [ADAFACTOR]]
              [--group_by_length [GROUP_BY_LENGTH]]
              [--length_column_name LENGTH_COLUMN_NAME]
              [--report_to REPORT_TO]
              [--ddp_find_unused_parameters DDP_FIND_UNUSED_PARAMETERS]
              [--ddp_bucket_cap_mb DDP_BUCKET_CAP_MB]
              [--ddp_broadcast_buffers DDP_BROADCAST_BUFFERS]
              [--dataloader_pin_memory [DATALOADER_PIN_MEMORY]]
              [--no_dataloader_pin_memory]
              [--dataloader_persistent_workers [DATALOADER_PERSISTENT_WORKERS]]
              [--skip_memory_metrics [SKIP_MEMORY_METRICS]]
              [--no_skip_memory_metrics]
              [--use_legacy_prediction_loop [USE_LEGACY_PREDICTION_LOOP]]
              [--push_to_hub [PUSH_TO_HUB]]
              [--resume_from_checkpoint RESUME_FROM_CHECKPOINT]
              [--hub_model_id HUB_MODEL_ID]
              [--hub_strategy {end,every_save,checkpoint,all_checkpoints}]
              [--hub_token HUB_TOKEN] [--hub_private_repo [HUB_PRIVATE_REPO]]
              [--hub_always_push [HUB_ALWAYS_PUSH]]
              [--gradient_checkpointing [GRADIENT_CHECKPOINTING]]
              [--gradient_checkpointing_kwargs GRADIENT_CHECKPOINTING_KWARGS]
              [--include_inputs_for_metrics [INCLUDE_INPUTS_FOR_METRICS]]
              [--eval_do_concat_batches [EVAL_DO_CONCAT_BATCHES]]
              [--no_eval_do_concat_batches]
              [--fp16_backend {auto,apex,cpu_amp}]
              [--push_to_hub_model_id PUSH_TO_HUB_MODEL_ID]
              [--push_to_hub_organization PUSH_TO_HUB_ORGANIZATION]
              [--push_to_hub_token PUSH_TO_HUB_TOKEN]
              [--mp_parameters MP_PARAMETERS]
              [--auto_find_batch_size [AUTO_FIND_BATCH_SIZE]]
              [--full_determinism [FULL_DETERMINISM]]
              [--torchdynamo TORCHDYNAMO] [--ray_scope RAY_SCOPE]
              [--ddp_timeout DDP_TIMEOUT] [--torch_compile [TORCH_COMPILE]]
              [--torch_compile_backend TORCH_COMPILE_BACKEND]
              [--torch_compile_mode TORCH_COMPILE_MODE]
              [--dispatch_batches DISPATCH_BATCHES]
              [--split_batches SPLIT_BATCHES]
              [--include_tokens_per_second [INCLUDE_TOKENS_PER_SECOND]]
              [--include_num_input_tokens_seen [INCLUDE_NUM_INPUT_TOKENS_SEEN]]
              [--neftune_noise_alpha NEFTUNE_NOISE_ALPHA]
              [--optim_target_modules OPTIM_TARGET_MODULES]
              [--model_name_or_path MODEL_NAME_OR_PATH]
              [--model_revision MODEL_REVISION]
              [--torch_dtype {auto,bfloat16,float16,float32}]
              [--trust_remote_code [TRUST_REMOTE_CODE]]
              [--attn_implementation ATTN_IMPLEMENTATION]
              [--use_peft [USE_PEFT]] [--lora_r LORA_R]
              [--lora_alpha LORA_ALPHA] [--lora_dropout LORA_DROPOUT]
              [--lora_target_modules LORA_TARGET_MODULES [LORA_TARGET_MODULES ...]]
              [--lora_modules_to_save LORA_MODULES_TO_SAVE [LORA_MODULES_TO_SAVE ...]]
              [--lora_task_type LORA_TASK_TYPE]
              [--load_in_8bit [LOAD_IN_8BIT]] [--load_in_4bit [LOAD_IN_4BIT]]
              [--bnb_4bit_quant_type BNB_4BIT_QUANT_TYPE]
              [--use_bnb_nested_quant [USE_BNB_NESTED_QUANT]]

options:
  -h, --help            show this help message and exit
  --dataset_name DATASET_NAME
                        the dataset name (default: timdettmers/openassistant-
                        guanaco)
  --dataset_text_field DATASET_TEXT_FIELD
                        the text field of the dataset (default: None)
  --dataset_train_name DATASET_TRAIN_NAME
                        the name of the training set of the dataset (default:
                        train)
  --dataset_test_name DATASET_TEST_NAME
                        the name of the training set of the dataset (default:
                        test)
  --max_seq_length MAX_SEQ_LENGTH
                        The maximum sequence length for SFT Trainer (default:
                        512)
  --packing [PACKING]   Whether to apply data packing or not during training
                        (default: False)
  --config CONFIG       Path to the optional config file (default: None)
  --gradient_checkpointing_use_reentrant [GRADIENT_CHECKPOINTING_USE_REENTRANT]
                        Whether to apply `use_reentrant` for
                        gradient_checkpointing (default: False)
  --output_dir OUTPUT_DIR
                        The output directory where the model predictions and
                        checkpoints will be written. (default: None)
  --overwrite_output_dir [OVERWRITE_OUTPUT_DIR]
                        Overwrite the content of the output directory. Use
                        this to continue training if output_dir points to a
                        checkpoint directory. (default: False)
  --do_train [DO_TRAIN]
                        Whether to run training. (default: False)
  --do_eval [DO_EVAL]   Whether to run eval on the dev set. (default: False)
  --do_predict [DO_PREDICT]
                        Whether to run predictions on the test set. (default:
                        False)
  --evaluation_strategy {no,steps,epoch}
                        The evaluation strategy to use. (default: no)
  --prediction_loss_only [PREDICTION_LOSS_ONLY]
                        When performing evaluation and predictions, only
                        returns the loss. (default: False)
  --per_device_train_batch_size PER_DEVICE_TRAIN_BATCH_SIZE
                        Batch size per GPU/TPU/MPS/NPU core/CPU for training.
                        (default: 8)
  --per_device_eval_batch_size PER_DEVICE_EVAL_BATCH_SIZE
                        Batch size per GPU/TPU/MPS/NPU core/CPU for
                        evaluation. (default: 8)
  --per_gpu_train_batch_size PER_GPU_TRAIN_BATCH_SIZE
                        Deprecated, the use of `--per_device_train_batch_size`
                        is preferred. Batch size per GPU/TPU core/CPU for
                        training. (default: None)
  --per_gpu_eval_batch_size PER_GPU_EVAL_BATCH_SIZE
                        Deprecated, the use of `--per_device_eval_batch_size`
                        is preferred. Batch size per GPU/TPU core/CPU for
                        evaluation. (default: None)
  --gradient_accumulation_steps GRADIENT_ACCUMULATION_STEPS
                        Number of updates steps to accumulate before
                        performing a backward/update pass. (default: 1)
  --eval_accumulation_steps EVAL_ACCUMULATION_STEPS
                        Number of predictions steps to accumulate before
                        moving the tensors to the CPU. (default: None)
  --eval_delay EVAL_DELAY
                        Number of epochs or steps to wait for before the first
                        evaluation can be performed, depending on the
                        evaluation_strategy. (default: 0)
  --learning_rate LEARNING_RATE
                        The initial learning rate for AdamW. (default: 5e-05)
  --weight_decay WEIGHT_DECAY
                        Weight decay for AdamW if we apply some. (default:
                        0.0)
  --adam_beta1 ADAM_BETA1
                        Beta1 for AdamW optimizer (default: 0.9)
  --adam_beta2 ADAM_BETA2
                        Beta2 for AdamW optimizer (default: 0.999)
  --adam_epsilon ADAM_EPSILON
                        Epsilon for AdamW optimizer. (default: 1e-08)
  --max_grad_norm MAX_GRAD_NORM
                        Max gradient norm. (default: 1.0)
  --num_train_epochs NUM_TRAIN_EPOCHS
                        Total number of training epochs to perform. (default:
                        3.0)
  --max_steps MAX_STEPS
                        If > 0: set total number of training steps to perform.
                        Override num_train_epochs. (default: -1)
  --lr_scheduler_type {linear,cosine,cosine_with_restarts,polynomial,constant,constant_with_warmup,inverse_sqrt,reduce_lr_on_plateau,cosine_with_min_lr}
                        The scheduler type to use. (default: linear)
  --lr_scheduler_kwargs LR_SCHEDULER_KWARGS
                        Extra parameters for the lr_scheduler such as
                        {'num_cycles': 1} for the cosine with hard restarts.
                        (default: {})
  --warmup_ratio WARMUP_RATIO
                        Linear warmup over warmup_ratio fraction of total
                        steps. (default: 0.0)
  --warmup_steps WARMUP_STEPS
                        Linear warmup over warmup_steps. (default: 0)
  --log_level {detail,debug,info,warning,error,critical,passive}
                        Logger log level to use on the main node. Possible
                        choices are the log levels as strings: 'debug',
                        'info', 'warning', 'error' and 'critical', plus a
                        'passive' level which doesn't set anything and lets
                        the application set the level. Defaults to 'passive'.
                        (default: passive)
  --log_level_replica {detail,debug,info,warning,error,critical,passive}
                        Logger log level to use on replica nodes. Same choices
                        and defaults as ``log_level`` (default: warning)
  --log_on_each_node [LOG_ON_EACH_NODE]
                        When doing a multinode distributed training, whether
                        to log once per node or just once on the main node.
                        (default: True)
  --no_log_on_each_node
                        When doing a multinode distributed training, whether
                        to log once per node or just once on the main node.
                        (default: False)
  --logging_dir LOGGING_DIR
                        Tensorboard log dir. (default: None)
  --logging_strategy {no,steps,epoch}
                        The logging strategy to use. (default: steps)
  --logging_first_step [LOGGING_FIRST_STEP]
                        Log the first global_step (default: False)
  --logging_steps LOGGING_STEPS
                        Log every X updates steps. Should be an integer or a
                        float in range `[0,1)`. If smaller than 1, will be
                        interpreted as ratio of total training steps.
                        (default: 500)
  --logging_nan_inf_filter [LOGGING_NAN_INF_FILTER]
                        Filter nan and inf losses for logging. (default: True)
  --no_logging_nan_inf_filter
                        Filter nan and inf losses for logging. (default:
                        False)
  --save_strategy {no,steps,epoch}
                        The checkpoint save strategy to use. (default: steps)
  --save_steps SAVE_STEPS
                        Save checkpoint every X updates steps. Should be an
                        integer or a float in range `[0,1)`. If smaller than
                        1, will be interpreted as ratio of total training
                        steps. (default: 500)
  --save_total_limit SAVE_TOTAL_LIMIT
                        If a value is passed, will limit the total amount of
                        checkpoints. Deletes the older checkpoints in
                        `output_dir`. When `load_best_model_at_end` is
                        enabled, the 'best' checkpoint according to
                        `metric_for_best_model` will always be retained in
                        addition to the most recent ones. For example, for
                        `save_total_limit=5` and
                        `load_best_model_at_end=True`, the four last
                        checkpoints will always be retained alongside the best
                        model. When `save_total_limit=1` and
                        `load_best_model_at_end=True`, it is possible that two
                        checkpoints are saved: the last one and the best one
                        (if they are different). Default is unlimited
                        checkpoints (default: None)
  --save_safetensors [SAVE_SAFETENSORS]
                        Use safetensors saving and loading for state dicts
                        instead of default torch.load and torch.save.
                        (default: True)
  --no_save_safetensors
                        Use safetensors saving and loading for state dicts
                        instead of default torch.load and torch.save.
                        (default: False)
  --save_on_each_node [SAVE_ON_EACH_NODE]
                        When doing multi-node distributed training, whether to
                        save models and checkpoints on each node, or only on
                        the main one (default: False)
  --save_only_model [SAVE_ONLY_MODEL]
                        When checkpointing, whether to only save the model, or
                        also the optimizer, scheduler & rng state.Note that
                        when this is true, you won't be able to resume
                        training from checkpoint.This enables you to save
                        storage by not storing the optimizer, scheduler & rng
                        state.You can only load the model using
                        from_pretrained with this option set to True.
                        (default: False)
  --no_cuda [NO_CUDA]   This argument is deprecated. It will be removed in
                        version 5.0 of 🤗 Transformers. (default: False)
  --use_cpu [USE_CPU]   Whether or not to use cpu. If set to False, we will
                        use cuda/tpu/mps/npu device if available. (default:
                        False)
  --use_mps_device [USE_MPS_DEVICE]
                        This argument is deprecated. `mps` device will be used
                        if available similar to `cuda` device. It will be
                        removed in version 5.0 of 🤗 Transformers (default:
                        False)
  --seed SEED           Random seed that will be set at the beginning of
                        training. (default: 42)
  --data_seed DATA_SEED
                        Random seed to be used with data samplers. (default:
                        None)
  --jit_mode_eval [JIT_MODE_EVAL]
                        Whether or not to use PyTorch jit trace for inference
                        (default: False)
  --use_ipex [USE_IPEX]
                        Use Intel extension for PyTorch when it is available,
                        installation: 'https://github.com/intel/intel-
                        extension-for-pytorch' (default: False)
  --bf16 [BF16]         Whether to use bf16 (mixed) precision instead of
                        32-bit. Requires Ampere or higher NVIDIA architecture
                        or using CPU (use_cpu) or Ascend NPU. This is an
                        experimental API and it may change. (default: False)
  --fp16 [FP16]         Whether to use fp16 (mixed) precision instead of
                        32-bit (default: False)
  --fp16_opt_level FP16_OPT_LEVEL
                        For fp16: Apex AMP optimization level selected in
                        ['O0', 'O1', 'O2', and 'O3']. See details at
                        https://nvidia.github.io/apex/amp.html (default: O1)
  --half_precision_backend {auto,apex,cpu_amp}
                        The backend to be used for half precision. (default:
                        auto)
  --bf16_full_eval [BF16_FULL_EVAL]
                        Whether to use full bfloat16 evaluation instead of
                        32-bit. This is an experimental API and it may change.
                        (default: False)
  --fp16_full_eval [FP16_FULL_EVAL]
                        Whether to use full float16 evaluation instead of
                        32-bit (default: False)
  --tf32 TF32           Whether to enable tf32 mode, available in Ampere and
                        newer GPU architectures. This is an experimental API
                        and it may change. (default: None)
  --local_rank LOCAL_RANK
                        For distributed training: local_rank (default: -1)
  --ddp_backend {nccl,gloo,mpi,ccl,hccl,cncl}
                        The backend to be used for distributed training
                        (default: None)
  --tpu_num_cores TPU_NUM_CORES
                        TPU: Number of TPU cores (automatically passed by
                        launcher script) (default: None)
  --tpu_metrics_debug [TPU_METRICS_DEBUG]
                        Deprecated, the use of `--debug tpu_metrics_debug` is
                        preferred. TPU: Whether to print debug metrics
                        (default: False)
  --debug DEBUG [DEBUG ...]
                        Whether or not to enable debug mode. Current options:
                        `underflow_overflow` (Detect underflow and overflow in
                        activations and weights), `tpu_metrics_debug` (print
                        debug metrics on TPU). (default: None)
  --dataloader_drop_last [DATALOADER_DROP_LAST]
                        Drop the last incomplete batch if it is not divisible
                        by the batch size. (default: False)
  --eval_steps EVAL_STEPS
                        Run an evaluation every X steps. Should be an integer
                        or a float in range `[0,1)`. If smaller than 1, will
                        be interpreted as ratio of total training steps.
                        (default: None)
  --dataloader_num_workers DATALOADER_NUM_WORKERS
                        Number of subprocesses to use for data loading
                        (PyTorch only). 0 means that the data will be loaded
                        in the main process. (default: 0)
  --dataloader_prefetch_factor DATALOADER_PREFETCH_FACTOR
                        Number of batches loaded in advance by each worker. 2
                        means there will be a total of 2 * num_workers batches
                        prefetched across all workers. Default is 2 for
                        PyTorch < 2.0.0 and otherwise None. (default: None)
  --past_index PAST_INDEX
                        If >=0, uses the corresponding part of the output as
                        the past state for next step. (default: -1)
  --run_name RUN_NAME   An optional descriptor for the run. Notably used for
                        wandb logging. (default: None)
  --disable_tqdm DISABLE_TQDM
                        Whether or not to disable the tqdm progress bars.
                        (default: None)
  --remove_unused_columns [REMOVE_UNUSED_COLUMNS]
                        Remove columns not required by the model when using an
                        nlp.Dataset. (default: True)
  --no_remove_unused_columns
                        Remove columns not required by the model when using an
                        nlp.Dataset. (default: False)
  --label_names LABEL_NAMES [LABEL_NAMES ...]
                        The list of keys in your dictionary of inputs that
                        correspond to the labels. (default: None)
  --load_best_model_at_end [LOAD_BEST_MODEL_AT_END]
                        Whether or not to load the best model found during
                        training at the end of training. When this option is
                        enabled, the best checkpoint will always be saved. See
                        `save_total_limit` for more. (default: False)
  --metric_for_best_model METRIC_FOR_BEST_MODEL
                        The metric to use to compare two different models.
                        (default: None)
  --greater_is_better GREATER_IS_BETTER
                        Whether the `metric_for_best_model` should be
                        maximized or not. (default: None)
  --ignore_data_skip [IGNORE_DATA_SKIP]
                        When resuming training, whether or not to skip the
                        first epochs and batches to get to the same training
                        data. (default: False)
  --fsdp FSDP           Whether or not to use PyTorch Fully Sharded Data
                        Parallel (FSDP) training (in distributed training
                        only). The base option should be `full_shard`,
                        `shard_grad_op` or `no_shard` and you can add CPU-
                        offload to `full_shard` or `shard_grad_op` like this:
                        full_shard offload` or `shard_grad_op offload`. You
                        can add auto-wrap to `full_shard` or `shard_grad_op`
                        with the same syntax: full_shard auto_wrap` or
                        `shard_grad_op auto_wrap`. (default: )
  --fsdp_min_num_params FSDP_MIN_NUM_PARAMS
                        This parameter is deprecated. FSDP's minimum number of
                        parameters for Default Auto Wrapping. (useful only
                        when `fsdp` field is passed). (default: 0)
  --fsdp_config FSDP_CONFIG
                        Config to be used with FSDP (Pytorch Fully Sharded
                        Data Parallel). The value is either a fsdp json config
                        file (e.g., `fsdp_config.json`) or an already loaded
                        json file as `dict`. (default: None)
  --fsdp_transformer_layer_cls_to_wrap FSDP_TRANSFORMER_LAYER_CLS_TO_WRAP
                        This parameter is deprecated. Transformer layer class
                        name (case-sensitive) to wrap, e.g, `BertLayer`,
                        `GPTJBlock`, `T5Block` .... (useful only when `fsdp`
                        flag is passed). (default: None)
  --accelerator_config ACCELERATOR_CONFIG
                        Config to be used with the internal Accelerator object
                        initializtion. The value is either a accelerator json
                        config file (e.g., `accelerator_config.json`) or an
                        already loaded json file as `dict`. (default: None)
  --deepspeed DEEPSPEED
                        Enable deepspeed and pass the path to deepspeed json
                        config file (e.g. `ds_config.json`) or an already
                        loaded json file as a dict (default: None)
  --label_smoothing_factor LABEL_SMOOTHING_FACTOR
                        The label smoothing epsilon to apply (zero means no
                        label smoothing). (default: 0.0)
  --optim {adamw_hf,adamw_torch,adamw_torch_fused,adamw_torch_xla,adamw_torch_npu_fused,adamw_apex_fused,adafactor,adamw_anyprecision,sgd,adagrad,adamw_bnb_8bit,adamw_8bit,lion_8bit,lion_32bit,paged_adamw_32bit,paged_adamw_8bit,paged_lion_32bit,paged_lion_8bit,rmsprop,rmsprop_bnb,rmsprop_bnb_8bit,rmsprop_bnb_32bit,galore_adamw,galore_adamw_8bit,galore_adafactor,galore_adamw_layerwise,galore_adamw_8bit_layerwise,galore_adafactor_layerwise}
                        The optimizer to use. (default: adamw_torch)
  --optim_args OPTIM_ARGS
                        Optional arguments to supply to optimizer. (default:
                        None)
  --adafactor [ADAFACTOR]
                        Whether or not to replace AdamW by Adafactor.
                        (default: False)
  --group_by_length [GROUP_BY_LENGTH]
                        Whether or not to group samples of roughly the same
                        length together when batching. (default: False)
  --length_column_name LENGTH_COLUMN_NAME
                        Column name with precomputed lengths to use when
                        grouping by length. (default: length)
  --report_to REPORT_TO
                        The list of integrations to report the results and
                        logs to. (default: None)
  --ddp_find_unused_parameters DDP_FIND_UNUSED_PARAMETERS
                        When using distributed training, the value of the flag
                        `find_unused_parameters` passed to
                        `DistributedDataParallel`. (default: None)
  --ddp_bucket_cap_mb DDP_BUCKET_CAP_MB
                        When using distributed training, the value of the flag
                        `bucket_cap_mb` passed to `DistributedDataParallel`.
                        (default: None)
  --ddp_broadcast_buffers DDP_BROADCAST_BUFFERS
                        When using distributed training, the value of the flag
                        `broadcast_buffers` passed to
                        `DistributedDataParallel`. (default: None)
  --dataloader_pin_memory [DATALOADER_PIN_MEMORY]
                        Whether or not to pin memory for DataLoader. (default:
                        True)
  --no_dataloader_pin_memory
                        Whether or not to pin memory for DataLoader. (default:
                        False)
  --dataloader_persistent_workers [DATALOADER_PERSISTENT_WORKERS]
                        If True, the data loader will not shut down the worker
                        processes after a dataset has been consumed once. This
                        allows to maintain the workers Dataset instances
                        alive. Can potentially speed up training, but will
                        increase RAM usage. (default: False)
  --skip_memory_metrics [SKIP_MEMORY_METRICS]
                        Whether or not to skip adding of memory profiler
                        reports to metrics. (default: True)
  --no_skip_memory_metrics
                        Whether or not to skip adding of memory profiler
                        reports to metrics. (default: False)
  --use_legacy_prediction_loop [USE_LEGACY_PREDICTION_LOOP]
                        Whether or not to use the legacy prediction_loop in
                        the Trainer. (default: False)
  --push_to_hub [PUSH_TO_HUB]
                        Whether or not to upload the trained model to the
                        model hub after training. (default: False)
  --resume_from_checkpoint RESUME_FROM_CHECKPOINT
                        The path to a folder with a valid checkpoint for your
                        model. (default: None)
  --hub_model_id HUB_MODEL_ID
                        The name of the repository to keep in sync with the
                        local `output_dir`. (default: None)
  --hub_strategy {end,every_save,checkpoint,all_checkpoints}
                        The hub strategy to use when `--push_to_hub` is
                        activated. (default: every_save)
  --hub_token HUB_TOKEN
                        The token to use to push to the Model Hub. (default:
                        None)
  --hub_private_repo [HUB_PRIVATE_REPO]
                        Whether the model repository is private or not.
                        (default: False)
  --hub_always_push [HUB_ALWAYS_PUSH]
                        Unless `True`, the Trainer will skip pushes if the
                        previous one wasn't finished yet. (default: False)
  --gradient_checkpointing [GRADIENT_CHECKPOINTING]
                        If True, use gradient checkpointing to save memory at
                        the expense of slower backward pass. (default: False)
  --gradient_checkpointing_kwargs GRADIENT_CHECKPOINTING_KWARGS
                        Gradient checkpointing key word arguments such as
                        `use_reentrant`. Will be passed to
                        `torch.utils.checkpoint.checkpoint` through
                        `model.gradient_checkpointing_enable`. (default: None)
  --include_inputs_for_metrics [INCLUDE_INPUTS_FOR_METRICS]
                        Whether or not the inputs will be passed to the
                        `compute_metrics` function. (default: False)
  --eval_do_concat_batches [EVAL_DO_CONCAT_BATCHES]
                        Whether to recursively concat
                        inputs/losses/labels/predictions across batches. If
                        `False`, will instead store them as lists, with each
                        batch kept separate. (default: True)
  --no_eval_do_concat_batches
                        Whether to recursively concat
                        inputs/losses/labels/predictions across batches. If
                        `False`, will instead store them as lists, with each
                        batch kept separate. (default: False)
  --fp16_backend {auto,apex,cpu_amp}
                        Deprecated. Use half_precision_backend instead
                        (default: auto)
  --push_to_hub_model_id PUSH_TO_HUB_MODEL_ID
                        The name of the repository to which push the
                        `Trainer`. (default: None)
  --push_to_hub_organization PUSH_TO_HUB_ORGANIZATION
                        The name of the organization in with to which push the
                        `Trainer`. (default: None)
  --push_to_hub_token PUSH_TO_HUB_TOKEN
                        The token to use to push to the Model Hub. (default:
                        None)
  --mp_parameters MP_PARAMETERS
                        Used by the SageMaker launcher to send mp-specific
                        args. Ignored in Trainer (default: )
  --auto_find_batch_size [AUTO_FIND_BATCH_SIZE]
                        Whether to automatically decrease the batch size in
                        half and rerun the training loop again each time a
                        CUDA Out-of-Memory was reached (default: False)
  --full_determinism [FULL_DETERMINISM]
                        Whether to call enable_full_determinism instead of
                        set_seed for reproducibility in distributed training.
                        Important: this will negatively impact the
                        performance, so only use it for debugging. (default:
                        False)
  --torchdynamo TORCHDYNAMO
                        This argument is deprecated, use
                        `--torch_compile_backend` instead. (default: None)
  --ray_scope RAY_SCOPE
                        The scope to use when doing hyperparameter search with
                        Ray. By default, `"last"` will be used. Ray will then
                        use the last checkpoint of all trials, compare those,
                        and select the best one. However, other options are
                        also available. See the Ray documentation (https://doc
                        s.ray.io/en/latest/tune/api_docs/analysis.html#ray.tun
                        e.ExperimentAnalysis.get_best_trial) for more options.
                        (default: last)
  --ddp_timeout DDP_TIMEOUT
                        Overrides the default timeout for distributed training
                        (value should be given in seconds). (default: 1800)
  --torch_compile [TORCH_COMPILE]
                        If set to `True`, the model will be wrapped in
                        `torch.compile`. (default: False)
  --torch_compile_backend TORCH_COMPILE_BACKEND
                        Which backend to use with `torch.compile`, passing one
                        will trigger a model compilation. (default: None)
  --torch_compile_mode TORCH_COMPILE_MODE
                        Which mode to use with `torch.compile`, passing one
                        will trigger a model compilation. (default: None)
  --dispatch_batches DISPATCH_BATCHES
                        Deprecated. Pass {'dispatch_batches':VALUE} to
                        `accelerator_config`. (default: None)
  --split_batches SPLIT_BATCHES
                        Deprecated. Pass {'split_batches':True} to
                        `accelerator_config`. (default: None)
  --include_tokens_per_second [INCLUDE_TOKENS_PER_SECOND]
                        If set to `True`, the speed metrics will include `tgs`
                        (tokens per second per device). (default: False)
  --include_num_input_tokens_seen [INCLUDE_NUM_INPUT_TOKENS_SEEN]
                        If set to `True`, will track the number of input
                        tokens seen throughout training. (May be slower in
                        distributed training) (default: False)
  --neftune_noise_alpha NEFTUNE_NOISE_ALPHA
                        Activates neftune noise embeddings into the model.
                        NEFTune has been proven to drastically improve model
                        performances for instrcution fine-tuning. Check out
                        the original paper here:
                        https://arxiv.org/abs/2310.05914 and the original code
                        here: https://github.com/neelsjain/NEFTune. Only
                        supported for `PreTrainedModel` and `PeftModel`
                        classes. (default: None)
  --optim_target_modules OPTIM_TARGET_MODULES
                        Target modules for the optimizer defined in the
                        `optim` argument. Only used for the GaLore optimizer
                        at the moment. (default: None)
  --model_name_or_path MODEL_NAME_OR_PATH
                        The model checkpoint for weights initialization.
                        (default: None)
  --model_revision MODEL_REVISION
                        The specific model version to use (can be a branch
                        name, tag name or commit id). (default: main)
  --torch_dtype {auto,bfloat16,float16,float32}
                        Override the default `torch.dtype` and load the model
                        under this dtype. If `auto` is passed, the dtype will
                        be automatically derived from the model's weights.
                        (default: None)
  --trust_remote_code [TRUST_REMOTE_CODE]
                        Trust remote code when loading a model. (default:
                        False)
  --attn_implementation ATTN_IMPLEMENTATION
                        Which attention implementation to use; you can run
                        --attn_implementation=flash_attention_2, in which case
                        you must install this manually by running `pip install
                        flash-attn --no-build-isolation` (default: None)
  --use_peft [USE_PEFT]
                        Whether to use PEFT or not for training. (default:
                        False)
  --lora_r LORA_R       LoRA R value. (default: 16)
  --lora_alpha LORA_ALPHA
                        LoRA alpha. (default: 32)
  --lora_dropout LORA_DROPOUT
                        LoRA dropout. (default: 0.05)
  --lora_target_modules LORA_TARGET_MODULES [LORA_TARGET_MODULES ...]
                        LoRA target modules. (default: None)
  --lora_modules_to_save LORA_MODULES_TO_SAVE [LORA_MODULES_TO_SAVE ...]
                        Model layers to unfreeze & train (default: None)
  --lora_task_type LORA_TASK_TYPE
                        The task_type to pass for LoRA (use SEQ_CLS for reward
                        modeling) (default: CAUSAL_LM)
  --load_in_8bit [LOAD_IN_8BIT]
                        use 8 bit precision for the base model - works only
                        with LoRA (default: False)
  --load_in_4bit [LOAD_IN_4BIT]
                        use 4 bit precision for the base model - works only
                        with LoRA (default: False)
  --bnb_4bit_quant_type BNB_4BIT_QUANT_TYPE
                        precise the quantization type (fp4 or nf4) (default:
                        nf4)
  --use_bnb_nested_quant [USE_BNB_NESTED_QUANT]
                        use nested quantization (default: False)
