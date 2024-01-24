# using normal function
def fact(x):
    result = 1
    if x == 0:
        return 1
    else:
        for i in range(x):
            result = result * (i+1)

        return result

print(fact(1))

# using recursion

def factorial(a):
    if a == 0:
        return 1

    return a* factorial(a-1)

print(factorial(5))
