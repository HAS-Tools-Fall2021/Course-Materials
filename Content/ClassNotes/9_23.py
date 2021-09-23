# %%
import numpy as np
import pandas as pd 

# %%
#1. Get set of integers that is less than or equal to the division
# of the inputs x1 and x2 where x1 is all the integers from 1-10 and x2=1.3]

#Step1: create x1
x1 = np.array([i for i in range(1,11,1)])
x1 = [1,2,3,4,5,6,7,8,9,10]
x1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x1 = np.arange(10)+1
x1 = np.array(range(11))[1:11]
x1 = np.array(range(1, 11))
x1 = np.arange(1,11)

#step 2:ceate x2
x2 = 1.3

#step 3: get the answer
#example1
x3 = x1//x2
np.max(x3)

#eg2
np.max(np.floor(x1/x2))

#eg3
divide=x1/x2
floor = np.zeros(10)
for x in x1:
    floor[x-1] = np.floor(divide[x-1])

#eg4
answer = (x1/x2).astype(int)
    
    
     
# %%
#PANDAS!
# With pandas - we can can name our rows and columns and refer to them by names
# We don't have to have just one data type like with numpy 
# Builds off of numpy 

# Pandas - series
# Three things - Series, DataFrames and Indices
#making a pandas series - note when you print this that it
# has an extra column to the left --- this is the index!
data = pd.Series([0.1, 50, 47, 1.376])
data0= [0.1, 50, 47, 1.376]

#We can grab elements from the Series the same as we did with a numpy array
data[1:3]

# Or we can name our index differently 
data1 = pd.Series([0.1, 50, 47, 1.376], index=['a', 'b', 'c', 'd'])
data1['b':'d']
data1[0:2]

# our series has two things it has values and indices
data1.values  #this gives us just the values
data1.index #this is the index that goes with it

# %%
#Pandas - Dataframes
# these are like series but in 2D so we have rows and columns
# remember - the index is always refering to the row numbers/numes
rng = np.random.RandomState(42) # this holds my random numbers constant
dataframe = pd.DataFrame(rng.randint(0,10,(3,3)), columns=['b', 'a', 'c'], 
            index=['row1', 'row2', 'row3']) 

array = np.random.randn(3,3)

# Grab out a column of data
dataframe.b
np.mean(dataframe.b)

dataframe['b']
np.mean(dataframe['b'])

#grabing out the parts of our dataframe
dataframe.values
dataframe.index
dataframe.columns

# loc - lets you find rows by their names
dataframe.loc['row1']
dataframe.loc['row1', 'a']

# iloc - lets you find rows by their numbers
dataframe.iloc[0]
dataframe.iloc[0, 1]



dataframe2 = pd.DataFrame(rng.randint(0,10,(3,3)), columns=['b', 'a', 'c'], 
            index=['row3', 'row1', 'row']) 

dataframe + dataframe2


dataframe3 = pd.DataFrame(rng.randint(0,10,(3,3)), columns=['b', 'a', 'c'], 
            index=['row3', 'row1', 'row4']) 

dataframe + dataframe3

# Masking values
dataframe[dataframe['c']>8]

dataframe[dataframe.iloc[1:2,0:2] > 5]


# Sorting dataframes:

