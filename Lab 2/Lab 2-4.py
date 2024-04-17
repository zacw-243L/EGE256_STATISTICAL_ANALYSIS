import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

start_time = time.time()
norm_data = np.random.normal(size=50)
outliers = np.random.normal(15, size=3)
combined_data = pd.DataFrame(np.concatenate((norm_data, outliers), axis=0))
combined_data.plot(kind="density", xlim=(-5, 20))
plt.vlines(combined_data.mean(), ymin=0, ymax=0.2, linewidth=3, color="black")
plt.vlines(combined_data.median(), ymin=0, ymax=0.2, linewidth=3, color="red")
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
