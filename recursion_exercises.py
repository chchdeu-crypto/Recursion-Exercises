#mission 1
def power(base,exponent):
    if exponent<=0:
        return 1
    return base*power(base,exponent-1)
    
print(power(2,4))

#mission 2
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(5))

#mission 3
def numbers_to_n(n):
    if n<1:
        return []
    
    return numbers_to_n(n-1)+[n]
print(numbers_to_n(5))
