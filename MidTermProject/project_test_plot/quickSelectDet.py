from math import ceil
from TrivialSelect import trivialSelect

def quickSelectDet(l, k, minLen):
    if k <= 0 or k > len(l):
        return None
    return recursiveQuickSelectDet(l, 0, len(l) - 1, k, minLen)


def recursiveQuickSelectDet(l, left, right, k, minLen):

    if left == right:
        return l[left]

    # si usa stop per decidere quando smettere di ricorrere ed utilizzare un algoritmo diverso
    if len(l) < minLen:
        med = trivialSelect(l[left: right + 1], k - left)

        return med

    # compute groups of five
    numElem = right - left + 1
    numGroups = int(ceil(numElem / 5.0))
    median = []
    for i in range(0, numGroups):
        dimGroup = 5 if (i < numGroups - 1 or numElem % 5 == 0) \
            else (numElem - (numGroups - 1) * 5)
        a = left + i * 5
        b = left + i * 5 + dimGroup - 1


        m = trivialSelect(l[a:b + 1], int(ceil(dimGroup / 2.0)))
        median.append(m)



    vperno = quickSelectDet(median, ceil(len(median) / 2), minLen)  #vperno è un valore e non un indice



    perno = partitionDet(l, left, right,
                         vperno)  # Watch: this is a new function which takes the pivot as the parameter

    posperno = perno + 1
    if posperno == k:

        return l[perno]
    if posperno > k:

        return recursiveQuickSelectDet(l, left, perno - 1, k, minLen)
    else:

        return recursiveQuickSelectDet(l, perno + 1, right, k, minLen)


def partitionDet(l, left, right, pivot):
    #nota: pivot è un valore dell'array l e non un indice!
    inf = left
    sup = right

    while True:
        while inf <= right and l[inf] <= pivot:
            if l[inf] == pivot and l[left] != pivot:
                l[left], l[inf] = l[inf], l[left]
            else:
                inf += 1

        while sup >= 0 and l[sup] > pivot:
            sup -= 1

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    l[left], l[sup] = l[sup], l[left]



    return sup
