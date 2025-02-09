def fibonacci(n):
    if n == 0:
        return "Invelid input"
    if n == 1:
        return 0
    if n == 2:
        return [0,1]
    
    a,b = 0,1
    fib_sequence = [0,1]
    for _ in range(n-2):
        a,b = b, a+b
        fib_sequence.append(b)

    return fib_sequence   
    
n = int(input())
print(fibonacci(n))    

