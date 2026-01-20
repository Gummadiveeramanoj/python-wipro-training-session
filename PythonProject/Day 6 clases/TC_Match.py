import re
text="pythonpowerful"
result=re.match("python",text)
if result:
    print("match found")
else:
    print("match not found")

searchresult=re.search("powerful",text)
print(searchresult.group())
print(searchresult.start())
print(searchresult.end())

email="admin@gmail.com"
if re.match(r"[a-zA-Z]+@",email):
    print("Valid Start")

result2=re.fullmatch(r"\d{10}","1234567898")
print(result)


print(re.findall(r"\d+","price 50 and 100 and 200"))

for n in re.finditer(r"\d+","A1 b1000, B33, C444"):
    print(n.group(),n.start(),n.end())

for n in re.finditer(r"[a-z]","a1 b1000, B33, C444"):
    print(n.group(),n.start(),n.end())
for n in re.finditer(r"[A-Z]","a1 b1000, B33, C444"):
    print(n.group(),n.start(),n.end())

print(re.search(r"\d+","Age is 25"))

print(re.search(r"^a.*c$","abnkkkkkknnc"))

m=re.search(r"\w+(?=@)","test@gmail.com")
print(m.group())

print(re.search("python","Python",re.I))

text4="one\ntwo\nthree"
print(re.findall(r"^t\w+",text4,re.M))

