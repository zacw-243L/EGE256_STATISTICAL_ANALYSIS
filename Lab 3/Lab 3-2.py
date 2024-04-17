import time
import random
import matplotlib.pyplot as plt

start_time = time.time()
random.seed(7)
total_trials = 1000
total = 0
count_not_6 = 0
P_E_complement = []
for trial in range(total_trials):
    dice = random.randint(1, 6)
    if not dice == 6:
        count_not_6 += 1
    P_E_complement.append(count_not_6 / (trial + 1))

# plot graph of fraction of not-6's against number of rolls
ax = plt.gca()
ax.set_xlim([0, total_trials])
ax.set_ylim([0, 1])
plt.title("Graph of Fraction of not-6's against Number of Rolls")
plt.xlabel("Number of Rolls")
plt.ylabel("Fraction of not-6's")
plt.plot(range(total_trials), P_E_complement)
print("P(E complement) =", P_E_complement[-1])
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
