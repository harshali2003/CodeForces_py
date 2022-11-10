username=input("")
list=[]
for i in username:
    if i not in list:
        list.append(i)

if len(list)%2==0:
   
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

#236A-Boy or Girl
