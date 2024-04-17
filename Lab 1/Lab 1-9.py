import time
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

start_time = time.time()
titanic = pd.read_csv('titanic.csv')

# table of survival vs passenger class
survived_class = pd.crosstab(index=titanic["survived"], columns=titanic["pclass"], margins=True)
survived_class.columns = ["class1", "class2", "class3", "row total"]
survived_class.index = ["died", "survived", "col total"]

print(survived_class)
print(survived_class / survived_class.loc["col total", "row total"])
print(survived_class / survived_class.loc["col total"])
print(survived_class.div(survived_class["row total"], axis=0))

print("--- %s seconds ---" % (time.time() - start_time))
