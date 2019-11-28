import numpy as np
def lis(array,n):
    li = [1]*(n+1)
    combinations =[]
    for i in range(1,n):
        mat =[]
        for j in range(0,i):
            if (array[i] >array[j]) and (li[i] < li[j]+1):
                li[i] = li[j]+1
                mat.append(array[j])
        mat.append(array[i])
        combinations.append(mat)


    return (combinations)

print(lis([10,22,9,33,21,50,41,60,80],9))