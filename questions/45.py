def Triangle(resault:int)-> int:
    """The check that asked a number,
    which number is in the sequence of triangular numbers
    """
    n = 1
    while True:
        if (n)*(n+1)*(0.5) == resault:
            return n
        n += 1

Triangle(40755)
285

def Pentagonal(P:int)-> bool:
    """check number is Pentagonal 
    """
    if ((((24)*(P)+1)**0.5)+1)% 6 == 0:
        return True
    return False


def Hexagonal(H:int)-> int:
    """check number is Hexagonal
    """
    if ((((8)*(H)+1)**0.5)+1) % 4 == 0:
        return True
    return False


"So start after 285"
i = 286
while True:
    Triangle = (i)*(i+1)*(1/2)
    if Hexagonal(Triangle) and Pentagonal(Triangle):
        print(Triangle)
        break
    i += 1



#I first checked the number 40755 that came in the question form,
#  which number is the number in the sequence of triangular numbers,
#  the number I found while loop starts after the number 285,
#  we use two functions to find pentagonal and hexagonal numbers,
#  until now we use while loop We will find the first number
#  after 285 which is triangle and is both hexagone and pentagone