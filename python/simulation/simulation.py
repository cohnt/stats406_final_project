import numpy as np
from mpl_toolkits.basemap import Basemap
from copy import deepcopy
from hurricane import Hurricane

def addTrackNoise(hurricane_list, noise_type="normal", cov=np.array([[0.1, 0], [0, 0.1]]), radius=0.25):
	for hurricane in hurricane_list:
		track_len = len(hurricane.track)
		noise = np.zeros((track_len, 2))
		for i in range(track_len):
			if noise_type == "normal":
				noise[i,:] = np.random.multivariate_normal([0, 0], cov)
			elif noise_type == "uniform":
				noise[i,:] = radius * 2 * (np.random.rand(2) - 0.5)
		hurricane.track = hurricane.track + np.cumsum(noise, axis=0)

		# Check if landfall
		bm = Basemap()
		for i in range(track_len):
			[lat, lon] = hurricane.track[i]
			if(bm.is_land(lon, lat)):
				hurricane.made_landfall = True
				break
		else:
			hurricane.made_landfall = False

def pointwiseTrackNoise(hurricane_list, noise_type="normal", cov=np.array([[0.1, 0], [0, 0.1]]), radius=0.25):
	for hurricane in hurricane_list:
		track_len = len(hurricane.track)
		noise = np.zeros((track_len, 2))
		for i in range(track_len):
			if noise_type == "normal":
				noise[i,:] = np.random.multivariate_normal([0, 0], cov)
			elif noise_type == "uniform":
				noise[i,:] = radius * 2 * (np.random.rand(2) - 0.5)
		hurricane.track = hurricane.track + noise

		# Check if landfall
		bm = Basemap()
		for i in range(track_len):
			[lat, lon] = hurricane.track[i]
			if(bm.is_land(lon, lat)):
				hurricane.made_landfall = True
				break
		else:
			hurricane.made_landfall = False

def repeatDeepCopy(arr, num_repeats):
	new_arr = []
	for _ in range(num_repeats):
		new_arr.extend(deepcopy(arr))
	return new_arr