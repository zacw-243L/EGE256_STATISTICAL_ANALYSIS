import time
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

start_time = time.time()
titanic = pd.read_csv('titanic.csv')

survived_sex = pd.crosstab(index=titanic["survived"], columns=titanic["sex"])
survived_sex.index = ["died", "survived"]

print(survived_sex)
print("--- %s seconds ---" % (time.time() - start_time))
 