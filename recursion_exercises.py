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

#mission 4
def count_items(lst):
    if lst==[]:
        return 0
    lst.pop(0)
    num_len=1
    return num_len+count_items(lst)
print(count_items(["a","b","c"]))

#mission 5
def count_evens(numbers):
    if numbers==[]:
        return 0
    current=numbers.pop(0)
    if current%2==0:
        count=1
        return count +count_evens(numbers)
    else:
        count=0
        
    return count +count_evens(numbers)
print(count_evens([4,7,10,3,8]))

#mission 6
def max_number(numbers):
    if len(numbers)==1:
        return numbers[0]
    first_num=numbers.pop(0)
    max_of_rest=max_number(numbers)
    if first_num>max_of_rest:
        return first_num
    else:
        return max_of_rest
print(max_number([4,9,2,11,6]))




