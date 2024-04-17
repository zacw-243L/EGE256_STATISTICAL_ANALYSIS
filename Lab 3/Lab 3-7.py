import time
import random
import matplotlib.pyplot as plt


def compute_probability(num_people):
    num_trials = 1000
    same_birthday = 0
    for trial in range(num_trials):
        day = [0] * 365
        for i in range(num_people):
            birthday = random.randint(0, 364)
            if day[birthday] == 0:
                day[birthday] = 1
            else:
                same_birthday += 1
                break
    return same_birthday / num_trials


start_time = time.time()
random.seed(3)
probability = [compute_probability(num_people) for num_people in range(1, 60)]
print(probability)
plt.plot(probability)
plt.title("Graph of probability of at least two people having the same birthdays")
plt.xlabel("Number of people")
plt.ylabel("Probability")
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()
