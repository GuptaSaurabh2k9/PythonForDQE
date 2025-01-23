
import re

# Original text
text = """homEwork:
 tHis iz your homeWork, copy these Text to variable.

 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# Normalize the text to lowercase
norm_txt = text.lower()
# print(norm_txt)

# Replace 'iz' with 'is'
corr_text = re.sub(r'\biz\b', 'is', norm_txt)

# Create a sentence with the last words of each existing sentence
sen = re.split(r'[.\n]\s*', corr_text)
# print(sen)
last_word = []
for s in sen:
    if s:
        last_word = last_word + [s.split()[-1]]
        # print(last_word,type(last_word))
# print(last_word)
last_sen = ' '.join(last_word)
# print(last_sen, type(last_sen))
final_txt = ' '.join(sen) + ' ' + last_sen + '.'
print(final_txt)

# Count whitespace characters

space_cnt = len(re.findall(r'\s', final_txt))
print(space_cnt)
