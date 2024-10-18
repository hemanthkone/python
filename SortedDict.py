n = int(input())
my_dict = {}
l1=[]
l2=[]
for i in range(n):
 a=int(input())
 b=input()
 l1.append(a)
 l2.append(b)
my_dict=dict(zip(l1,l2))
mykeys=list(my_dict.keys())
mykeys.sort()
result={i:my_dict[i] for i in mykeys}
print(result)
