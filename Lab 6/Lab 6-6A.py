import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import time

start_time = time.time()

i = 0
while i < 100:
    rv_normal = norm(3.0, 5.0)
    x = rv_normal.rvs(1000)
    print('mean =', np.mean(x))
    print('standard deviation =', np.std(x))
    i += 1

print("--- %s seconds ---" % (time.time() - start_time))
