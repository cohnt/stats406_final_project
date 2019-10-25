import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def plot_track_raw(track):

	fix, ax = plt.subplots()
	ax.scatter(track[:,0], track[:,1])
	plt.show()

def plot_track_map(track):
	track = np.asarray(track)
	
	# Heavily based on:
	# https://matplotlib.org/basemap/users/mapcoords.html
	# https://matplotlib.org/basemap/users/examples.html
	m = Basemap(llcrnrlon=-100.,llcrnrlat=0.,urcrnrlon=-20.,urcrnrlat=57.,
	            projection='lcc',lat_1=20.,lat_2=40.,lon_0=-60.,
	            resolution ='l',area_thresh=1000.)
	m.drawcoastlines()
	m.drawcountries()
	m.drawmapboundary(fill_color='#99ffff')
	m.fillcontinents(color='#cc9966',lake_color='#99ffff')
	m.drawparallels(np.arange(10, 70, 20),labels=[1, 1, 0, 0])
	m.drawmeridians(np.arange(-100, 0, 20),labels=[0, 0, 0, 1])

	m.plot(track[:,0], track[:,1], latlon=True)

	plt.show()

def plot_tracks_map(track_list):
	m = Basemap(llcrnrlon=-100.,llcrnrlat=0.,urcrnrlon=20.,urcrnrlat=60.,
	            projection='lcc',lat_1=20.,lat_2=40.,lon_0=-60.,
	            resolution ='l',area_thresh=1000.)
	m.drawcoastlines()
	m.drawcountries()
	m.drawmapboundary(fill_color='#99ffff')
	m.fillcontinents(color='#cc9966',lake_color='#99ffff')
	m.drawparallels(np.arange(10, 70, 20),labels=[1, 1, 0, 0])
	m.drawmeridians(np.arange(-100, 0, 20),labels=[0, 0, 0, 1])

	for track in track_list:
		track = np.asarray(track)
		m.plot(track[:,0], track[:,1], latlon=True)

	plt.show()

def plot_track_status(hurricane):
	m = Basemap(llcrnrlon=-100.,llcrnrlat=0.,urcrnrlon=20.,urcrnrlat=60.,
	            projection='lcc',lat_1=20.,lat_2=40.,lon_0=-60.,
	            resolution ='l',area_thresh=1000.)
	m.drawcoastlines()
	m.drawcountries()
	m.drawmapboundary(fill_color='#99ffff')
	m.fillcontinents(color='#cc9966',lake_color='#99ffff')
	m.drawparallels(np.arange(10, 70, 20),labels=[1, 1, 0, 0])
	m.drawmeridians(np.arange(-100, 0, 20),labels=[0, 0, 0, 1])

	for i in range(0, len(hurricane.track)-1):
		x = [hurricane.track[i][0], hurricane.track[i+1][0]]
		y = [hurricane.track[i][1], hurricane.track[i+1][1]]
		c = "blue"
		if hurricane.data_lines[i].system_status == "HU":
			c = "red"
		m.plot(x, y, latlon=True, color=c)

	plt.show()

def plot_tracks_status(hurricane_list):
	m = Basemap(llcrnrlon=-100.,llcrnrlat=0.,urcrnrlon=20.,urcrnrlat=60.,
	            projection='lcc',lat_1=20.,lat_2=40.,lon_0=-60.,
	            resolution ='l',area_thresh=1000.)
	m.drawcoastlines()
	m.drawcountries()
	m.drawmapboundary(fill_color='#99ffff')
	m.fillcontinents(color='#cc9966',lake_color='#99ffff')
	m.drawparallels(np.arange(10, 70, 20),labels=[1, 1, 0, 0])
	m.drawmeridians(np.arange(-100, 0, 20),labels=[0, 0, 0, 1])

	for hurricane in hurricane_list:
		for i in range(0, len(hurricane.track)-1):
			x = [hurricane.track[i][0], hurricane.track[i+1][0]]
			y = [hurricane.track[i][1], hurricane.track[i+1][1]]
			c = "blue"
			if hurricane.data_lines[i].system_status == "HU":
				c = "red"
			m.plot(x, y, latlon=True, color=c)

	plt.show()