for _ in range(int(input())):
    n,m=map(int,input().split())
    c=[]
    m1=0
    j=1
    d=0
    for i in range(m):
        x=[int(k) for k in input().split()]
        if(len(x)!=1):
            c.append(x[0])
            c.append(x[1])
        else:
            m1+=1
    while(j<n):
        if(c[j]==c[j+1]):
            j+=2
            if(d==0):
                m1+=1
            d+=1
            continue
        else:
            m1+=1
            if(n-j>2):
                j+=2
            else:
                j=j+(n-j)
    print(m1)
        
    
