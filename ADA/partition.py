def partition(array):
    n = len(array)
    sum = 0
    for i in range(n):
        sum +=array[i]

    if sum %2 !=0:
        return False
    par = [[True for j in range(n+1)] for i in range(sum//2+1)]
    for i in range(1,(sum//2)+1):
        par[i][0] = False
    for i in range(1,sum//2+1):
        for j in range(1,n+1):
            par[i][j] = par[i][j-1]
            if i >=array[j-1]:
                par[i][j] = par[i][j] or par[i-array[j-1]][j-1]

    return True

print(partition([1,5,11,5]))