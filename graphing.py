import numpy as np
import matplotlib.pyplot as plt

#Sequence of Data Headers
#X,Y,sig11,sig22,sig12

print("Reading Data from analytical.dat")
#Import .dat file and plot data
data = np.loadtxt('analytical.dat')

#Filter
data = data[data[:,0] < 8]

plt.plot(data[:,0],data[:,2],label='sig11')
plt.plot(data[:,0],data[:,3],label='sig22')
plt.plot(data[:,0],data[:,4],label='sig12')
plt.legend()
plt.xlabel('X')
plt.ylabel('Sig')
plt.title('Sig11, Sig22, Sig12')
plt.savefig('sig.png')
