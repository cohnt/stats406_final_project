import sys

import read_data
from visualization.track import *
from visualization.storm_lifetime import *
from similarity import *

# hurricane_list = read_data.read_file("../data/hurdat2-1851-2018-051019.csv")
# hurricane_list = read_data.read_file("../data/by_year/2000-2018.csv")
# hurricane_list = read_data.read_file("../data/by_year/2010-2018.csv")
# hurricane_list = read_data.read_file("../data/by_year/1970-2018.csv")
hurricane_list = read_data.read_file("../data/by_year/2018.csv")

ts_list = [hurricane_to_time_series(h) for h in hurricane_list]

n = len(hurricane_list)
sim_mat = np.zeros((n, n))

delta = 21600
eps = 3

print "There are %d hurricanes. So I need to perform %d comparisons." % (n, n*(n+1)/2)
count = 0

for i in range(0, n):
	for j in range(i, n):
		sim_mat[i][j] = M2(ts_list[i], ts_list[j], delta, eps)
		sim_mat[j][i] = sim_mat[i][j]

		count = count + 1
		if count % 1000 == 0:
			print count

target_dim = 7

from sklearn.decomposition import KernelPCA
kpca = KernelPCA(n_components=target_dim, kernel="precomputed", eigen_solver="auto", tol=1e-9, max_iter=3000, n_jobs=-1)
feature_coords = kpca.fit_transform((sim_mat**2) * -0.5)

