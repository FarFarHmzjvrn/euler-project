

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

# open the file words.txt
with open('p042_words.txt','r+') as f:
    # split the lines into a list
    for line in f:
        line = line.lower().strip().split(',')
        # for loop to loop through the line
        for word in line:
            com = sum(map(position,word[1:-1]))
