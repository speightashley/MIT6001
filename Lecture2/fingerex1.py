# Finger exercise: Write a program that examines three variables—x, y, and z—and
# prints the largest odd number among them. If none of them are odd, it should
# print a message to that effect.

numlist = []

x = int(input("Enter a number "))
y = int(input("Enter another number "))
z = int(input("And the last one "))

numlist.append(x)
numlist.append(y)
numlist.append(z)

sortedlist = []

for i in numlist:
    if i % 2 == 1:
        sortedlist.append(i)

sortedlist = sorted(sortedlist)
if not sortedlist:
    print("No odd numbers")
else:
    print(sortedlist[-1])
