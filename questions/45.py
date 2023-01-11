def Triangle(resault):
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
