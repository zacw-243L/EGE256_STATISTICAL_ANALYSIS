import time
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

start_time = time.time()
titanic = pd.read_csv('titanic.csv')

survived_class = pd.crosstab(index=titanic["survived"], columns=titanic["pclass"])
survived_class.columns = ["class1", "class2", "class3"]
survived_class.index = ["died", "survived"]

print(survived_class)
print("--- %s seconds ---" % (time.time() - start_time))
