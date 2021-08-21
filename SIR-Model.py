 from matplotlib import pyplot as plt
susceptible_list = [99]
infected_list = [1]
recoverd_list = [0]

b = 2.5*y/100
y =  1/14
h = 0.001

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

for i in range(100000):
    susceptible_n_plus_1(susceptible_list, infected_list, b, i,h)
    infected_n_plus_1(susceptible_list, infected_list, b, y, i, h)
    recoverd_n_plus_1(infected_list, y, i, h, recoverd_list)
plt.plot(susceptible_list)
plt.plot(infected_list)
plt.plot(recoverd_list)
print(susceptible_list[len(susceptible_list)-1])
print(infected_list[len(infected_list )-1])
print(recoverd_list[len(recoverd_list)-1])



