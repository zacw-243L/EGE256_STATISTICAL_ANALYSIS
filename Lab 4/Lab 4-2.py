import time
import random

start_time = time.time()
random.seed(123)
cabs = ['green'] * 85 + ['blue'] * 15
sawGcab_and_Gcab = 0
sawBcab_and_Bcab = 0
sawBcab_and_Gcab = 0
sawGcab_and_Bcab = 0

total_trials = 5000000
for _ in range(total_trials):
    # randomly choose a cab
    cab = random.choice(cabs)
    # witness correctly identifies cab 80% of the time
    if random.random() > 0.2:
        # 80% of the time, colour of the cab is identified correctly
        if cab == 'green':
            sawGcab_and_Gcab += 1
        if cab == 'blue':
            sawBcab_and_Bcab += 1
    else:
        # 20% of the time, colour of the cab is identified wrongly
        if cab == 'green':
            sawBcab_and_Gcab += 1
        if cab == 'blue':
            sawGcab_and_Bcab += 1
print("P( saw blue cab | blue cab )P( blue cab ) = %0.3f" % (sawBcab_and_Bcab / total_trials))
print("P( saw green cab | green cab )P( green cab ) = %0.3f" % (sawGcab_and_Gcab / total_trials))
print("P( saw green cab | blue cab )P( blue cab ) = %0.3f" % (sawGcab_and_Bcab / total_trials))
print("P( saw blue cab | green cab )P( green cab ) = %0.3f" % (sawBcab_and_Gcab / total_trials))
print("P( blue cab | saw blue cab ) = %0.3f" % (sawBcab_and_Bcab / (sawBcab_and_Bcab + sawBcab_and_Gcab)))
print("--- %s seconds ---" % (time.time() - start_time))

