n=int(input(""))
s=['T','i','m','r','u']
p=[]
while n!=0:
    no=int(input(""))
    x=input()
    l=[]
    for i in x:
        l.append(i)

    l.sort()
    if l == s:
        p.append("YES")
    else:
        p.append("NO")
    
    n-=1
for i in p:
    print(i)

#1722A