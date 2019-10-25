import numpy as np
import matplotlib.pyplot as plt

def plot_track_raw(track):
	track = np.asarray(track)
	fix, ax = plt.subplots()
	ax.scatter(track[:,0], track[:,1])
	plt.show()