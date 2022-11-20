from numpy import log

x = int(input("Give me a number "))
y = int(input("Give me another number "))

raised = (x ** y)  
logged = log(raised)

print(f"{x} raised to the power of {y} is {raised}. \nThe logarithm of {raised} is {logged}")

