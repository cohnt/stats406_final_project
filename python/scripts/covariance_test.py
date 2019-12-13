import sys

import read_data
from visualization.track import *
from visualization.storm_lifetime import *
from simulation.simulation import *

hurricane_list = [read_data.read_file("../data/by_year/2018.csv")[0]]

plot_tracks_status(hurricane_list)
repeated_list = hurricane_list

for i in range(3):
	repeated_list = repeatDeepCopy(repeated_list, 2)

duplicate_list = repeatDeepCopy(repeated_list, 1)

addTrackNoise(repeated_list, cov=np.array([[2, 1], [1, 2]]))
addTrackNoise(duplicate_list, cov=np.array([[2, -1], [-1, 2]]))

plot_tracks_status(repeated_list)
plot_tracks_status(duplicate_list)