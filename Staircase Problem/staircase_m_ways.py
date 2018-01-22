'''
Generalization of the above problem
How to count number of ways if the person can climb up to m stairs for a given value m? 
For example if m is 4, the person can climb 1 stair or 2 stairs or 3 stairs or 4 stairs at a time.
recurrence is:
ways(n, m) = ways(n-1, m) + ways(n-2, m) + ... ways(n-m, m)
'''
def countways(n,m):
    if n <= 1:
        return n
    res = 0
    i = 1
    while i <=m and i<=n:
        res += countways(n-i,m)
        i += 1
    return res
s,m = 4,2
print countways(s+1,m)