frame = 0


def fib(n):
    global frame
    frame += 1
    if n == 0 or n == 1:
        #print(f"frame = {frame}")
        return 1
    else:
        #print(f"frame = {frame}")
        return fib(n - 1) + fib(n - 2)


print(fib(5))
print(frame)

