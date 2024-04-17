import time
import random
from matplotlib import pyplot as plt

start_time = time.time()
a = 7
b = 8  # experiment around with random seed
c = 10
random.seed(a)
total_trials = 500000
total_trials1 = 900000  # samething for trials
total = 0
count_6 = 0
P_E = []
for trial in range(total_trials):
    dice = random.randint(1, 6)
    if dice == 6:
        count_6 += 1
    P_E.append(count_6 / (trial + 1))

ax = plt.gca()
ax.set_xlim([0, total_trials])
ax.set_ylim([0, 1])
plt.title("Graph of Fraction of 6's against Number of Rolls")
plt.xlabel('Number of Rolls')
plt.ylabel("Fraction of 6's")
plt.plot(range(total_trials), P_E)
print("P(E) =", P_E[-1])
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
