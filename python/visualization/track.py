import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib import cm

def plot_track_raw(track):

	fix, ax = plt.subplots()
	ax.scatter(track[:,0], track[:,1])
	plt.show()

def plot_track_map(track, m=None, linewidth=2):
	if m == None:
		m=create_default_map()

	track = np.asarray(track)

	plot_tracks_map([track], m, linewidth=linewidth)

def plot_tracks_map(track_list, m=None, linewidth=2):
	if m == None:
		m=create_default_map()

	for track in track_list:
		track = np.asarray(track)
		m.plot(track[:,0], track[:,1], latlon=True, linewidth=linewidth)

	plt.show()

def plot_track_status(hurricane, m=None, linewidth=2):
	if m == None:
		m=create_default_map()

	plot_tracks_status([hurricane], m, linewidth=linewidth)

def plot_tracks_status(hurricane_list, m=None, linewidth=2):
	if m == None:
		m=create_default_map()

	for hurricane in hurricane_list:
		for i in range(0, len(hurricane.track)-1):
			x = [hurricane.track[i][0], hurricane.track[i+1][0]]
			y = [hurricane.track[i][1], hurricane.track[i+1][1]]
			c = "blue"
			if hurricane.lines[i].system_status == "HU":
				c = "red"
			m.plot(x, y, latlon=True, color=c, linewidth=linewidth)

	plt.show()

def plot_tracks_wind_speed(hurricane_list, m=None, color_max_wind=120.0, linewidth=2):
	if m == None:
		m=create_default_map()

	# color_max_wind is the highest wind speed which is displayed as its own color

	for hurricane in hurricane_list:
		for i in range(0, len(hurricane.track)-1):
			x = [hurricane.track[i][0], hurricane.track[i+1][0]]
			y = [hurricane.track[i][1], hurricane.track[i+1][1]]
			c = cm.cool(hurricane.lines[i].max_wind / color_max_wind)
			m.plot(x, y, latlon=True, color=c, linewidth=linewidth)

	plt.show()

def create_default_map():
	# Heavily based on:
	# https://matplotlib.org/basemap/users/mapcoords.html
	# https://matplotlib.org/basemap/users/examples.html
	m = Basemap(llcrnrlon=-100.,llcrnrlat=0.,urcrnrlon=20.,urcrnrlat=60.,
	            projection='lcc',lat_1=20.,lat_2=40.,lon_0=-60.,
	            resolution ='l',area_thresh=1000.)
	m.drawcoastlines()
	m.drawcountries()
	m.drawmapboundary(fill_color='#99ffff')
	m.fillcontinents(color='#cc9966',lake_color='#99ffff')
	m.drawparallels(np.arange(10, 70, 20),labels=[1, 1, 0, 0])
	m.drawmeridians(np.arange(-100, 0, 20),labels=[0, 0, 0, 1])
	return m

def create_gulf_map():
	pass

def create_florida_map():
	m = Basemap(llcrnrlon=-85.,llcrnrlat=20.,urcrnrlon=-75.,urcrnrlat=35.,
	            projection='lcc',lat_1=20.,lat_2=40.,lon_0=-60.,
	            resolution ='l',area_thresh=1000.)
	m.drawcoastlines()
	m.drawcountries()
	m.drawmapboundary(fill_color='#99ffff')
	m.fillcontinents(color='#cc9966',lake_color='#99ffff')
	m.drawparallels(np.arange(10, 70, 20),labels=[1, 1, 0, 0])
	m.drawmeridians(np.arange(-100, 0, 20),labels=[0, 0, 0, 1])
	return m