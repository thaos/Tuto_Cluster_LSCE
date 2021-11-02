# Tuto_Cluster_LSCE

This tutorial will cover the following topics

- Basic commands in a terminal (navigation, file and folder creation, move, copy, script execution)
- File permissions (chmod)
- SSH connection (private public/ key), scp
- Module system (module load, ...)
- Disks on the cluster (du/df)
- Job submissions (qsub, qstat)

"Everything" will be done with the command line in a bash terminal.


### Examples with the following two scripts:

- download_ERA5_temperature.py 
- download_ERA5_temperature.sh scripts

Those scripts are used to download date frome the [Climate Data Store](https://cds.climate.copernicus.eu)

The aim is to show how to use those scripts on one's computer and the LSCE the server.

We will cover the following tasks

- [ ] Create a folder for the example. (check where we are, what is inside)
- [ ] Copy the scripts into the folder
- [ ] Execute it (shebang, make python and bash scripts executable)
- [ ] SSH connection, private/public key, copy  example forder to obelix.
- [ ] Give read/write/execute access to others.
- [ ] Load module to run the script
- [ ] Load module to look at the data downloaded ncdump/cdo.
- [ ] Run the scripts on obelix
- [ ] Prepare the script to be run in the job system 
- [ ] Show how to run the script in an interactive job.


### Some useful resources (cheatsheets):

https://cheatography.com/davechild/cheat-sheets/linux-command-line/

https://gif.biotech.iastate.edu/torque-pbs-job-management-cheat-sheet

https://www.nrel.gov/hpc/assets/pdfs/pbs-to-slurm-translation-sheet.pdf


### Some interesting commands:

man, whatis

top, ps

history

