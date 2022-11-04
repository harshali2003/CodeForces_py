problems,travel=[int(i) for i in input().split()]
total=4*60
total=total-travel
prob_time=0

for i in range(1,problems+1):
        prob_time+=i*5
        if prob_time>total:
                print(i-1)
                break
        elif i is problems:
                print(i)
                break


        
        



