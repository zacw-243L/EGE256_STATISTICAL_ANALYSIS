import time
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

start_time = time.time()
titanic = pd.read_csv('titanic.csv')
# titanic = sns.load_dataset('titanic')

# print(titanic.shape)
# print(titanic.columns)

print(titanic.head())
print("--- %s seconds ---" % (time.time() - start_time))
