import sys
a = [100,80,120,130,70,60,100,125]
n = len(a)
minp = sys.maxint
profit = 0
for i in range(n):
    profit = max(profit,a[i]-minp)
    minp = min(a[i],minp)

print profit
