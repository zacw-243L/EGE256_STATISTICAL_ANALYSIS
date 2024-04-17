import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

start_time = time.time()
skewed_data = pd.DataFrame(np.random.exponential(size=100000))
skewed_data.plot(kind="density", xlim=(-1, 5), legend=False)
# plot black line at mean
plt.vlines(skewed_data.mean(), ymin=0, ymax=0.8, linewidth=3, color="black")
# plot red line at median
plt.vlines(skewed_data.median(), ymin=0, ymax=0.8, linewidth=3, color="red")
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
