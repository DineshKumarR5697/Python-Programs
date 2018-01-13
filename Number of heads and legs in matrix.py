## We count 35 heads and 94 legs among the chickens and rabbits in a farm.
##How many rabbits and how many chickens do we have? 
import numpy as np 
A = np.array([[1,1], [2,4]])
B = np.array([35,94])
C = np.linalg.solve(A, B)
print(C)

