list = [2,1,-5,3,5,8,7,4,16,12,15,4]
n = 0 
for j in range(len(list)):
    for i in range(n, len(list)):
        if i == n:
            smallest = list[n]
        if smallest > list[i]:
            smallest = list[i]
            k = i 
            list[n], list[k] =list[k], list[n]
    n = n+1          
print(list)    
