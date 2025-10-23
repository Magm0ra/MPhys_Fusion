import numpy as np
import csv
import re
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import peak_widths, find_peaks

def load_2col(filename):
	""" load a 2 column file to return to equally sized data arrays """
	
	xdata = []
	ydata = []
	
	with open(filename, 'r') as inputfile:
	
		lines = inputfile.readlines()
		
		for line in lines:
			data = [_f for _f in re.split('[, \t]', line) if _f]
			if is_number(data[0]) and is_number(data[1]):
				xdata.append(float(data[0]))
				ydata.append(float(data[1]))
			
			
	return np.array(xdata), np.array(ydata)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False	