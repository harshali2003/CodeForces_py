iterate=int(input(""))
l=[]
while iterate!=0:
    n=int(input(""))
    str=""
    sum=0
    x=input("")
    for i in range(0,n-1):
        sum+=int(x[i])

        if x[i]=="0" and x[i+1]=="1":
            if sum%2==0:
                str=str+"+"
            else:
                str=str+"-"
        elif x[i]=="1" and x[i+1]=="1":
            if sum%2==0:
                str=str+"+"
            else:
                str=str+"-"
        else:
            str=str+"+"


    l.append(str)
    iterate-=1

for i in l:
    print(i)

#1774A