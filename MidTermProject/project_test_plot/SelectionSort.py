def selectionSort(list):
    for i in range(0,len(list)-2):
        m=i+1
        for j in range(i+2,len(list)):
            if list[j]<list[m]:
                m=j
        swap=list[m]
        list[m]=list[i+1]
        list[i+1]=swap
    return list
