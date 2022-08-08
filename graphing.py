import numpy as np
import matplotlib.pyplot as plt

#Sequence of Data Headers
#X/30.0,Y,sig11/4.0,sig22/4.0,sig12/4.0

#Import .dat file and plot data
data = np.loadtxt('analytical.dat')
plt.plot(data[:,0],data[:,2],label='sig11')
plt.plot(data[:,0],data[:,3],label='sig22')
plt.plot(data[:,0],data[:,4],label='sig12')
plt.legend()
plt.xlabel('X')
plt.ylabel('Sig')
plt.title('Sig11, Sig22, Sig12')
plt.savefig('sig.png')
