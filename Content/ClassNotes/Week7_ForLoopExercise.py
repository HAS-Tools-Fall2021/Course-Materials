# Week 7: Python Exercise
# 1. Write a for loop to calculate the average 
# flow for every day in october (i.e. 31 values)
# 2. Do the same thing without using a for loop

# %%
import pandas as pd
import numpy as np

# %%
# You can start from the dataframe we have been creating for our homework. 
# Just make sure adjsut the filepath accordingly
filename = 'streamflow_week2.txt'
filepath = os.path.join('../data', filename)
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     parse_dates=['datetime']
                     )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# %%
# Solution 1: Write a for loop to calculate the average flow for every day in October
oct_mean = np.zeros(31)
for d in range(31):
    daytemp = d+1
    tempdata = data[(data['month']==10) & (data['day'] == daytemp)]
    oct_mean[d] = np.mean(tempdata['flow'])
    print('Iteration', d, 'Day=', daytemp, 'Flow=', oct_mean[d])


# %%
# Solution 2: Same thing without a for loop
oct_data = data[data['month']==10]
oct_mean2 = oct_data.groupby('day').mean()['flow']

# %%
# As a function 
def day_mean(month, daysinmonth, data):
    month_mean = np.zeros(daysinmonth)
    for d in range(daysinmonth):
        daytemp = d+1
        tempdata = data[(data['month'] == month) & (data['day'] == daytemp)]
        month_mean[d] = np.mean(tempdata['flow'])
        #print('Iteration', d, 'Day=', daytemp, 'Flow=', oct_mean[d])

    return month_mean


day_mean(2, 28, data)


# %%

def calc_median(monthpick, daysinmonth, startyear, data):
    my_median = np.zeros(daysinmonth)
    for d in range(daysinmonth):
        daytemp = d+1
        tempdata = data[(data['year'] >= startyear) & (
            data['month'] == monthpick) & (data['day'] == daytemp)]
        my_median[d] = np.median(tempdata['flow'])
    return my_median

favorite_month=10
calc_median(favorite_month, 31,2016, data)
# %%
