import sys

import read_data
from visualization.track import *
from visualization.storm_lifetime import *
from similarity import *

# hurricane_list = read_data.read_file("../data/hurdat2-1851-2018-051019.csv")
# hurricane_list = read_data.read_file("../data/by_year/2000-2018.csv")
hurricane_list = read_data.read_file("../data/by_year/2010-2018.csv")
# hurricane_list = read_data.read_file("../data/by_year/1970-2018.csv")

ts_list = [hurricane_to_time_series(h) for h in hurricane_list]

n = len(hurricane_list)
sim_mat_1 = np.zeros((n, n))
sim_mat_2 = np.zeros((n, n))
sim_mat_3 = np.zeros((n, n))

delta = 21600
eps = 3

print "There are %d hurricanes. So I need to perform %d comparisons." % (n, n*(n+1)/2)
count = 0

for i in range(0, n):
	for j in range(i, n):
		sim_mat_1[i][j] = M1(ts_list[i], ts_list[j], delta, eps)
		sim_mat_1[j][i] = sim_mat_1[i][j]

		sim_mat_2[i][j] = M2(ts_list[i], ts_list[j], delta, eps)
		sim_mat_2[j][i] = sim_mat_1[i][j]

		sim_mat_3[i][j] = M3(ts_list[i], ts_list[j], delta, eps)
		sim_mat_3[j][i] = sim_mat_1[i][j]

		count = count + 1
		if count % 1000 == 0:
			print count

n_largest = 4

while True:
	my_pick = np.random.randint(low=0, high=len(ts_list))

	sim_arr_1 = sim_mat_1[my_pick]
	sim_arr_2 = sim_mat_2[my_pick]
	sim_arr_3 = sim_mat_3[my_pick]

	largest_5_1 = np.argpartition(sim_arr_1, -n_largest)[-n_largest:]
	largest_5_2 = np.argpartition(sim_arr_2, -n_largest)[-n_largest:]
	largest_5_3 = np.argpartition(sim_arr_3, -n_largest)[-n_largest:]

	hlist_1 = [hurricane_list[i] for i in largest_5_1]
	hlist_2 = [hurricane_list[i] for i in largest_5_2]
	hlist_3 = [hurricane_list[i] for i in largest_5_3]

	hlist_1.append(hurricane_list[my_pick])
	hlist_2.append(hurricane_list[my_pick])
	hlist_3.append(hurricane_list[my_pick])

	plot_tracks_status(hlist_1)
	plot_tracks_status(hlist_2)
	plot_tracks_status(hlist_3)