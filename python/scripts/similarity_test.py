import sys

import read_data
from visualization.track import *
from visualization.storm_lifetime import *
from simulation.simulation import *
from similarity import *

hurricane_list = [read_data.read_file("../data/by_year/2018.csv")[0]]

repeated_list = repeatDeepCopy(hurricane_list, 2)
addTrackNoise(repeated_list)

plot_tracks_status(repeated_list)

ts1 = hurricane_to_time_series(repeated_list[0])
ts2 = hurricane_to_time_series(repeated_list[1])

for eps in range(1, 6):
	print M1(ts1, ts2, 21600, eps)