steps=0
a=int(input())

while a>5:
    a-=5
    steps+=1

if a==0:
    print(steps)
else:
    steps+=1
    print(steps)

