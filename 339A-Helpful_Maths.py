str = list(map(int,input().split("+")))
str.sort()
l=len(str)
count=0
for i in str:
    count+=1
    if count==l:
        print(i)
    else:
        print(i,end="+")