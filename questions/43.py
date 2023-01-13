
# create a function to get mod
def subdiv(num, n):
    return num % n == 0

#Using permutation for different combinations of these numbers
# 0,1,2,3,4,5,6,7,8,9
from itertools import permutations
x = permutations('0123456789')



#variable to store the value of sum
total = 0
#for loop to loop through permutations
for num in x:
    if (subdiv(int(''.join(num[7:10])), 17)and
       subdiv(int(''.join(num[6:9])), 13)and
       subdiv(int(''.join(num[5:8])), 11)and
       subdiv(int(''.join(num[4:7])), 7)and
       subdiv(int(''.join(num[3:6])), 5)and
       subdiv(int(''.join(num[2:5])), 3)and
       subdiv(int(''.join(num[1:4])), 2)):
        total += int(''.join(num))



total