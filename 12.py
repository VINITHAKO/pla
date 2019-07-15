a,j=map(int,input().split())
v=list(map(int,input().split()))
for j in range (0,j):
    v=[v[-1]]+v[:-1]
print(*v,end='')
