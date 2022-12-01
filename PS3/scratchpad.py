
hand = {'a':1, 'x':2, 'l':3, 'e':1}


for letter in hand.keys():
    for j in range(hand[letter]):
        print(letter, end=' ')  # print all on the same line
print()  # print an empty line
