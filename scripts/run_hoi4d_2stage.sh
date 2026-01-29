# version=$1 ##1024, 512, 256
seed=42

ckpt1="/simurgh2/projects/Mask2IV/checkpoints/pretrained_mask2iv/first_stage/ckpt1.ckpt"
config1=/simurgh2/projects/Mask2IV/Mask2IV/configs/inference_512_hoi4d_first.yaml

# maskcat
ckpt2="/simurgh2/projects/Mask2IV/checkpoints/pretrained_mask2iv/second_stage/ckpt2.ckpt"
config2=/simurgh2/projects/Mask2IV/Mask2IV/configs/inference_512_hoi4d_maskcat.yaml

prompt_dir=/simurgh2/projects/Mask2IV/Mask2IV/prompts
res_dir="/simurgh2/projects/Mask2IV/Mask2IV/exp_outputs/Mask2IV-inference/maskcat/hoi4d"


python /simurgh2/projects/Mask2IV/Mask2IV/scripts/evaluation/inference_hoi4d_2stage.py \
--seed ${seed} \
--ckpt_path1 $ckpt1 \
--ckpt_path2 $ckpt2 \
--config1 $config1 \
--config2 $config2 \
--savedir $res_dir \
--n_samples 1 \
--bs 1 --height 320 --width 512 \
--unconditional_guidance_scale 1.0 \
--ddim_steps 50 \
--ddim_eta 1.0 \
--prompt_dir $prompt_dir \
--text_input \
--video_length 16 \
--timestep_spacing 'uniform_trailing' --guidance_rescale 0.7 --perframe_ae \
# --second_stage_only
