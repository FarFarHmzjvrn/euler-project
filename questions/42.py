

# A list of triangular numbers
num_list = []
a = 1
while a <= 100:
    num = (a)*(a+1)*(1/2)
    a += 1
    num = int(num)
    num_list.append(num)

# from collections import Counter
from collections import Counter

def position(chara):
    """A function to convert 
    letters to alphabetical position"""
    return ord(chara)-96