

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

# A function to convert letters to alphabetical position
def position(chara):
    return ord(chara)-96