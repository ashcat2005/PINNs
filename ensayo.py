import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
data = np.loadtxt('exodata.csv', delimiter=',')

X = data[:,0].reshape(1,40000)
Y = data[:,1].reshape(1,40000)
Z = data[:,2].reshape(1,40000)
print(X.shape)
print(X.min(), X.max())
S = np.random.rand(X.size).reshape(1,40000)
print(S.shape)
plt.figure()
plt.pcolormesh(X, Y, S,shading='gouraud') #, norm=colors.SymLogNorm(linthresh=0.03, linscale=0.03, vmin=-1.0, vmax=2300))
plt.show()

