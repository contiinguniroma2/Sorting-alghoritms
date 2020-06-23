def inserctionSort(list):
    for i in range(1,len(list)):
        x=list[i]
        for j in range(i-1,-1,-1):
            if list[j]<=x:
                break
        if j<i-1:
            for z in range(i,j+1,-1):
                list[z]=list[z-1]
            list[j+1]=x
    return list