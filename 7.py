vi=list(input())
dd=len(vi)
new=''
for l in range (0,dd,2):
    vi[l],vi[l+1]=vi[l+1],vi[l]
print(*vi,sep='')
