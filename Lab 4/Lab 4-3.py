import time
import random
from random import choice

start_time = time.time()
random.seed(123)
num_games = 1000000
stay_wins = 0
switch_wins = 0
doors = [ 'A', 'B', 'C' ]
for _ in range(num_games):
    prize_door = choice(doors)
    chosen_door = choice(doors)
    opened_door = choice(list(set(doors) - set([prize_door, chosen_door])))
    switch_door = (set(doors) - set([ chosen_door, opened_door ])).pop()
    if chosen_door == prize_door:
        stay_wins += 1
    if switch_door == prize_door:
        switch_wins += 1

print('Probability of winning with a stay strategy = %0.3f' %(stay_wins / num_games))
print('Probability of winning with a switch strategy = %0.3f' % (switch_wins / num_games))
print("--- %s seconds ---" % (time.time() - start_time))