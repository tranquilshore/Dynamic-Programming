'''
you can either climb one or two steps. You need to find minimum cost to reach the top of the floor,
and you can either start from the step with index 0, or the step with index 1.

'''

def min_cost(cost):
    dp = [0]*(len(cost)+1)
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2,len(cost)):
        dp[i] = min(dp[i-1],dp[i-2]) + cost[i]
    
    return min(dp[len(cost) -1], dp[len(cost)-2])

print min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
