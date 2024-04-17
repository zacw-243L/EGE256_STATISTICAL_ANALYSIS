import time
from matplotlib import pyplot as plt

start_time = time.time()
P_unique = 1
P_list = []

for i in range(60):
    P_unique *= (365 - i) / 365
    P_list.append(1 - P_unique)

for i in range(60):
    if P_list[i] >= 0.5:
        print(i + 1)
        print(P_list[i])
        break

plt.xlabel("Number of people")
plt.ylabel("Probability")
plt.title("Graph of Probability of at least two people having the same birthday")
plt.plot(P_list)
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
