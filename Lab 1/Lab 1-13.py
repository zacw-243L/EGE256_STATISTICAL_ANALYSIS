import time
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

start_time = time.time()
titanic = pd.read_csv('titanic.csv')

print('mean fare = $%0.2f' % titanic['fare'].mean())
print('median fare = $%0.2f' % titanic['fare'].median())
print("--- %s seconds ---" % (time.time() - start_time))
