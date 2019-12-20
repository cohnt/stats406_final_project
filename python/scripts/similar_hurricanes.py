import sys

import read_data
from visualization.track import *
from visualization.storm_lifetime import *
from similarity import *

hurricane_list = read_data.read_file("../data/hurdat2-1851-2018-051019.csv")
n = len(hurricane_list)

ts_list = [hurricane_to_time_series(h) for h in hurricane_list]

delta = 21600
eps = 3
n_largest = 6

while True:
	my_pick = np.random.randint(low=0, high=n)

	sim_arr = np.zeros(n)
	for i in range(n):
		sim_arr[i] = M2(ts_list[my_pick], ts_list[i], delta, eps)

	largest_n = np.argpartition(sim_arr, -n_largest)[-n_largest:]
	hlist = [hurricane_list[i] for i in largest_n]
	plot_tracks_status(hlist)