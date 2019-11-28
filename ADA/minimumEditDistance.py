def editDistance(string1,string2):
    m =len(string1)
    n = len(string2)
    l = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                l[i][j] = j
            elif j==0:
                l[i][j]=i
            elif string1[i-1]==string2[j-1]:
                l[i][j]=l[i-1][j-1]
            else:
                l[i][j] = 1 + min(l[i-1][j],l[i][j-1],l[i-1][j-1])

    return l[m][n]

print(editDistance("sunday","saturday"))