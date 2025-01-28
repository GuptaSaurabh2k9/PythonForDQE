# Write a code, which will:

# 1. create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example:[{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

import random as r

# 1: Generate a random number

num_dict = r.randint(2,10)
print('number of dict',num_dict)
fnl_dict_list = []

# 2: create a loop to generate dic till random number

for i in range(num_dict):
    #2.1 generate a random number that defines how may of keys should be present in each
    num_key = r.randint(1, 26)
    # print('number of keys:',num_key)
    random_dict = {}
    for i in range(num_key):
        # 3: generate keys for each dict in range a-z
        random_key = chr(97+r.randint(0,25))
        # 4: generate values for each dict in range 1-100
        random_value = r.randint(0, 100)
        random_dict[random_key] = random_value

    # 5: append the dic to the final list
    fnl_dict_list.append(random_dict)
print('step1',fnl_dict_list)

# 2. get previously generated list of dicts and create one common dict:
#
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example:{'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# Each line of code should be commented with description.
#
# Commit script to git repository and provide link as home task result.

# created an empty dict
f_dict = {}

#loop thru each key of each dict

for i in range(len(fnl_dict_list)):
    # print(i)
    # print('final:',fnl_dict_list[i])

    for k,v in fnl_dict_list[i].items():
        # print(k, v)
        # do the comparison for each key values and update the values in the form of key value
        if k in f_dict:
            # print(k,v)
            if v > f_dict[k][1]:
                f_dict[k]= (f"{k}_{i+1}",v)
        else:
            f_dict[k] = (k, v)
        # print(f_dict[k])

# print(f_dict)

# from the final dict pick the values only and create a new dict
final_dict = {}

for v in f_dict.values():
    final_dict[v[0]] = v[1]

print(final_dict)


