'''
There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. 
Count the number of ways, the person can reach the top.
recurrence is:
ways(n) = ways(n-1) + ways(n-2)
'''

def fib(n):
    f = [0]*(n+1)

    f[1] = 1
    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

n = 4
ways = fib(n+1)
print ways



    