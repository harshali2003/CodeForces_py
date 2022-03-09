testcases = int(input())
while testcases!=0:
    string = input()
    length = len(string)
    if length<11:
        print(string)
    else:
        length=length-2
        output = string[0]+str(length)+string[-1]
        print(output)
    testcases=testcases-1
