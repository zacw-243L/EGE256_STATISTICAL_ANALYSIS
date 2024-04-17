import time
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

B = float(input("Enter number: "))
start_time = time.time()

rv_normal = norm(0, B)
x = np.arange(-15, 15, 0.01)
plt.figure()
plt.plot(x, rv_normal.pdf(x))
plt.title(f"Probability Density Function (PDF) of X~N( 0, {B} )")
plt.xlabel('x')
plt.ylabel('f(x)')
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
