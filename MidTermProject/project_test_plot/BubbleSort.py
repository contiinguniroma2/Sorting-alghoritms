def bubbleSort(list):
    swap=True
    while swap:
        swap=False
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                #list[j], list[j + 1] = l[j + 1], l[j]
                v=list[j]
                list[j]=list[j+1]
                list[j+1]=v
                swap=True
    return list
