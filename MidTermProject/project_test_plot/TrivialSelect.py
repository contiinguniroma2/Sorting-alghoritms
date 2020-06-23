def trivialSelect(l, k):

    length = len(l)
    if k <= 0 or k > length:
        return None

    for i in range(0, k):
        minimum = i
        for j in range(i + 1, length):
            if l[j] < l[minimum]:
                minimum = j
        l[minimum], l[i] = l[i], l[minimum]

    return l[k - 1]

