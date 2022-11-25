def f(x):
    def g():
        x = "abc"
        print(f"X = {x}")

    def h():
        z = x
        print(f"z = {z}")

    x = x + 1
    print(f"x = {x}")
    h()
    g()
    print(f"x = {x}")
    return g


x = 3
z = f(x)
print(f"x = {x}")
print(f"z = {z}")
z()
