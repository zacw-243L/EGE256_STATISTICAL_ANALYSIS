import time
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

start_time = time.time()
titanic = pd.read_csv('titanic.csv')

sns.barplot(x='pclass', y='survived', data=titanic)
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()

