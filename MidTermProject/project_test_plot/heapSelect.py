from HeapMin import HeapMin

def heapSelect(l, k):

    if k <= 0 or k > len(l):
        return None

    heap = HeapMin(l)
    heap.heapify()

    for i in range(0, k - 1):  # @UnusedVariable i
        heap.deleteMin()

    return heap.findMin()

