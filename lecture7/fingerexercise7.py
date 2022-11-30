def sumDigits(s):
    """Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""

    numbers = []
    total = 0
    try:
        for char in s:
            if char.isnumeric():
                numbers.append(int(char))

        for i in numbers:
            total = total + i
    except TypeError:
        return "Type Error - Not a string"

    return total


print(sumDigits("123"))
