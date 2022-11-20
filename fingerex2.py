# Finger exercise: Write a program that asks the user to input 10 integers, and then
# prints the largest odd number that was entered. If no odd number was entered, it
# should print a message to that effect.

total = 10
numberlist = []
while total != 0:
    print(f"{total} times to go")
    number = int(input("Give me a number "))
    if number % 2 == 1:
        numberlist.append(number)
    total -= 1

if not numberlist:
    print("There are no odd numbers in the list")
else:
    numberlist = sorted(numberlist)
    print("The highest odd number is " + str(numberlist[-1]))




