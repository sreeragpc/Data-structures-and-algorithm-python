list = [3,2,5,4,7,8,23,12]

for i in range(1,len(list)):
    current = list[i]
    j = i-1
    while j>=0 and current < list[j]:
        list[j+1] = list[j]
        j -= 1
    list[j+1] = current    
print(list)