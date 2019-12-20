import sys

import read_data

hurricane_list = read_data.read_file("../data/hurdat2-1851-2018-051019.csv")

num_landfall = 0
for hurricane in hurricane_list:
	if hurricane.made_landfall:
		num_landfall = num_landfall + 1

print "num_landfall: %d" % num_landfall
print "num: %d" % len(hurricane_list)
print float(num_landfall)/float(len(hurricane_list))