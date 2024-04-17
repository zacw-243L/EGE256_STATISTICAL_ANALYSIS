import time
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

start_time = time.time()
titanic = pd.read_csv('titanic.csv')
# titanic = sns.load_dataset('titanic')

my_tab = pd.crosstab(index=titanic["deck"], columns="count")

print(my_tab)
print(my_tab.sum())
print(my_tab/my_tab.sum())
print("--- %s seconds ---" % (time.time() - start_time))
