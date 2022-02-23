testcases = int(input())
while testcases!=0: 
    str = input()
    str_copy=str
    
    str="a"+str
    new_str=""
    for i in range(1,len(str)+1):
        new_str+=str[-i]

    if new_str== str:
        pal=True
    else:
        pal=False
    
    all_a = True
    for i in range(0,len(str)):
        if str[i]!='a':  
            all_a = False 
    
    if all_a:
        print("no")
    else:    
        if not pal :
            print("yes")
            print(str)
        else:
            print("yes")
            print(str_copy+"a")

    testcases=testcases-1
    