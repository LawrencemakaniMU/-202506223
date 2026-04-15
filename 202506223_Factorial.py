def factorial(n):
    result = 1 #Starting value
    for i in range(1, n + 1): 
        result = result * i #multiply each number
    return result
print(factorial(5))
