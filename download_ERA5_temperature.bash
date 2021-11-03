#!/usr/bin/env bash
set -o errexit
set -o nounset
set -o pipefail


variable=2m_temperature
interpolator=remapbic

files_tomerge=""
#tmp_dir=$(mktemp -d)
tmp_dir="tmp.temperature"
echo "Created temp working directory $tmp_dir"
#  deletes the temp directory
function cleanup {
  rm -rf $tmp_dir
  echo "Deleted temp working directory $tmp_dir"
}
# register the cleanup function to be called on the EXIT signal
# trap cleanup EXIT

for year in {1979..2019}; do
  for month in {01..12}; do
    filename=$tmp_dir/${variable}_$year$month.nc
    files_tomerge="${files_tomerge} ${filename}"
    until ./download_ERA5_temperature.py -y $year -m $month -v $variable
    do
      sleep 60
      echo "Trying again"
    done
    cdo -${interpolator},target_grid.txt -daymean t2m.nc $filename
    rm t2m.nc
  done
done
cdo -O mergetime $files_tomerge "${variable}_ERA5.nc"
