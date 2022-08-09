def pivot(list,first,last):
    pivot = first
    left = first+1
    right =last
    
    while True:
        while left <= right and list[left] <= list[pivot]:
            left = left + 1
        while left <= right and list[right] >= list[pivot]:
            right = right-1
        if left > right:
            break
        else :
            list[left],list[right] = list[right],list[left] 
    list[first],list[right] = list[right],list[first]
    return right

def quick_sort(list,first,last):
    if first<last:
        piv = pivot(list,first,last)
        quick_sort(list,first,piv-1)
        quick_sort(list,piv+1,last)

list = [15,85,48,66,2,7,5]
quick_sort(list,0,len(list)-1)
print(list)
