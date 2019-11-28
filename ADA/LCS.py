def lcs(string1,string2):
    m = len(string1)
    n = len(string2)
    L = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i ==0 or j==0:
                L[i][j] =0
            elif string1[i-1]==string2[j-1]:
                L[i][j] = 1+L[i-1][j-1]
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
    sequence =[]
    i,j=m,n
    while i>0 and j>0:
        if string1[i-1]==string2[j-1]:
            sequence.append(string1[i-1])
            i-=1
            j-=1
        elif L[i-1][j] >L[i][j-1]:
            i-=1
        else:
            j-=1
    
    print(("".join(sequence))[::-1])

lcs("aggtab","gxtxayb")
