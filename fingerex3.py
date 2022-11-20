#  Finger exercise: Let s be a string that contains a sequence of decimal numbers
# separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints the
# sum of the numbers in s.

s = '1.23,2.4,3.123'


segmented = s.split(',')  # split the string into list elements

convertedlist = []

# convert from string to float
for num in segmented:
    num = float(num)
    convertedlist.append(num)

# total the numbers
total = 0
for num in convertedlist:
    total += num

print(total)
