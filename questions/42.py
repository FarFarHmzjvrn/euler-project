

# A list of triangular numbers
num_list = []
a = 1
while a <= 100:
    num = (a)*(a+1)*(1/2)
    a += 1
    num = int(num)
    num_list.append(num)

def position(chara):
    """A function to convert 
    letters to alphabetical position"""
    return ord(chara)-96

# open the file words.txt
with open('p042_words.txt','r+') as f:
    # split the lines into a list
    for line in f:
        line = line.lower().strip().split(',')
        Counter = 0
        # for loop to loop through the line
        for word in line:
            # convert the words to numbers and find the sum
            com = sum(map(position,word[1:-1]))
            # check if the given number is in num_list
            if com in num_list:
                Counter += 1
print(Counter)


# I have used open to do file operations. I am assuming that you know all the file operations.
# Function position will convert the given letter to a alphabetical position of the number.
# For example position('A') will return 1, position('S') will return 19 and so on.
# We will loop through the words and map each and every word to position function.
# This will return a list with the word converted to their alphabetical positions.
# Finally sum function will find the sum of the numbers in the list.
# i.e. we are simply finding the word value in this statement at line 36. For example map(position,'SKY') will return 55 and so on.

