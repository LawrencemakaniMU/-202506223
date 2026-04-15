def fibonacci(j):
    a, b = 0, 1 #Starting Values
    for i in range(j):
        print(a) #Show current number
        a, b = b, a + b #Update
fibonacci(10)
