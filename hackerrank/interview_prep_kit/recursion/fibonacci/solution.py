
fibonacci_numbers = dict()

def fibonacci(n):

    # Write your code here.
    if n < 2:
        return n
    
    if n in fibonacci_numbers:
        return fibonacci_numbers[n] 
    
    result = fibonacci(n - 1) + fibonacci(n - 2)
    fibonacci_numbers[n] = result
    return result