# Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
k = 24.0
guess = k / 2.0
count = 0
while abs(guess * guess - k) >= epsilon:
    guess = guess - (((guess ** 2) - k) / (2 * guess))
    count = count + 1
print('Square root of', k, 'is about', guess)
print(f"count is {count}")
