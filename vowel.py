a=list(input().split(" "))
b=list(input().split(" "))
c=len(a)
d=len(b)
if(c==d):
    mydict1=dict(zip(a,b))
    e=list(input().split(' '))
    a.append(e[0])
    b.append(e[1])
    mydict2=dict(zip(a,b))
    print(mydict1)
    print(mydict2)
else:
    print('Invalid')
