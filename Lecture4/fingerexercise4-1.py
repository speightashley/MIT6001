def isIn(string1, string2):
    if string1 in string2 or string2 in string1:
        return True
    else:
        return False


x = "This is string one"
y = "is"
z = "the"

print(isIn(y, x))
