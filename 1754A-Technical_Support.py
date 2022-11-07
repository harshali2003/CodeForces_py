loop=int(input(""))
while loop!=0:
    criteria=0
    x=int(input(""))
    convo=input("")
    len=0
    for i in convo:
        len+=1
        if i=='Q':
            criteria+=1
        else:
            if criteria==0:
                criteria=0
            else:
                criteria-=1
    if criteria==0 :
        print("Yes")
    else:
        print("No")
    loop-=1