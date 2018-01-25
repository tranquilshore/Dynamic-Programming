money = [4,1,1,4,2,1]

def rob_in_line(money,lo,hi):
    if len(money) == 0:
        return 0
    if len(money) == 1:
        return money[0]

    incl = 0
    excl = 0
    for i in range(lo,hi+1):
        temp = incl
        incl = max(incl,excl+money[i])
        excl = temp

    return max(incl,excl)

print rob_in_line(money,0,(len(money)-1))