import sys

import read_data
from simulation.simulation import *

hurricane_list = read_data.read_file("../data/hurdat2-1851-2018-051019.csv")
# hurricane_list = read_data.read_file("../data/by_year/2018.csv")

num_landfall = 0
for hurricane in hurricane_list:
	if hurricane.made_landfall:
		num_landfall = num_landfall + 1

print "num_landfall: %d" % num_landfall
print "num: %d" % len(hurricane_list)
print float(num_landfall)/float(len(hurricane_list))

cpy1 = repeatDeepCopy(hurricane_list, 1)
cpy2 = repeatDeepCopy(hurricane_list, 1)

print "Copied!"

addTrackNoise(cpy1)
print "Done with noise 1"
pointwiseTrackNoise(cpy2)
print "Done with noise 2"

num_landfall = 0
for hurricane in cpy1:
	if hurricane.made_landfall:
		num_landfall = num_landfall + 1

print "Random walk"
print "num_landfall: %d" % num_landfall
print "num: %d" % len(hurricane_list)
print float(num_landfall)/float(len(hurricane_list))

num_landfall = 0
for hurricane in cpy2:
	if hurricane.made_landfall:
		num_landfall = num_landfall + 1

print "Pointwise"
print "num_landfall: %d" % num_landfall
print "num: %d" % len(hurricane_list)
print float(num_landfall)/float(len(hurricane_list))

from visualization.track import *
from visualization.storm_lifetime import *

inds = -np.arange(1,5)
hlist_1 = np.asarray(cpy1)[inds]
hlist_2 = np.asarray(cpy2)[inds]

plot_tracks_status(hlist_1)
plot_tracks_status(hlist_2)