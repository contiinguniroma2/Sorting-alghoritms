import random
from math import ceil
from quickSelectDet import quickSelectDet
from quickSelectRand import quickSelectRand
from TrivialSelect import trivialSelect
from heapSelect import heapSelect
from MergeSort import mergeSort

"""In questo file è riportato l'algoritmo quickSort in cui la scelta del pivot avviene tramite un algoritmo di selezione
il quale dato l'array in ingresso ne prende un sottoinsieme di elementi casuali e ne seleziona il mediano con gli algoritmi
visti a lezione (sono importati e commentati tutti gli algoritmi utilizzati per i test)"""

def sampleMedianSelect(list, left, right,m):
    if m>=len(list[left:right+1]) :
        #print("m>len(list)->decreasing m")
        m = len(list[left:right + 1])                               # alla minima grandezza accettabile affinche l'algoritmo funzioni
    S = random.sample(list[left:right + 1], m)  # cosi in un caso pratico in cui verrebbe utilizzato in qualche applicazione
    #m=quickSelectDet(S,ceil(len(S)/2),10)       # in cui m è scelto a caso l'algoritmo non si ferma,al massimo rallenta un po'
    #m = trivialSelectDet(S, ceil(len(S) / 2))  # oppure potrebbe anche non accadere mai con opportuni controlli a monte
    #m = quickSelectRand(S, ceil(len(S) / 2))   # nella scelta di m da parte dell'utente o dalla funzione chiamante
    m = heapSelect(S, ceil(len(S) / 2))
    return m


# QUICKSORT

def QuickSort(l,m):
    if m==0:
        m+=1
    RecursiveQuickSort(l, 0, len(l) - 1,m)    # Chiamata a quickSort dell'array in ingresso con m scelto dall'utente
    print("quickSort------Fine:   ", l)


def RecursiveQuickSort(l, left, right,m):
    print("recursiveQuickSort------left:    ", left)
    print("recursiveQuickSort------right:   ", right)
    if left >= right:                          # Passo base del quickSort
        print("recursiveQuickSort------left>=right, esco da recurQuick. ")
        return
    mid = Partition(l, left, right,m)          # Partition in cui viene passato l'm che andra' a sampleMedianSelect
    print("recursiveQuickSort------mid dopo partition:  ", mid)
    RecursiveQuickSort(l, left, mid - 1,m)     # Ricorsione sugli elementi piu piccoli del pivot
    print("recursiveQuickSort------array dopo left quick:   ", l)
    RecursiveQuickSort(l, mid + 1, right,m)    # Ricorsione sugli elementi piu grandi del pivot
    print("recursiveQuickSort------array dopo right quick:   ", l)


def Partition(l, left, right,m):
    inf = left
    print("partition------inf: ", inf)
    sup = right + 1
    print("partition------sup: ", sup)
    random.seed(2)
    if m==1:                                       # se m=1 per evitare qualsiasi passo di oridnamento che ad esempio
        mid=random.sample(l[left:right + 1], 1)    # nel caso di heapSort comporterebbero almeno 2 chiamate a funzione
    else:                                          # si esegue direttamente il quickSort classico
        mid = sampleMedianSelect(l, left, right,m) # altrimenti si procede con la scelta del pivot con sampleMedianSelect
        print("partition------mid random:   ", mid)
    indice = l.index(mid)
    l[left], l[indice] = l[indice], l[left]  # swap del primo elemento con quello scelto da sampleMedianSelect
    print("partition------array dopo mid random, swap del pivot:   ", l)
    indice = left  # il pivot è il primo elemento dell'array

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
    print("- " * left + str(l[left:right + 1]) + " -" * (len(l) - right - 1))
    return sup

# Breve main per il test dell'algoritmo

if __name__ == "__main__":
    #A = []
    A = [30, 30, 30, 30, 30]
    A=[]
    dim=1000
    random.seed(2)
    """for i in range(0,dim):
        A.append(random.randint(0,dim+1000))"""
    B=A
    QuickSort(A,50)
    mergeSort(B)
    for i in range(0,len(A)-1):
        if A[i]!=B[i]:
            print("NOT EQUAL")
            break
    print("EQUAL")