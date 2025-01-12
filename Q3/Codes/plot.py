import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load the shared library
lib = ctypes.CDLL('./lib.so')

# Set argument and return types for the C functions
lib.trapezoidal.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_double]
lib.function.argtypes=[ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int]

# Parameters
x_start = 0
x_end = 6.3
h = 0.1
n_steps = 64

#Setting up the arrays
area_x = np.linspace(x_start, x_end, n_steps)
area_y = np.zeros(n_steps)
y=np.zeros(n_steps)

#Conversion to ctypes array
area_x_ctypes = area_x.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
area_y_ctypes = area_y.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
y_ctypes = y.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

# Call the C functions
lib.function(area_x_ctypes, y_ctypes, n_steps)
lib.trapezoidal(area_x_ctypes,area_y_ctypes, n_steps,h)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(area_x, y, label="Theory", linestyle='-', color='b',linewidth=10)
plt.fill_between(area_x, 0, y, color="lightblue", alpha=0.5, label="Area")
print(f'The area enclosed is {4*area_y[16]}')
plt.xlabel("x")
plt.ylabel("y")
#plt.legend()
plt.legend(['Theory',f'Area={4*area_y[16]}'])
plt.grid()
#plt.show()
plt.savefig('plot.png')




