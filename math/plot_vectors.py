
# Import libraries
import numpy as np
import matplotlib.pyplot as plt
  
# Vector origin location
X_1 = [-1]
Y_1 = [-1]
  
# Directional vectors
U_1 = [3]  
V_1 = [4]

# Vector origin location
X_2 = [-1]
Y_2 = [-1]
  
# Directional vectors
U_2 = [3]  
V_2 = [0]

# Vector origin location
X_3 = [2]
Y_3 = [-1]
  
# Directional vectors
U_3 = [0]  
V_3 = [4]

  
# Creating plot
plt.quiver(X_1, Y_1, U_1, V_1, color='purple', units='xy', angles='xy', scale_units='xy', scale=1)
plt.quiver(X_2, Y_2, U_2, V_2, color='red', units='xy', angles='xy', scale_units='xy', scale=1)
plt.quiver(X_3, Y_3, U_3, V_3, color='blue', units='xy', angles='xy', scale_units='xy', scale=1)
plt.title('Vector Magnitude')

plt.annotate('(-1,1)', xy=(-1.3,-1.3), xycoords='data', fontsize=12)
plt.annotate('(2,3)', xy=(2,3), xycoords='data', fontsize=12)
plt.annotate(r'||V|| = $\sqrt{u^2 + v^2}$', xy=(-1,3.5), xycoords='data', fontsize=12)
plt.annotate(r'      = $\sqrt{3^2 + 4^2}$', xy=(-1,3.0), xycoords='data', fontsize=12)
plt.annotate(r'      = $\sqrt{(25}$', xy=(-1,2.5), xycoords='data', fontsize=12)
plt.annotate(r'      = 5', xy=(-1,2.0), xycoords='data', fontsize=12)
plt.annotate(r'u = (2 - (-1)) = 3', xy=(-0.5,-1.5), xycoords='data', fontsize=12)
plt.annotate(r'v = (3 - (-1)) = 4', xy=(2.25,1), xycoords='data', fontsize=12)
  
# x-lim and y-lim
plt.xlim(-2, 5)
plt.ylim(-2, 5)
  
# Show plot with grid
plt.grid()
plt.show()