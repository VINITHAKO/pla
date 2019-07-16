#v
d=input()
a=str(input())
o=('a','e','i','o','u')
for i in a:
    if i in o:
        a=a.replace(i,"")
print(a[::-1])
