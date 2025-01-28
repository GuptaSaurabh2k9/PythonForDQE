# 1. create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),

# 2. get previously generated list of dicts and create one common dict:
#
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example:{'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# Each line of code should be commented with description.
#
# Commit script to git repository and provide link as home task result.

import random as r

def generate_random_number():
    number_dict = r.randint(2,10)
    dic_list = []

    for i in range(number_dict):
        num_keys = r.randint(0,25)
        rand_dict = {chr(97+r.randint(0,25)):r.randint(0,100) for key in range(num_keys)}
        dic_list.append(rand_dict)
    return dic_list

def merge_dic(dict_list):
    m_dict = {}
    for i in range(len(dict_list)):
        for k,v in dict_list[i].items():
            if k in m_dict:
                if v > m_dict[k][1]:
                    m_dict[k] = (f"{k}_{i+1}",v)
            else:
                m_dict[k] = (k,v)
    fnl_dict = {val[0]:val[1] for val in m_dict.values()}
    return fnl_dict

random_dict = generate_random_number()
# print('random_dict:',random_dict)
f_dict = merge_dic(random_dict)
print('f_dict',f_dict)

import re

def pick_last_word(txt):
    sen = re.split(r'[.\n]\s*', txt)
    fnl_sen = [line.split()[-1] for line in sen if line]
    last_sen = ' '.join(fnl_sen)
    return sen,last_sen

def normalize_txt(txt1):
    norm_txt = txt1.lower()
    # Replace 'iz' with 'is'
    corr_text = re.sub(r'\biz\b', 'is', norm_txt)
    sen,last_sen = pick_last_word(corr_text)
    final_txt = ' '.join(sen) + ' ' + last_sen + '.'
    return final_txt

def count_whitespace(txt):
    # Count all whitespace characters
    return len(re.findall(r'\s', txt))  # This counts all types of whitespace

input_str = """homEwork:
 tHis iz your homeWork, copy these Text to variable.

 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

x = normalize_txt(input_str)
print('final_txt:',x)

whitespace_count = count_whitespace(x)
print(f"Number of whitespace characters: {whitespace_count}")