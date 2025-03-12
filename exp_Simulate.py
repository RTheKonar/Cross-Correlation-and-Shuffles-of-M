from numpy.random import uniform as unif
import numpy as np
import matplotlib.pyplot as plt

from Shuffle import ShuffleM
#from cross_cor import CCC
from RinPy import res

def indepUnif(n):
	x= unif(0,1,n)
	y= unif(0,1,n)
	plt.scatter(x, y, c ="red")
	plt.show()

def depUnif(f,n):
	x= unif(0,1,n)
	y= np.zeros(n)
	for i in range(n):
		y[i]=f(x[i])
	plt.scatter(x, y, c ="blue")
	plt.grid(color='green', linestyle='--', linewidth=0.8)
	plt.grid(which='minor',linestyle=":", color='#CCCCCC', linewidth=0.5)
	plt.minorticks_on()
	'''major_ticks = np.linspace(0, 1, 3)
	minor_ticks = np.linspace(0, 1, 5)
	plt.set_xticks(major_ticks)
	plt.set_yticks(major_ticks)
	plt.set_xticks(minor_ticks, minor=True)
	plt.set_yticks(minor_ticks, minor=True)
	'''
	plt.show()

def cTestDep(m,n):
	data= np.zeros([n,2],dtype=float)
	data[:,0]= unif(0,1,n)
	s= ShuffleM(m)
	for i in range(n):
		data[i,1]= s.getSupportFn(data[i,0])
	#print(data)
	print(m,res(data))

def cTestIndep(n):
	data= np.zeros([n,2],dtype=float)
	data[:,0]= unif(0,1,n)
	data[:,1]= unif(0,1,n)
	print("Indep",res(data))


#indepUnif(1000)
m=500
#s=ShuffleM(m)
for i in range(1,202,10):
	cTestDep(i,10000)
#depUnif(s.getSupportFn,1000)
print(cTestIndep(10000))

m=1
s=ShuffleM(m)
depUnif(s.getSupportFn,1000)
