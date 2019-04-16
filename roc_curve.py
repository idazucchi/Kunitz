# roc curve
import matplotlib.pyplot as plt
import sys
import numpy as np

def roc_curve(dataf):
	f = open(dataf)
	x = []
	y = []
	for line in f:
		if line[0:2]=='>>':
			line = line.split()
			y.append(line[2])
			x.append(line[4])
	#~ print(x,y)
	plt.plot(x,y)
	plt.show()
	
	
	
	
	
if __name__ == '__main__':
	datafile = sys.argv[1]
	roc_curve(datafile)
