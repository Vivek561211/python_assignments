import numpy as np
a=np.array([[1,2,3],[5,6,7],[8,9,10]])
print(a,end="\n\n")
b=np.array([[8,9,10],[5,6,7],[1,2,3]])
print(b,end="\n\n")
#  Matrix operations
#1) Addition of two matrix
c=(np.add(a,b))
print("Addition of matrix is :\n",c,end="\n\n")
#2) Substraction of two matrix
e=(np.subtract(a,b))
print("Substraction of matrix is :\n",e,end="\n\n")
#3) Multiplication of two matrix
f=(np.multiply(a,b))
print("Multiplication of two matrix is :\n",f,end="\n\n")
#4) Division of two matrix 
g=(np.divide(a,b))
print("Division of matrix is :\n",g,end="\n\n")
#5) Summation of a matrix
print("Summation of a matrix is :",np.sum(a))
#6) Transpose of  matrix a
print("Transpose of matrix a is :",a.T,end="\n\n")


