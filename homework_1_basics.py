# Create a python script:
#
# create list of 100 random numbers from 0 to 1000

# Import the random module to generate random numbers
import random as r
# initialize the list
f_list = []
# create a for loop to generate random numbers and append to the list
for i in range(10):
# for i in range(100):
    random_number = r.randint(0,1000)
    f_list.append(random_number)

# print the final list:
print(f_list)
###################################
# sort list from min to max(without using sort()):
# Bubble sort:
n = len(f_list)
# iterate each element from the list:
for i in range(n):
    for j in range(0,n-i-1):
        if f_list[j] > f_list[j+1]:
            f_list[j],f_list[j+1] = f_list[j+1], f_list[j]
print(f_list)

# calculate average for even and odd numbers
# initialize the variables
count_e = 0
count_o = 0
sum_e = 0
sum_o = 0
for i in f_list:
    if i%2 == 0:
        count_e = count_e+1
        sum_e = sum_e + i
    else:
        count_o = count_o + 1
        sum_o = sum_o + i
avg_e = sum_e/count_e
avg_o = sum_o/count_o

# print both average result in console
print(avg_e, avg_o)
# Each line of code should be commented with description.
#
# Commit script to git repository and provide link as home task result.
