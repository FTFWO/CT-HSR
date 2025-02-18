CUDA_VISIBLE_DEVICES=$1 python tools/run.py --tasks vqa --datasets m4c_stvqa --model CT-HSR --pretrain --seed $2 --config configs/vqa/m4c_stvqa/pretrain.yml --save_dir save/$3 
