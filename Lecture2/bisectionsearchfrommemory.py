x = int(input("enter a number "))

epsilon = 0.1
high = max(1.0, x)
low = 0.0
guess = (high + low) / 2.0

while abs(guess ** 2 - x) >= epsilon:
    if guess ** 2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2

print(f"{guess} is the square root of {x}")

