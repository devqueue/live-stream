LIST  = [15,14,13,12,10,5,2,1]

print(LIST)
n = len(LIST)
for i in range(n):
    for j in range(0, n-i-1):
        if LIST[j]> LIST[j+1]:
            LIST[j], LIST[j+1] = LIST[j+1], LIST[j]

print(LIST)
