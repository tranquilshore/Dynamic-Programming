'''
It is a bit complicated to solve like the simpler question. 
because in the simpler question whether to rob num[lo] is entirely our choice.
But, it is now constrained by whether num[hi] is robbed
solution:
the solution is simply the larger of two cases with consecutive houses
i.e. house i not robbed, break the circle, solve it, or house i + 1 not robbed
For example, 1 -> 2 -> 3 -> 1 becomes 2 -> 3 if 1 is not robbed.
'''
def rob_in_line(money,lo,hi):
    incl = 0
    excl = 0
    for i in range(lo,hi+1):
        temp = incl
        incl = max(incl,excl+money[i])
        excl = temp

    return max(incl,excl)

def rob_in_circle(money):
    if len(money) == 0:
        return 0
    if len(money) == 1:
        return money[0]
    return max(rob_in_line(money,0,len(money)-2), rob_in_line(money,1,len(money)-1))
