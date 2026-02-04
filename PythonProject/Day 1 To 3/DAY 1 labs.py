# question 1
for i in range(1,21):
    print(i)
from functools import reduce
l=list(i for i in range(1,21))
print(l)

e=list(filter(lambda x:x%2==0,l))
print(e)

sqn=list(map(lambda x:x*x,e))
print(sqn)

sum=reduce(lambda a,b:a+b,sqn)
print(sum)
for i,val in enumerate(sqn):
    print(i,val)

