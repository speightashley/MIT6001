def findAnEven(L: list):
    """Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number"""

    for number in L:
        if number % 2 == 0:
            return number
    raise ValueError("Not a list")


test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test2 = [1, 3, 5, 7, 9]
# test2 = 123456
print(findAnEven(test))
print(findAnEven(test2))
