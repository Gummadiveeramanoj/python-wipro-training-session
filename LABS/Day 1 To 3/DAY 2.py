data=[1,2,3,4,5,6,2,4]
sqd=[x*x for x in data]
print(sqd)
s=set(sqd)
print(s)
d={x:x*x*x for x in data}
print(d)