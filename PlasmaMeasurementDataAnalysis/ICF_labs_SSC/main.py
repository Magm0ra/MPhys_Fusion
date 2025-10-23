import numpy as np
import csv
import re
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import peak_widths, find_peaks
from SSC_functions import load_2col



if __name__ == "__main__":
    xdata, ydata = load_2col("ICF_labs_SSC_data//initial_data.csv") #load data
    plt.plot(xdata,ydata)   #plot data
    plt.grid(True)
    plt.xlabel("Pixels")
    plt.ylabel("Gray Value")
    plt.show()