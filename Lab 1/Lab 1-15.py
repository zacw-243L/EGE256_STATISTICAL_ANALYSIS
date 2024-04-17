import time
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

start_time = time.time()
titanic = pd.read_csv('titanic.csv')

titanic.boxplot(column=['age'], by="class")
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
