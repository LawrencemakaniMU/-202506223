def factorial(n):
    result = 1 #Starting value
    for i in range(1, n + 1): 
        result = result * i #multiply each number
    return result
print(factorial(5))
#Starting Fibonacci Code
def fibonacci(j):
    a, b = 0, 1 #Starting Values
    for i in range(j):
        print(a) #Show current number
        a, b = b, a + b #Update
fibonacci(10)
