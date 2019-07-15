vin,de=map(str,input().split())
vin=list(vin)
de=list(de)
kow=0
for f in range(0,len(vin)):
        if(vin[f]!=de[f]):
            kow=kow+1
if(kow==1):
    print("yes")
else:
    print("no")
