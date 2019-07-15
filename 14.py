#v
d=input()
a=str(input())
o=('a','e','i','o','u')
for i in a:
    if i in o:
        l=l.replace(i,"")
print(l[::-1])
