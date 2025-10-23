import numpy as np
import csv
import re
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import peak_widths, find_peaks

def load_2col(filename):
	""" load a 2 column file to return to equally sized data arrays """
	
	xdata = []		#create empty array for x data
	ydata = []		#create empty array for y data
	
	with open(filename, 'r') as inputfile:	#open file
	
		lines = inputfile.readlines()
		
		for line in lines:	#splits file into lines, and lines into x and y values
			data = [_f for _f in re.split('[, \t]', line) if _f]
			if is_number(data[0]) and is_number(data[1]):
				xdata.append(float(data[0]))	#saves x data
				ydata.append(float(data[1]))	#saves y data
			
			
	return np.array(xdata), np.array(ydata)	#returns x and y data from imported file

def is_number(s):	#detects if value is a float
    try:				#if float, return true
        float(s)
        return True
    except ValueError:	#if not float, returns false
        return False	