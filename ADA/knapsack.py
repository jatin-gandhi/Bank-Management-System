def knapsack(W,weight,value,n):
    K = [ [ 0 for i in range(W+1)] for j in range(n+1) ]
    for i in range(n+1):
        for j in range(W+1):
            if i ==0 or j ==0:
                K[i][j] =0
            elif weight[i-1] <= W:
                K[i][j] = max((value[i-1]+K[i-1][j-weight[i-1]]),K[i-1][j])
            else:
                K[i][j] = K[i-1][j]

    return K[n][W]

print(knapsack(50,[10,20,30],[60,100,120],3))
