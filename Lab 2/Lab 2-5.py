import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

start_time = time.time()
norm_data = np.random.normal(size=100000)
skewed_data = np.concatenate((np.random.normal(size=35000) + 2, np.random.exponential(size=65000)), axis=0)
uniform_data = np.random.uniform(0, 2, size=100000)
peaked_data = np.concatenate((np.random.exponential(size=50000), -np.random.exponential(size=50000)), axis=0)
data_df = pd.DataFrame({"norm": norm_data, "skewed": skewed_data, "uniform": uniform_data, "peaked": peaked_data})
data_df.plot(kind="density", figsize=(10, 10), xlim=(-5, 5))
print(data_df.skew())
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
