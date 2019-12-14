import numpy as np
from datetime import datetime

def datetime_to_epoch(dt):
	return (dt - datetime(1970, 1, 1)).total_seconds()

def hurricane_to_time_series(hurricane):
	time_vec = [datetime_to_epoch(hurricane.data[i].time) for i in range(len(hurricane.data))]
	return [(time_vec[i]-time_vec[0], hurricane.track[i]) for i in range(len(hurricane.track))]

def M1(A, B, delta, eps):
	l1 = len(A)
	l2 = len(B)
	return LCSS(A, B, delta, eps) / np.min(l1, l2)

def M2(A, B, delta, eps):
	l1 = len(A)
	l2 = len(B)
	return SLC(A, B, delta, eps) / np.min(l1, l2)

def LCSS(A, B, delta, eps):
	if len(A) == 0 or len(B) == 0:
		return 0
	else:
		arr = np.zeros(len(A)+1, len(B)+1)
		for i in range(1, len(A)+1):
			for j in range(1, len(B)+1):
				# Check time distance and real distance
				if abs(A[i][0]-B[j][0]) < delta and norm(np.asarray(A[i][1])-np.asarray(B[j][1])) < eps:
					arr[i][j] = arr[i-1][j-1] + 1
				else:
					arr[i][j] = np.max(arr[i-1][j], arr[i][j-1])
		return arr[len(A), len(B)]

def SLC(A, B, delta, eps):
	pass

def H(A):
	pass