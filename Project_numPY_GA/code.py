# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path, delimiter = ',', skip_header = 1) 
print (data)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census = np.concatenate((data, new_record), axis = 0)
#Code starts here



# --------------
#Code starts here
age = census[:,0]
max_age = np.max(age)
min_age = np.min(age)

mean = lambda x: np.sum(x) / len(x)

age_mean = mean(age)
print (age_mean)
def sd (x, x_mean):
    for element in x:
        diff = x - x_mean
        sum_squares = np.sum(diff ** 2)
        div = sum_squares / len(x)
        stdev = np.sqrt(div)
    return stdev

age_std = sd(age, age_mean)
print (age_std)


# --------------
#Code starts here
race = census[:, 2]

race_0 = census[race == 0]
race_1 = census[race == 1]
race_2 = census[race == 2]
race_3 = census[race == 3]
race_4 = census[race == 4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

arr = np.array([len_0, len_1, len_2, len_3, len_4])
rarr = np.array([race_0,race_1,race_2,race_3,race_4])
mini = np.min(arr)

def fi(x, value):
    n = 0
    for element in x:
        if value != element:
            n = n+1
        else:
            break
    return n
index = fi(arr, mini)
minority_race = index
print(minority_race)


# --------------
#Code starts here
senior_citizens = census[census[:,0] > 60]
working_hours_sum = np.sum(senior_citizens[:, 6])
senior_citizens_len = len(senior_citizens)

avg_working_hours = working_hours_sum / senior_citizens_len

print (avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1] > 10]
low = census[census[:,1] <= 10]

pay_high = high[:, 7]
pay_low = low[:, 7]

avg_pay_high = np.sum(pay_high)/len(pay_high)
avg_pay_low = np.sum(pay_low)/len(pay_low)
print (avg_pay_high, avg_pay_low)


