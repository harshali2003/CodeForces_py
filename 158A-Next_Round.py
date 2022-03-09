n_participants,kth_place = input().split()
n_participants= int(n_participants)
kth_place = int(kth_place)
s = input().split()
scores = []
count = 0

for i in s:
    scores.append(int(i))

qua_m = scores[kth_place-1]

for i in scores:
    if i > 0:
        if i >= qua_m:
            count += 1

print(count)