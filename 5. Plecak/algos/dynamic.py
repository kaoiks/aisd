def dynamic(kontenery,n,space):
    tab =[]
    
    for i in range(n+1):
        row = [0 for j in range (space+1)]
        tab.append(row)

    for i in range(1,n+1):
        for q in range(space+1):
            size = kontenery[i-1][0]
            value = kontenery[i-1][1]
            if size > q:
                tab[i][q] = tab[i-1][q]
            else:
                tab[i][q] = max(tab[i-1][q], tab[i-1][q-size]+value)
    
    statek=[]
    
    x=n
    y=space
    while(x>0 and y>0):
        if tab[x][y]==tab[x-1][y]:
            x-=1
        else:
            statek.append(kontenery[x-1])
            y-=kontenery[x-1][0]
            x-=1
    #print(statek)
    return statek