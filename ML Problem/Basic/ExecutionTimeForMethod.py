import time
number = int(input("Enter a Number to Find Factorial"))
start_time = time.time()
def factorial(number):
    fact = 1
    for counter in range(2, number+1):
        fact *= counter
    return fact
print(factorial(number))
stop_time = time.time()
print(stop_time - start_time)