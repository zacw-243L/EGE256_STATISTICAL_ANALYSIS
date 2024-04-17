import time
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

start_time = time.time()
titanic = pd.read_csv('titanic.csv')
# titanic = sns.load_dataset('titanic')

my_tab = pd.crosstab(index=titanic["pclass"], columns="count")

print(my_tab)
print("--- %s seconds ---" % (time.time() - start_time))
