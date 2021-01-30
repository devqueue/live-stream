LIST = [15, 14, 13, 12, 10, 5, 2, 1]

print(LIST)

for i in range(1, len(LIST)):
    key = LIST[i]
    j = i-1
    while j>=0 and key < LIST[j]:
        LIST[j+1] = LIST[j]
        j = j-1
    else:
        LIST[j+1] = key

print(LIST)