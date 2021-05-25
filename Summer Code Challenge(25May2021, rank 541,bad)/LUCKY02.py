tc=int(input())
for i in range(tc):
    x=input()
    j='LUCKY'
    for k in x:
        if k!='7' and k!='3':
            j='BETTER LUCK NEXT TIME'
            break
    print(j)
        

        
