# 1. Exercise 1
# 1a. Create a 6 by 12 matrix of random numbers (6 rows, 12 columns)
# 1b. Report the average and standard deviation for the entire matrix rounded to two decimal places
# 1c. Report the mean for the 3rd column
# 1s. Report the mean for every row and for every column
import numpy as np
import random

#a. making a matrix of random numbers
test = np.random.randint(1, 100, (6, 12))
rand = np.random.randn(6, 12)
test2= [[1,2,3,4,5,6,78,9,10,11,12], 
        [1, 2, 3, 4, 5, 6, 78, 9, 10, 11, 12],
        [1, 2, 3, 4, 5, 6, 78, 9, 10, 11, 12],
        [1, 2, 3, 4, 5, 6, 78, 9, 10, 11, 12],
        [1, 2, 3, 4, 5, 6, 78, 9, 10, 11, 12],
        [1, 2, 3, 4, 5, 6, 78, 9, 10, 11, 12]]
array1 = np.ones((6,12))*8

#b.
# done in one step
np.round(np.mean(test),2)
# done in two steps
mean=np.mean(test)
meanround=np.round(mean,2)

print("Average =", np.round(np.mean(rand), 2),
      "stdev=", np.round(np.std(rand), 2))


#c. 
np.round(np.mean(test[:,2]),2)
print("3rd Column Mean =", np.round(np.mean(rand[:, 2]), 2))


#c
print("Row Averages =", np.round(np.mean(rand, axis=1), 2))
print("Column =", np.round(np.mean(rand, axis=0), 2))
