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