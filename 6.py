v1,v2=map(str,input().split())
for s in v1:
    d=v1.count(s)
for y in v2:
    i=v2.count(y)
if(d==i):
    print("yes")
else:
    print("no")
