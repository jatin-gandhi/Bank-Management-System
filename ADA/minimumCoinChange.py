import sys

def coinChange(value,coins):
    Inf = sys.maxsize
    t = [0 for i in range(value+1)]
    r = [0 for i in range(value+1)]
    #print(r)
    for i in range(1,value+1,1):
        mini = Inf
        for j in range(len(coins)):
            if i>= coins[j]:
                t[i] = min(1+t[i-coins[j]],mini)
                r[i] = j 

    print(t[value])
    print(r)
    x = value
    sequence = []
    while x>0:
        sequence.append(coins[r[x]])
        x= x - coins[r[x]]
    print(sequence)

coinChange(13,[1,2,3])