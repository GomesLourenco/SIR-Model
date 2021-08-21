from matplotlib import pyplot as plt

import pandas as pd
biweekly_cases = pd.read_csv('biweekly_cases.csv') 

df = pd.DataFrame(biweekly_cases)
col_one_list = df['Portugal'].tolist()
col_one_list = col_one_list[340:]
print(col_one_list)

susceptible_list = [10280000]
infected_list = [45829]
recoverd_list = [0]

y = 14/10.5
b = 1.18*y/10280000
h = 1

def susceptible_n_plus_1(susceptible_list, infected_list, b,current_time,h):
    value = -b*susceptible_list[current_time-1]*infected_list[current_time-1]*h + susceptible_list[current_time - 1]
    susceptible_list.append(value)
    return susceptible_list
def infected_n_plus_1(susceptible_list, infected_list, b,y,current_time,h):
    value = (b*susceptible_list[current_time-1]*infected_list[current_time-1] - y*infected_list[current_time-1])*h  + infected_list[current_time -1]
    infected_list.append(value)
    return infected_list
def recoverd_n_plus_1(infected_list, y, current_time, h,recoverd_list):
    value =  y*infected_list[current_time-1]*h + recoverd_list[current_time -1]
    recoverd_list.append(value)
    return recoverd_list

for i in range(459):
    susceptible_n_plus_1(susceptible_list, infected_list, b, i,h)
    infected_n_plus_1(susceptible_list, infected_list, b, y, i, h)
    recoverd_n_plus_1(infected_list, y, i, h, recoverd_list)
    
plt.plot(col_one_list, label = 'Actual')
#plt.plot(susceptible_list)
plt.plot(infected_list, label = 'Predicted')
#plt.plot(recoverd_list)
plt.xlabel("Biweekly")
plt.ylabel("Cases")
plt.title("Biweekly Cases in Portugal, Actual and Predicted")
plt.xlim([0, 200])
leg = plt.legend(loc='upper right')
print(susceptible_list[len(susceptible_list)-1])
print(infected_list[len(infected_list )-1])
print(recoverd_list[len(recoverd_list)-1])
