CUDA_VISIBLE_DEVICES=$1 python tools/run.py --tasks vqa --datasets m4c_stvqa --model CT-HSR --seed $2 --config configs/vqa/m4c_stvqa/refine.yml --save_dir save/$3 --resume_file save/$4/best.ckpt 
