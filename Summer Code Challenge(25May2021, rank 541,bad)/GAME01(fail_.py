t=int(input())
for i in range(t):
    gay=input().split(' ')
    gay1=input().split(' ')
    gay2=input().split(' ')
    gay3=[]
    gay4=[]
    gay5=[]
    for i in gay1:
        if int(i) % 3 == 0:
            l=0
            for c in gay1:
                if i==c:
                    l+=1
            if l<2:
                gay3.append(i)
    for i in gay2:
        if int(i)%3==0:
            l=0
            for c in gay1:
                if i==c:
                    l+=1
            if l<2:
                gay4.append(i)
    for i in gay3:
        if i in gay4:
            gay5.append(i)
    gay5.sort()
    if len(gay5)==0:
        print(-1)
    else:
        e=''
        for i in gay5:
            e+=i+' '
        print(e)
