from HeapMax import HeapMax
def heapSort(l):

    heap = HeapMax(l);

    heap.heapify();  # costruisce l'heap

    while not heap.isEmpty():  # finchè l'heap non è vuoto cancella il massimo, ordinando così gli elementi in modo crescente
        heap.deleteMax()  # ATTENZIONE: per come implementata la deleteMax, nessun elemento viene realmente cancellato dalla lista passata in
        # argomento a HeapMax, ma spostato in fondo. Otteniamo un ordinamento crescente.
