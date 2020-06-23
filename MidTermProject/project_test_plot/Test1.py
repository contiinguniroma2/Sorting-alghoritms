import random
from math import ceil
from SelectionSort import selectionSort


def sampleMedianSelect(list, left, right,m):
    if m>=len(list[left:right+1]) :
        #print("m>len(list)->decreasing m")
        m = len(list[left:right + 1])
    S = random.sample(list[left:right + 1], m)
    if m<=20:
        selectionSort(S)
    else:
        S.sort()
    return S[ceil(len(S)/2)]




def QuickSort(l,m):
    if m==0:
        m+=1
    RecursiveQuickSort(l, 0, len(l) - 1,m)
    #print("quickSort------Fine:   ", l)


def RecursiveQuickSort(l, left, right,m):
    #print("recursiveQuickSort------left:    ", left)
    #print("recursiveQuickSort------right:   ", right)
    if left >= right:
        #print("recursiveQuickSort------left>=right, esco da recurQuick. ")
        return
    mid = Partition(l, left, right,m)
    #print("recursiveQuickSort------mid dopo partition:  ", mid)
    RecursiveQuickSort(l, left, mid - 1,m)
    #print("recursiveQuickSort------array dopo left quick:   ", l)
    RecursiveQuickSort(l, mid + 1, right,m)
    #print("recursiveQuickSort------array dopo right quick:   ", l)


def Partition(l, left, right,m):
    inf = left
    #print("partition------inf: ", inf)
    sup = right + 1
    #print("partition------sup: ", sup)
    random.seed(2)
    if m==1:
        mid=random.sample(l[left:right + 1], 1)
    else:
        mid = sampleMedianSelect(l, left, right,m)
        #print("partition------mid random:   ", mid)
    indice = l.index(mid)
    l[left], l[indice] = l[indice], l[left]  # exchange first elem with the randomically chosen one
    #print("partition------array dopo mid random, swappo il pivot:   ", l)
    indice = left  # the median is the first elem of the array

    while True:
        inf += 1
        while inf <= right and l[inf] <= l[indice]:
            inf += 1
        sup -= 1
        while l[sup] > l[indice]:
            sup -= 1
        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break
    l[indice], l[sup] = l[sup], l[indice]
    #print("- " * left + str(l[left:right + 1]) + " -" * (len(l) - right - 1))
    return sup


