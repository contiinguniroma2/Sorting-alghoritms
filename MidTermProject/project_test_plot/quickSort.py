import random

def quickSort(l, det=False):
    recursiveQuickSort(l, 0, len(l) - 1, det)


def recursiveQuickSort(l, left, right, det=False):

    if left >= right:
        return

    mid = partition(l, left, right, det)
    recursiveQuickSort(l, left, mid - 1, det)
    recursiveQuickSort(l, mid + 1, right, det)


def partition(l, left, right, det=False):
    inf = left
    sup = right + 1

    if not det:
        random.seed(1)
        mid = random.randint(left, right)
        l[left], l[mid] = l[mid], l[left]  # exchange first elem with the randomically chosen one

    mid = left # the median is the first elem of the array

    while True:
        inf += 1
        while inf <= right and l[inf] <= l[mid]:
            inf += 1

        sup -= 1
        while l[sup] > l[mid]:
            sup -= 1

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    l[mid], l[sup] = l[sup], l[mid]

    return sup

