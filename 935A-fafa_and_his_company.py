n=int(input())
count=0
if n>3:
    for i in range(1,n):
        x=n-i
        if x%i==0:
            count+=1
else:
    count=1
print(count)