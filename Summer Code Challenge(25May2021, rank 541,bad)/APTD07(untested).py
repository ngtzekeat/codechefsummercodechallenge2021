t=int(input())
for i in range(t):
    j=input().split(' ')
    x=input().split(' ')
    n=int(j[0])
    k=int(j[1])
##    gn=0
##    for a in range(1,int(k)+1):
##        ast=0
##        for b in x:
##            if int(a)%int(b)!=0:
##                ast=1
##                break
##        if ast==0:
##            gn+=1
    pl=[]
    for i in x:
        j=0
        while True:
            j+=int(i)
            if j<=k:
                pl.append(j)
            else:
                break
    pl.sort()
    ml=[]
    for i in pl:
        co=0
        for j in pl:
            if i==j:
                co+=1
                
        if co==n:
            ml.append(i)
    ml = list(dict.fromkeys(ml))
    print(len(ml))
