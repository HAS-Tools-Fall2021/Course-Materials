# Example solution for HW 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week2.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%

#1. Describe the variable flow_data:
#   - What is it?
#   - What type of values is is composed of?
#   - What is are its dimensions, and total size?
print('Type:', type(flow_data))
print('Data Type:', flow_data.dtype)
print('Shape:', flow_data.shape)
print('Size:', flow_data.size)
print('Dimensions:', flow_data.ndim)

#2. How many times was the daily flow greater than your prediction 
#   in the month of September (express your answer in terms of the total 
#   number of times and as a percentage)?
prediction = 500
greater = np.sum((flow_data[:,3] > prediction) & (flow_data[:,1]==9))
greater_pct = greater/np.sum(flow_data[:,1]==9) * 100
print("Flow was greater than predition", greater, "times")
print("this is", np.round(greater_pct,0), "% of the time")

#3. How would your answer to the previous question change if you 
#   considered only flows before 2000 or after 2010? 
#   (again report total number of times and percentage)
greater = np.sum((flow_data[:,3] > prediction) & 
          (flow_data[:,1]==9) & (flow_data[:,0]>=2010))
greater_pct = greater/np.sum((flow_data[:,1]==9) & 
            (flow_data[:,0]>=2010)) * 100
print("Flow was greater than predition", greater, "times in or after 2010")
print("this is", np.round(greater_pct,0), "% of the time")

greater = np.sum((flow_data[:,3] > prediction) & 
          (flow_data[:,1]==9) & (flow_data[:,0]<=2000))
          
greater_pct = greater/np.sum((flow_data[:,1]==9) & 
            (flow_data[:,0]<=2000)) * 100
print("Flow was greater than predition", greater, "times in or before 2000")
print("this is", np.round(greater_pct,0), "% of the time")

# 4. How does the flow generally change from the first half of
# September to the second?

index_list = (flow_data[:, 2] <= 15) & (flow_data[:, 1] == 9)
test = flow_data[index_list,3]
np.mean(test)

first_half = np.mean(flow_data[(flow_data[:,2] <= 15) & (flow_data[:,1]==9),3])

second_half = np.mean(flow_data[(flow_data[:,2] >= 15) & 
          (flow_data[:,1]==9),3])
print("First half average flows", np.mean(first_half))
print("Second half average flows", np.mean(second_half))
