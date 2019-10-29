#!/bin/bash

if [ $1 == "-h" ]
then
	echo "Usage: ./get_years [YYYY] [YYYY]"
	echo "The interval is inclusive."
	echo "Years available: [1851,2018]"
	exit 0
fi

if ! [[ "$1" =~ ^[0-9]+$ ]] # From https://unix.stackexchange.com/questions/151654/checking-if-an-input-number-is-an-integer
then
	echo "Usage: ./get_years [YYYY] [YYYY]"
	echo "The interval is inclusive."
	echo "Years available: [1851,2018]"
	exit 1
fi

if ! [[ "$2" =~ ^[0-9]+$ ]] # From https://unix.stackexchange.com/questions/151654/checking-if-an-input-number-is-an-integer
then
	echo "Usage: ./get_years [YYYY] [YYYY]"
	echo "The interval is inclusive."
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
if [ $2 -lt 1851 ]
then
	echo "No data from before 1851!"
	exit 1
fi
if [ $2 -gt 2018 ]
then
	echo "No data from after 2018!"
	exit 1
fi
if [ $1 -gt $2 ]
then
	echo "The second year must be greater than or equal to the first!"
	exit 1
fi

datafile=hurdat2-1851-2018-051019.csv
data_out_dir=by_year

mkdir -p $data_out_dir

year1=$1
year2=$2
let next_year=$year2+1

if [ $year2 -eq 2018 ]
then
	sed_str="/^AL..${year1}/,\$p"
	sed -n $sed_str $datafile > $data_out_dir/$year1-$year2.csv
else
	sed_str="/^AL..${year1}/,/^AL..${next_year}/p"
	sed -n $sed_str $datafile | head -n -1 > $data_out_dir/$year1-$year2.csv
fi