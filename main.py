N=int(input())
m=[True]*(N+1)
m[0]=m[1]=False
for i in range(2,N+1):
    if m[i]:
        if 2<=i<=N:
            print(i, end=' ')
        for k in range(i**2,N+1,i):
            m[k]=False
