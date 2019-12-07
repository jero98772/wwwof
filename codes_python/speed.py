import time
import numpy as np
start=time.time()
def matrix(min_,max_,size):
    matrix=np.random.RandomState(100).uniform(min_,max_,size)
    return matrix

nm=8500
mat1=matrix(-nm,nm,(nm,nm))
mat2=matrix(-nm,nm,(nm,nm))
mat1*mat2
finish=time.time()
print(finish-start)
