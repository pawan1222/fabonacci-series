import math

# A function to return true if x is a perfect square
def isperfectsquare(x):
    s=int(math.sqrt(x))
    return s*s == x
# Return true if n is a Fibonacci number, else false
def isFibonacci(n):
    return isperfectsquare(5*n*n + 4) or isperfectsquare(5*n*n - 4) 

# Takes input from the user and store in a list(l1)
l1=[int(i) for i in input("Enter the number or numbers: ").split(",")]

for i in l1:
    if (isFibonacci(i)== True):
        print(i, "is a valid Fibonacci number")
    else:
        print(i, "is not a valid Fibonacci number")    