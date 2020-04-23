import numpy as np

def arrayCreate(r,c):
	a = np.random.random(([r,c]))
	return a

a = arrayCreate(2,2)
print("Array of a : ",a)
b = arrayCreate(2,2)
print("Array of b : ",b)

c = np.multiply(a,b)
print("multiplication of a and b")
print("Array of c : ",c)