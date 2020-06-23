
def merge(list,left,mid,right):
    nlist=[]
    ileft=left
    iright=mid+1
    while True:
        if list[ileft] < list[iright]:
            nlist.append(list[ileft])
            ileft += 1
            if ileft > mid:  # first subsequence ended. Thus lets copy the remaining elements from the right partition.
                for v in list[iright:right + 1]:
                    nlist.append(v)
                break  # termitates the while loop
        else:  # Symmetric
            nlist.append(list[iright])
            iright += 1
            if iright > right:  # second subsequence ended. Thus lets copy the remaining elements from the left partition.
                for v in list[ileft:mid + 1]:
                    nlist.append(v)
                break  # termitates the while loop
    # Update the list with the computed ordered elements
    for i in range(left, right + 1):
        list[i] = nlist[i - left]

def rMergeSort(list,left,right):
    if(left>=right):
        return
    mid=(left+right)//2
    rMergeSort(list,left,mid)
    rMergeSort(list,mid+1,right)
    merge(list,left,mid,right)

def mergeSort(list):
    rMergeSort(list,0,len(list)-1)
    return list

