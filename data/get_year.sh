#!/bin/bash

if [ $1 == "-h" ]
then
	echo "Usage: ./get_year.sh [YYYY]"
	echo "Years available: [1851,2018]"
	exit 0
fi

if ! [[ "$1" =~ ^[0-9]+$ ]] # From https://unix.stackexchange.com/questions/151654/checking-if-an-input-number-is-an-integer
then
	echo "Usage: ./get_year.sh [YYYY]"
	echo "Years available: [1851,2018]"
	exit 1
fi

if [ $1 -lt 1851 ]
then
	echo "No data from before 1851!"
	exit 1
fi

if [ $1 -gt 2018 ]
then
	echo "No data from after 2018!"
	exit 1
fi

datafile=hurdat2-1851-2018-051019.csv
data_out_dir=by_year

mkdir -p $data_out_dir

year=$1
let next_year=$year+1

if [ $year -eq 2018 ]
then
	sed_str="/^AL..${year}/,\$p"
	sed -n $sed_str $datafile > $data_out_dir/$year.csv
else
	sed_str="/^AL..${year}/,/^AL..${next_year}/p"
	sed -n $sed_str $datafile | head -n -1 > $data_out_dir/$year.csv
fi