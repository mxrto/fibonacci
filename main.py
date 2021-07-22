def fibonacci(x, y, z):
    fib_list = []

    if x == 1:
        fib_list.append(x)

    while z < 255:
        fib_list.append(z)
        z = x + y
        x = y
        y = z

    return fib_list

 

numbers = fibonacci(1, 1, 1)
print(numbers)