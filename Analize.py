import pandas as pd
import numpy as np
import seaborn as sns
import datetime
from scipy import stats
import matplotlib.pyplot as plt

# importing the data set ***** important all data was cleaned using sqlserver Inteligente Business and SQL to fill all the missing data with mean value of the collumns
# some rows was with categorical data in a numerical column that rows was replaced with mean of that column
# some fare amount was 0.00 and that can be free ride " i guess" so a replace that also 
# i didnt know what to do with trip_distance = 0 so a didnt do nothing but i was thinking to delete the row 
dataset_Final = pd.read_csv('yellow_tripdata_2018-01.csv')
dataset_Final = pd.read_csv('yellow_tripdata_2018-02.csv')
dataset_Final = pd.read_csv('yellow_tripdata_2018-03.csv')
dataset_Final = pd.read_csv('yellow_tripdata_2018-04.csv')
dataset_Final = pd.read_csv('yellow_tripdata_2018-05.csv')
dataset_Final = pd.read_csv('yellow_tripdata_2018-06.csv')

# join all parts of data set 
lista = [dataset1, dataset2, dataset3, dataset4, dataset5, dataset6]
dataset_Final = pd.concat(lista)

# Exporting a complete data set 
dataset_Final.to_csv('yellow_tripdata_2018.csv')

# Cleaning the labels 
dataset_Final.columns = ['VendorID', 'pickup_datetime', 'dropoff_datetime',
       'passenger_count', 'trip_distance', 'RatecodeID', 'store_and_fwd_flag',
       'PULocationID', 'DOLocationID', 'payment_type', 'fare_amount', 'extra',
       'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge',
       'total_amount']


# What are the time slots with more passengers? how we can see in this plot the period of more intensive use 
# is beetweem 19 to 21:00
dataset_Final['hour'] = pd.DatetimeIndex(dataset_Final['pickup_datetime']).hour
a = sns.distplot(dataset_Final.hour, bins=24)

# In what period of the year Taxis are used more?
dataset_Final['month'] = pd.DatetimeIndex(dataset_Final['pickup_datetime']).month
s = sns.distplot(dataset_Final.month, bins=12)

# Do the all trips last the same? We can see in thes column that not every trip are the same some is faster or not 
dataset_Final['dif'] = pd.to_datetime(dataset_Final['dropoff_datetime']) - pd.to_datetime(dataset_Final['pickup_datetime'])
print(dataset_Final['dif'])

# What is the most common way of payments? if this chart we can see clearily that credit cards is the common way of payments
pay_plot = sns.distplot(dataset_Final.payment_type)
chi_square_value = stats.chisquare(dataset_Final.payment_type)
print(chi_square_value)

# Does a long distance correlate with the duration of the trip on average? in this plot we can see that is not sure the longest 
# distance is more time consuming 
dataset_Final['trip_distance'] = dataset_Final['trip_distance']*1000
dataset_Final['dif'] = dataset_Final['dif'].dt.total_seconds()
sns.lmplot(x='trip_distance', y="dif", data=dataset_Final)

pearson_coefficient = stats.pearsonr(dataset_Final['trip_distance'], dataset_Final['dif'])
print(pearson_coefficient)


# Core Research Questions
# Compute the price per km equation for each trip.
dataset_Final['price_km'] = dataset_Final['fare_amount'] / dataset_Final['trip_distance']

# Run the mean and the standard deviation of the new variable for each borough. Then plot the distribution. What do you see?
mean = dataset_Final['price_km'].mean(skipna=True)
print(mean)
print (dataset_Final['price_km'].std())

# Run the t-test among all the possible pairs of distribution of different boroughs.Run the t-test among all the possible pairs of distribution of different boroughs.
t_test1 = stats.ttest_ind(dataset_Final['fare_amount'], dataset_Final['trip_distance'], equal_var=False)
print(t_test1)

t_test2 = stats.ttest_ind(dataset_Final['trip_distance'], dataset_Final['dif'], equal_var=False)
print(t_test2)

t_test3 = stats.ttest_ind(dataset_Final['trip_distance'], dataset_Final['total_amount'], equal_var=False)
print(t_test3)


t_test4 = stats.ttest_ind(dataset_Final['trip_distance'], dataset_Final['tip_amount'], equal_var=False)
print(t_test4)

t_test5 = stats.ttest_ind(dataset_Final['RatecodeID'], dataset_Final['tip_amount'], equal_var=False)
print(t_test5)

t_test6 = stats.ttest_ind(dataset_Final['tip_amount'], dataset_Final['fare_amount'], equal_var=False)
print(t_test6)













