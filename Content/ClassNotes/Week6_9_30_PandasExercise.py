import pandas as pd

# Pandas Indexing Exercise 1
# start with the following dataframe of all 1's
data = np.ones((7, 3))
data_frame = pd.DataFrame(data,
                          columns=['data1', 'data2', 'data3'],
                          index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# 1. Change the values for all of the vowel rows to 3
# 2. Multiply the first 4 rows by 7
# 3. Make the dataframe into a checkerboard  of 0's and 1's using loc
# 4. Same question as 3 but without using loc

#__________
# Solution 
# 1. Change the values for all of the vowel rows to 3
data_frame.loc[['a', 'e'], : ] = 3
data_frame.loc[['a', 'e']] = 3

data_frame.loc[('a', 'e'), :] = 3
data_frame.iloc[0]=3
data_frame.iloc[4]=4
data_frame.iloc[(0,4),:] = 4
data_frame.iloc[[0, 4], :] = 4

#2. multiply the first 4 rows by 7
data_frame.iloc[:4, ] *= 7
data_frame.iloc[0:4, :] = data_frame.iloc[0:4, :] * 7
data_frame2= data_frame.iloc[:4, ] * 7

#3. Make the dataframe into a checkerboard  of 0's and 1's using loc
data_frame2 = data_frame * 0 + 1
data_frame2.loc[['a', 'c', 'e', 'g'], ['data1', 'data3']] = 0
data_frame2.loc[['b', 'd', 'f'], ['data2']] = 0

#4. Do the same thing without using loc
data_frame3 = data_frame * 0 +1
data_frame3.iloc[0:8:2, 0:3:2] = 0
data_frame3.iloc[1:8:2, 1:3:2] = 0
