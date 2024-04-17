import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

start_time = time.time()
norm_data = pd.DataFrame(np.random.normal(size=100000))
norm_data.plot(kind="density", legend=False)
# plot black line at mean
plt.vlines(norm_data.mean(), ymin=0, ymax=0.4, linewidth=3, color="black")
# plot red line at median
plt.vlines(norm_data.median(), ymin=0, ymax=0.4, linewidth=3, color="red")
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
