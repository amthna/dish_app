# Python3 code to demonstrate working of
# Most frequent word in Strings List
# Using loop + max() + split() + defaultdict()
from collections import defaultdict
import re


def token_counter(text):
    list = text
    temp = defaultdict(int)
    for sub in list:
        for wrd in sub.split():
            wrd = wrd.lower()
            hyphen = re.search(r'-', wrd)
            if hyphen:
                continue
            else:
                temp[wrd] += 1
    # getting max frequency
    # res = max(temp, key=temp.get)

    # printing result
    return temp