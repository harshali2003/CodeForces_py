a,b=map(int,input().split())
count=0
while b>=a:
    count+=1
    b*=2
    a*=3
print(count)