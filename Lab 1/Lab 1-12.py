import time
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

start_time = time.time()
titanic = pd.read_csv('titanic.csv')

women = titanic[titanic['sex'] == 'female']
sns.displot(women[women['survived'] == 1].age, bins=18, label='survived')
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
