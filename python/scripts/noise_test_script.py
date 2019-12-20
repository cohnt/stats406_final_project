import sys

import read_data
from visualization.track import *
from visualization.storm_lifetime import *
from simulation.simulation import *

hurricane_list = [read_data.read_file("../data/by_year/2018.csv")[0]]

plot_tracks_status(hurricane_list)

repeated_list = repeatDeepCopy(hurricane_list, 10)
addTrackNoise(repeated_list)

plot_tracks_status(repeated_list)

repeated_list = repeatDeepCopy(hurricane_list, 10)
pointwiseTrackNoise(repeated_list)

plot_tracks_status(repeated_list)