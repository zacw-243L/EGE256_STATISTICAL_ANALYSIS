import time
import random

start_time = time.time()
random.seed(7)
total_trials = 1000
count_A = 0
count_B = 0
count_A_and_B = 0
for trial in range(total_trials):
    dice1 = random.randint(1, 6)
    if dice1 == 6:
        count_A += 1
    dice2 = random.randint(1, 6)
    if dice2 == 1:
        count_B += 1
    if dice1 == 6 and dice2 == 1:
        count_A_and_B += 1
P_A = count_A / total_trials
P_B = count_B / total_trials
P_A_intersect_B = count_A_and_B / total_trials
print("P(A) =", P_A)
print("P(B) =", P_B)
print("P(A intersect B) =", P_A_intersect_B)
print("P(A)P(B) =", P_A * P_B)
print("--- %s seconds ---" % (time.time() - start_time))
