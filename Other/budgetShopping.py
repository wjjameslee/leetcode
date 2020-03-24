def budgetShopping(n, bundleQuantities, bundleCosts):
    dp = []
    # initialize dp array
    for i in range(0,n+1):
        dp.append(0)
    
    for i in range(1, n+1):
        maxassign = 0
        for j in range(0, len(bundleQuantities)):
            if i - bundleCosts[j] >= 0:
                maxsofar = max(bundleQuantities[j] + dp[i-bundleCosts[j]], dp[i-1])
                if maxsofar > maxassign:
                    maxassign = maxsofar
            else:
                maxsofar = dp[i-1]
                if maxsofar > maxassign:
                    maxassign = maxsofar
        
        dp[i] = maxassign
        maxassign = 0
    print(dp)
    return dp[n]
