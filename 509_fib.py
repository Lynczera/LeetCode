'''
Dynamic programming 
don't call recursion -> multiple unnecessary computations 

create and array and calculate based on the previous values
'''




def fib(n):
    if n==0: return 0
    if n==1: return 1
    
    fib_arr = [None]*(n+1)
    fib_arr[0] = 0
    fib_arr[1] = 1

    for i in range(2,n+1):
        fib_arr[i] = fib_arr[i-1] + fib_arr[i-2]

    return fib_arr[-1]




print(fib(5))

