#!/usr/bin/env bash


# From https://stackoverflow.com/questions/59942315/starting-jupyter-notebook-on-a-node-of-my-cluster-high-performance-computation
#PBS -N Notebook
#PBS -j oe



cd $PBS_O_WORKDIR

module load python/3.6

NOTEBOOK_LOGFILE=jupyterlog.out

jupyter notebook --no-browser --ip=0.0.0.0 --port=8890 > ${NOTEBOOK_LOGFILE} 2>&1
