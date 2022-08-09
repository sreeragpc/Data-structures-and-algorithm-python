def search(arr,x):
    low = 0
    high = len(arr) -1
    m = 0
    while low <= high:
        m = (high + low) // 2 
        if arr[m] < x:
            low = m + 1  
        elif arr[m] > x:
            high = m - 1
        else:
            return m      
    return -1



arr = [ 2, 3, 4, 10, 40 ]
x = 10

result = search(arr, x)
print(result)