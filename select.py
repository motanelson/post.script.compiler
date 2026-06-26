import os
down="https://en.wikipedia.org/wiki/List_of_CIL_instructions"
files="down.html"
finds="Common Type System."
select1="Forms"
select2="Operand Stack"
print("\033c\033[47;31m\nfile: "+files)
os.system("curl "+down+" -o "+files)
f1=open(files,"r")
a=f1.read()
f1.close()

b=a.find("<body")
if b<0:
    b=a.find("<BODY")
a=a[b:]
a=a.replace("\n","")
a=a.replace("\r","")
a=a.replace("<tr>","\n")
a=a.replace("<td>"," | ")

bodys=a.split("<")
c=""
for body in bodys:
    t=body.split(">")
    if len(t)>1:
        c=c+t[1]

b=c.find(finds)
if b<0:
    print("error:")
else:
    d=len(finds)+b
    c=c[d:]
finds="See also"
b=c.find(finds)
if b<0:
    print("error:")
else:
    d=len(finds)+b
    c=c[:d]
g=c.split("\n")
v=""
for gg in g:
    ll=gg.split("|")
    if len(ll)>1:
        v=v+"\n"+ll[0]+" | "+ ll[1]

f1=open(files,"w")
f1.write(v)
f1.close()