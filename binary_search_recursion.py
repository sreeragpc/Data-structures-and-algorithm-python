def search(arr,start,end,x):
    if end >= start :
        m = (start + end) // 2
        if arr[m] == x:
            return m
        elif arr[m] > x :
            return search(arr, start, m-1,x)
        else:
            return search(arr, m+1, end, x)
    else:
        return print("not found")

arr = [ 2, 3, 4, 10, 40 ]
x = 10

result = search(arr, 0, len(arr)-1, x)
print(result)
