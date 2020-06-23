import random
from time import time
from math import ceil
from MergeSort import mergeSort
from quickSort import quickSort
from BubbleSort import bubbleSort
from InserctionSort import inserctionSort
from SelectionSort import selectionSort
from heapSort import heapSort
import Test1
import Test2
import Test3
import Test4
import Test5
import Test6
import Test7
import Test8
import test9
import test10
import test11
import test12
import Test13
import test14
import test15
import test16
"""
Nel seguente codice sono importati più moduli "test" di quanti effettivamente ne vengano eseguiti in quanto per come è scritto 
l'algoritmo sampleMedianSelect (versione ordinamento) se m<=20 utilizza per ordinare il campione bubbleSort,inserctionSort e 
selectionSortmentre per m>20 tutti gli altri algoritmi di ordinamento visti a lezione perciò ai fini del testing delle 
prestazioni sarebbe inutile mandarli tutti in esecuzione però per completezza in un caso pratico 
l'utente potrebbe sceglierne uno a piacimento (in quanto vi sono tutte le possibili combinazioni) ovviamente
come si vedrà dai test ci sono delle versioni più efficienti delle altre e perciò la scelta ricadrebbe su quelle.
"""

if __name__ == "__main__":
    random.seed(2)
    # SMALL SAMPLE
    m=-1
    while m < 20:
        m += 3       # m parte da 2 cosi' viene mostrata anche una variante in cui m troppo grande viene gestita
        j = 1        # decrementando m alla lunghezza dell'array
        while m <= 20 and j <= 16385:
           #while j<=32769:  # NOTA: gia con questa dimensione dell'input l'algoritmo impiega anche piu' di 60 secondi
           # percio' si puo' optare per questo while che lascia comunque apprezzare l'andamento dell'algoritmo
            A = []        #in più o meno 5- secondi per variante di quickSort
            print("")
            print("TESTING WITH n=", j)
            print("TESTING WITH m=", m)
            print("")
            for i in range(0,j):
                A.append(random.randint(0,j))
            B = A
            j=2*j

            # SAMPLE WITH SELECTION

            start = time()
            Test13.QuickSort(A, m)
            end = time()
            temp = end - start
            print("Sample's median chosen with trivialSelect time -->", temp)

            A=B
            start = time()
            test14.QuickSort(A, m)
            end = time()
            temp = end - start
            print("Sample's median chosen with heapSelect time -->", temp)

            A=B
            start = time()
            test15.QuickSort(A, m)
            end = time()
            temp = end - start
            print("Sample's median chosen with selectRand time -->", temp)

            A=B
            start = time()
            test16.QuickSort(A, m)
            end = time()
            temp = end - start
            print("Sample's median chosen with selectDet time -->", temp)


            # SMALL SAMPLE WITH SORTING

            A = B
            start = time()
            Test5.QuickSort(A,m)       # Sample ordered with selectionSort
            end = time()
            temp = end - start
            print("Sample sorted with selectionSort time -->", temp)

            A = B
            start = time()
            Test1.QuickSort(A,m)       # Sample ordered with inserctionSort
            end = time()
            temp = end - start
            print("Sample sorted with inserctionSort time -->", temp)

            A = B
            start = time()
            test9.QuickSort(A,m)       # Sample ordered with bubbleSort
            end = time()
            temp = end - start
            print("Sample sorted with bubbleSort time -->", temp)

            # OTHER SORTING ALGHORITMS

            A = B
            start = time()
            mergeSort(A)        # mergeSort
            end = time()
            temp = end - start
            print("Array sorted with mergeSort time-->", temp)

            A = B
            start = time()
            heapSort(A)         # heapSort
            end = time()
            temp = end - start
            print("Array sorted with heapSort time-->", temp)

            A = B
            start = time()
            quickSort(A,False)  # non-deterministic quickSort
            end = time()
            temp = end - start
            print("Array sorted with classic non-deterministic quickSort time-->", temp)

            A = B
            start = time()
            A.sort()            #pythonSort
            end = time()
            temp = end - start
            print("Array sorted with pythonSort time-->", temp)
            """ I confronti con gli algoritmi seguenti sono eseguiti solo su un array piccolo in quanto 
            al crescere di n il loro tempo è di gran lunga superiore a quelli degli algoritmi precedenti 
            """
            """
            A = B
            start=time()
            selectionSort(A)
            end=time()
            temp=end-start
            print("Array sorted with time-->",temp)
            A = B 
            start = time()
            inserctionSort(A)
            end = time()
            temp = end - start
            print("Array sorted with inserctionSort time-->", temp)
            A = B
            start = time()
            bubbleSort(A)
            end = time()
            temp = end - start
            print("Array sorted with bubbleSort time-->", temp)"""

    # BIG SAMPLE
    print("BIG SAMPLE")
    m=-59
    while m<=500:
        m += 80
        j = 1
        while m<500 and j <= 16385:
        # while j<=32769:  # NOTA: gia con questa dimensione dell'input l'algoritmo impiega anche piu' di 60 secondi
          # percio' si puo' optare per questo while che lascia comunque apprezzare l'andamento dell'algoritmo
            A=[]
            print("TESTING WITH n =", j)  # in più o meno 15 secondi per variante di quickSort
            print("TESTING WITH m =", m)
            print("")
            print("")
            for i in range(0, j):
                A.append(random.randint(0, j))
            B = A
            j = 2 * j
            # SAMPLE WITH SELECTION

            start = time()
            Test13.QuickSort(A, m)
            end = time()
            temp = end - start
            print("Sample's median chosen with trivialSelect time -->", temp)

            A = B
            start = time()
            test14.QuickSort(A, m)
            end = time()
            temp = end - start
            print("Sample's median chosen with heapSelect time -->", temp)

            A = B
            start = time()
            test15.QuickSort(A, m)
            end = time()
            temp = end - start
            print("Sample's median chosen with selectRand time -->", temp)

            A = B
            start = time()
            test16.QuickSort(A, m)
            end = time()
            temp = end - start
            print("Sample's median chosen with selectDet time -->", temp)

            # HIGH SAMPLE WITH SORTING
            A = B
            start = time()
            Test1.QuickSort(A, m)
            end = time()
            temp = end - start
            print("Sample sorted with pythonSort time -->", temp)

            A = B
            start = time()
            Test2.QuickSort(A, m)
            end = time()
            temp = end - start
            print("Sample sorted with mergeSort time -->", temp)

            A = B
            start = time()
            Test3.QuickSort(A, m)
            end = time()
            temp = end - start
            print("Sample sorted with quickSort classic time -->", temp)

            A = B
            start = time()
            Test4.QuickSort(A,m)
            end = time()
            temp = end - start
            print("Sample sorted with heapSort time -->", temp)

            # OTHER SORTING ALGHORITMS

            A = B
            start = time()
            mergeSort(A)  # mergeSort
            end = time()
            temp = end - start
            print("Array sorted with mergeSort time-->", temp)

            A = B
            start = time()
            heapSort(A)  # heapSort
            end = time()
            temp = end - start
            print("Array sorted with heapSort time-->", temp)

            A = B
            start = time()
            quickSort(A, False)  # non-deterministic quickSort
            end = time()
            temp = end - start
            print("Array sorted with classic non-deterministic quickSort time-->", temp)

            A = B
            start = time()
            A.sort()  # pythonSort
            end = time()
            temp = end - start
            print("Array sorted with pythonSort time-->", temp)
            """ I confronti con gli algoritmi seguenti sono eseguiti solo su un array piccolo in quanto 
            al crescere di n il loro tempo è di gran lunga superiore a quelli degli algoritmi precedenti 
            """
            """
            A = B
            start=time()
            selectionSort(A)
            end=time()
            temp=end-start
            print("Array sorted with time-->",temp)
            A = B 
            start = time()
            inserctionSort(A)
            end = time()
            temp = end - start
            print("Array sorted with inserctionSort time-->", temp)
            A = B
            start = time()
            bubbleSort(A)
            end = time()
            temp = end - start
            print("Array sorted with bubbleSort time-->", temp)"""