def fibonacci(n):
    if n==1 or n==0:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

result = fibonacci(2)
print(result)

def fibonacci_memoization(n,d):
    if n in d:
        return d[n]
    else:
        d[n] =fibonacci_memoization((n-1),d)+fibonacci_memoization((n-2),d)
        return d[n]
d={0:1,1:1}
memoization_result = fibonacci_memoization(4,d)
print(memoization_result)
