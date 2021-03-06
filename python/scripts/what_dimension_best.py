import sys

import read_data
from visualization.track import *
from visualization.storm_lifetime import *
from similarity import *

from sklearn.decomposition import KernelPCA
from statsmodels.nonparametric.kernel_regression import KernelReg

hurricane_list = read_data.read_file("../data/by_year/2010-2018.csv")
# hurricane_list = read_data.read_file("../data/by_year/2000-2018.csv")
ts_list = [hurricane_to_time_series(h) for h in hurricane_list]

n = len(hurricane_list)
sim_mat = np.zeros((n, n))

delta = 21600
eps = 3

errs = []
errs_high_prob = []

count = 0
for i in range(0, n):
	for j in range(i, n):
		sim_mat[i][j] = M2(ts_list[i], ts_list[j], delta, eps)
		sim_mat[j][i] = sim_mat[i][j]

		count = count + 1
		if count % 1000 == 0:
			print count

n_check_ts = 12

# cv_hurricane_list = read_data.read_file("../data/by_year/1970-1999.csv")
cv_hurricane_list = read_data.read_file("../data/by_year/2000-2009.csv")
cv_ts_list = [hurricane_to_time_series(h)[0:np.min([n_check_ts, len(h.track)])] for h in cv_hurricane_list]
m = len(cv_hurricane_list)

data_matrix = np.zeros((m, n))

print "There are %d hurricanes for cross validation. So I need to perform %d comparisons." % (m, m*n)
count = 0

for i in range(len(cv_hurricane_list)):
	for j in range(n):
		data_matrix[i][j] = M2(cv_ts_list[i], ts_list[j], delta, eps)

		count = count + 1
		if count % 1000 == 0:
			print count

for target_dim in range(1, 20+1):
	print "\n\nChecking dimension %d" % target_dim
	print "There are %d hurricanes. So I need to perform %d comparisons." % (n, n*(n+1)/2)

	kpca = KernelPCA(n_components=target_dim, kernel="precomputed", eigen_solver="auto", tol=1e-9, max_iter=3000, n_jobs=-1)
	feature_coords = kpca.fit_transform((sim_mat**2) * -0.5)

	landfalls = np.array([float(h.made_landfall) for h in hurricane_list])

	inds = np.argsort(feature_coords[:,0])

	feature_coords_sorted = feature_coords[inds]
	landfalls_sorted = landfalls[inds]

	vartypes = ''.join('c' * target_dim)
	reg = KernelReg(landfalls_sorted, feature_coords_sorted, vartypes)
	[mean, mfx] = reg.fit()

	# plt.figure()
	# plt.scatter(feature_coords_sorted[:,0], landfalls_sorted, color="green")
	# plt.plot(feature_coords_sorted[:,0], mean, color="red")
	# plt.show()

	cv_feature_coords = kpca.transform((data_matrix**2) * -0.5)
	# print cv_feature_coords
	[cv_mean, cv_mfx] = reg.fit(cv_feature_coords)
	# print cv_mean

	cv_predicted = np.zeros(m)
	cv_high_prob = np.zeros(m) + 0.5
	num_high_prob = 0
	thresh = 0.05

	for i in range(m):
		if cv_mean[i] >= 0.5:
			cv_predicted[i] = 1

		if cv_mean[i] <= thresh:
			num_high_prob = num_high_prob + 1
			cv_high_prob[i] = 0
		if cv_mean[i] >= (1-thresh):
			num_high_prob = num_high_prob + 1
			cv_high_prob[i] = 1

	cv_actual = np.array([int(h.made_landfall) for h in cv_hurricane_list])

	# print cv_predicted
	# print cv_high_prob
	# print cv_actual

	num_correct = np.sum(cv_predicted == cv_actual)
	print "num_correct", num_correct
	print "m", m
	print float(num_correct)/float(m)

	errs.append(float(num_correct)/float(m))

	high_prob_correct = 0
	for i in range(m):
		if cv_high_prob[i] != 0.5 and cv_high_prob[i] == cv_actual[i]:
			high_prob_correct = high_prob_correct + 1

	print "high_prob_correct", high_prob_correct
	print "num_high_prob", num_high_prob
	print float(high_prob_correct)/float(num_high_prob)

	errs_high_prob.append(float(high_prob_correct)/float(num_high_prob))

plt.figure()
plt.plot(np.arange(start=1, stop=20+1), np.asarray(errs))
plt.xlabel("Dimension")
plt.ylabel("Accuracy")
plt.title("Accuracy vs Dimension")
plt.show()

plt.figure()
plt.plot(np.arange(start=1, stop=20+1), np.asarray(errs_high_prob))
plt.xlabel("Dimension")
plt.ylabel("Accuracy")
plt.title("Accuracy vs Dimension")
plt.show()