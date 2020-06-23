from quickSort import partition

def quickSelectRand(l, k):  # k 1...n
    if k <= 0 or k > len(l):
        return None
    return recursiveQuickSelectRand(l, 0, len(l) - 1, k)


def recursiveQuickSelectRand(l, left, right, k):

    if left > right:  # controllo superfluo
        return

    if left == right and k - 1 == left:
        return l[k - 1]

    mid = partition(l, left, right)

    if k - 1 == mid:
        return l[mid]
    if k - 1 < mid:
        return recursiveQuickSelectRand(l, left, mid - 1, k)
    else:
        return recursiveQuickSelectRand(l, mid + 1, right, k)

