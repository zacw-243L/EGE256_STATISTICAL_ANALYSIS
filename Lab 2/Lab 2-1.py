import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read mtcars.csv
start_time = time.time()
mtcars = pd.read_csv('mtcars.csv')

five_num = [mtcars["mpg"].quantile(0),
            mtcars["mpg"].quantile(0.25),
            mtcars["mpg"].quantile(0.50),
            mtcars["mpg"].quantile(0.75),
            mtcars["mpg"].quantile(1)]

mtcars = mtcars.rename(columns={'Unnamed: 0': 'model'})
mtcars.index = mtcars.model

del mtcars['model']
print(mtcars.head())
print(mtcars.mean())
print(mtcars.median())
print(mtcars.mode())
print('range of mpg = %0.2f' % (max(mtcars["mpg"]) - min(mtcars["mpg"])))
print(five_num)
print(mtcars["mpg"].describe())
print('IQR of mpg = %0.2f' % (mtcars["mpg"].quantile(0.75) - mtcars["mpg"].quantile(0.25)))
plt.figure()
mtcars.boxplot(column="mpg", return_type="axes")
plt.text(x=0.74, y=22.25, s="3rd Quartile")
plt.text(x=0.8, y=18.75, s="Median")
plt.text(x=0.75, y=15.5, s="1st Quartile")
plt.text(x=0.9, y=10, s="Min")
plt.text(x=0.9, y=33.5, s="Max")
plt.text(x=0.7, y=18, s="IQR", rotation=90, size=25)
print('variance of mpg = %0.2f' % mtcars["mpg"].var())
print('standard deviation of mpg = %0.2f' % mtcars["mpg"].std())
print('skew of mpg = %0.2f' % mtcars["mpg"].skew())
print("--- %s seconds ---" % (time.time() - start_time))
# plt.show()
