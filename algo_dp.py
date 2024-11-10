def splitting_cost_minimized(cuts, n):
    cuts = [0] + cuts + [n]
    cutsCount = len(cuts)
    dp = [[0] * cutsCount for _ in range(cutsCount)]
    for l in range(2, cutsCount):
        for i in range(0, cutsCount - l):
            j = i + l
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            dp[i][j] += cuts[j] - cuts[i]
    return dp[0][cutsCount - 1]


n = 34
cuts = [7, 22, 31]

print("Total Cost:", splitting_cost_minimized(cuts, n))
