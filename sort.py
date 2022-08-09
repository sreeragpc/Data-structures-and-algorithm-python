list = [3,1,5,6]

for i in range(len(list)-1):
    for j in range(len(list)-1-i):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print(list)

for i in range(len(list)-1):
    n = 0
    for i in range(n,len(list)-1):
        if i == n:
            smallest = list[n]
        if smallest > list[i]:
            smallest = list[i]
            k = i
            list[k],list[n] = list[n], list[k]    
print(list)             

for i in range(1,len(list)-1):
    current = list[i]
    j = i-1
    while j>=0 and current < list[j]:
        list[j+1] = list[j]
        j = j-1
    list[j+1] = current
print(list)    

