import numpy as np
from datetime import datetime

def datetime_to_epoch(dt):
	return (dt - datetime(1970, 1, 1)).total_seconds()

def hurricane_to_time_series(hurricane):
	time_vec = [datetime_to_epoch(hurricane.data[i].time) for i in range(len(hurricane.data))]
	return [(time_vec[i], hurricane.track[i]) for i in range(len(hurricane.track))]

def M1(A, B, delta, eps_vec):
	pass

def M2(A, B, delta, eps_vec):
	pass

def LCSS(A, B, delta, eps_vec):
	pass

def SLC(A, B, delta, eps_vec):
	pass

def H(A):
	pass