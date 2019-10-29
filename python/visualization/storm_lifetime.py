import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import date2num

def plot_lifetime_max_wind(hurricane):
	xvals = [d.time for d in hurricane.data]
	yvals = [d.max_wind for d in hurricane.data]

	fig, ax = plt.subplots()
	ax.plot_date(date2num(xvals), yvals, 'b-')
	ax.set_ylim([0,200])
	plt.show()