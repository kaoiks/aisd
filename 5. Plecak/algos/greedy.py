def greedy(kontenery,n,space):
    sortedKontenery = sorted(kontenery,key = lambda x: x[1]/x[0])[::-1]
    
    statek=[]
    i = 0
    space = space #wolne miejsce na statku
    while(i<n and space>0):
        if sortedKontenery[i][0]<=space:
            statek.append(sortedKontenery[i])
            space-=sortedKontenery[i][0]
        i+=1
    return statek