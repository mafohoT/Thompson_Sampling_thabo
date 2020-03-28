import numpy as np
import matplotlib.pyplot as plt
import random

#selecting the parameters
N = 2000000
d = 9


#creating the simultion
conversion_rates = [0.03,0.13,0.09,0.16,0.11,0.04,0.20,0.08,0.01]

X = np.array(np.zeros([N,d]))
for i in range(N):
    for j in range(d):
        if np.random.rand() <= conversion_rates[j]:
           X[i,j]=1
        
# implementing a Random strategy and Thompson Sampling
strategies_selected_rs = []   
strategies_selected_ts = []  
total_reward_rs = 0
total_reward_ts = 0       
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d  
for n in range(0, N):
    #random strategy 
    strategy_rs = random.randrange(d)
    strategies_selected_rs.append(strategy_rs)
    reward_rs = X[n, strategy_rs]
    total_reward_rs = total_reward_rs + reward_rs
   
    
    #Thompson Strategy
    strategy_ts=0
    MAX_random = 0
    for i in range(0, d):
        random_beta = random.betavariate(numbers_of_rewards_1[i] + 1,numbers_of_rewards_0[i]+1)
        if random_beta > MAX_random:
            MAX_random = random_beta
            strategy_ts = i
    rewards_ts = X[n, strategy_ts]
    if rewards_ts == 1:
        numbers_of_rewards_1[strategy_ts] = numbers_of_rewards_1[strategy_ts] + 1
    else:
        numbers_of_rewards_0[strategy_ts] = numbers_of_rewards_0[strategy_ts] + 1
    strategies_selected_ts.append(strategy_ts)
    total_reward_ts = total_reward_ts + rewards_ts

#Computing the Absolute relating return
absolute_return = (total_reward_ts - total_reward_rs) * 100
relative_return =  (total_reward_ts - total_reward_rs) / total_reward_rs * 100
print("Absolute Return: {:.0f} R".format(absolute_return))
print("Relative Return: {:.0f} R".format(relative_return))
#plotting the Histogram of the selections
plt.hist(strategies_selected_ts)
plt.title('Histogtam of selections')
plt.xlabel('Strategy')
plt.ylabel('Number of times strategy was selected')
plt.show()



    
    
    
    