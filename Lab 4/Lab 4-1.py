import time
import random

start_time = time.time()
random.seed(7)
total_trials = 1000
count_B = 0
count_AgivenB = 0
count_AandB = 0
omega = [1, 2, 3, 4, 5, 6]
A = [6]
B = [2, 4, 6]
for trial in range(total_trials):
    outcome = random.choice(omega)
    if outcome in B:
        count_B += 1
        if outcome in A:
            count_AgivenB += 1
    if outcome in A and outcome in B:
        count_AandB += 1

P_B = count_B / total_trials
P_AgivenB = count_AgivenB / count_B
P_AandB = count_AandB / total_trials
print("P(B) = %0.3f" % P_B)
print("P(A|B) = %0.3f" % P_AgivenB)
print("P(A and B) = %0.3f" % P_AandB)
print("P( A and B ) / P( B ) = %0.3f" % (P_AandB / P_B))
print("--- %s seconds ---" % (time.time() - start_time))
