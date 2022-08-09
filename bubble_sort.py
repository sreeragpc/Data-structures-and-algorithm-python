list = [8,6,7,30]
def bubble(list):
    for i in range(len(list)-1) :
        for i in range(len(list)-1-i) :
            if list[i] > list[i+1]:
                list[i], list[i+1]= list[i+1] ,list[i]   
    print(list)

bubble(list)