testcases= int(input())
while testcases!=0:
    strn,strm = input().split()
    n = int(strn)
    m = int(strm)
    boxes = n*m
    if boxes%2==0:
        print(boxes//2)
    else:
        print((boxes//2)+1)
    testcases-=1