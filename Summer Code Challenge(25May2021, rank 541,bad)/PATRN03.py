t=int(input())
for i in range(t):
    x=int(input())
    n=[]
    e=''
    for j in range(1,x+1):
        for p in range(j):
            e+='*'
        e=e[:len(e)-1]
        e+=str(j)
        print(e)
