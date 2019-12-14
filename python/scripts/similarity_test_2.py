import sys

import read_data
from visualization.track import *
from visualization.storm_lifetime import *
from simulation.simulation import *
from similarity import *

hurricane_list = read_data.read_file("../data/by_year/2018.csv")[0:2]

plot_tracks_status(hurricane_list)

ts1 = hurricane_to_time_series(hurricane_list[0])
ts2 = hurricane_to_time_series(hurricane_list[1])

print "\nM1"
for eps in range(1, 50):
	print M1(ts1, ts2, 21600, eps)

print "\nM2"
for eps in range(1, 50):
	print M2(ts1, ts2, 21600, eps)