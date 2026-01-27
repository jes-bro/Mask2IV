#!/bin/bash
#SBATCH --account=simurgh
#SBATCH --partition=simurgh --qos=normal
#SBATCH --time=168:00:00
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=256G

# only use the following on partition with GPUs
#SBATCH --gres=gpu:l40s:2

#SBATCH --job-name="train mask2IV"
#SBATCH --output=sample-%j.out

# only use the following if you want email notification
#SBATCH --mail-user=jesb@stanford.edu
#SBATCH --mail-type=ALL

# list out some useful information (optional)
echo "SLURM_JOBID="$SLURM_JOBID
echo "SLURM_JOB_NODELIST"=$SLURM_JOB_NODELIST
echo "SLURM_NNODES"=$SLURM_NNODES
echo "SLURMTMPDIR="$SLURMTMPDIR
echo "working directory = "$SLURM_SUBMIT_DIR

# sample process (list hostnames of the nodes you've requested)
source ~/.bashrc
conda deactivate
conda activate dyncraft
sh /simurgh2/projects/Mask2IV/Mask2IV/configs/training_512_v1.0/run_first.sh hoi4d

# can try the following to list out which GPU you have access to
#srun /usr/local/cuda/samples/1_Utilities/deviceQuery/deviceQuery

# done
echo "Done"
