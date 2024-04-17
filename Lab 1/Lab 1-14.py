import time
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

start_time = time.time()
titanic = pd.read_csv('titanic.csv')

print(titanic['age'].value_counts())
print('mode of age = %d' % titanic['age'].mode())
print("--- %s seconds ---" % (time.time() - start_time))
