import random
from time import time
from math import ceil
from MergeSort import mergeSort
from quickSort import quickSort
from heapSort import heapSort
import Test1
import Test2
import Test3
import Test4
import Test5
import test9
import Test13
import test14
import test15
import test16
"""
Nel seguente codice sono riportati degli spezzoni del file demoQuickSort i quali sono mirati a testare
l'algoritmo con m specifici ossia m=2,10,20,50,300 e 500 i cui risultati verranno poi graficati 
(la scelta di m specifici è per dare un m piccolo,medio e grande ad entrambi i casi dell'algoritmo e inserire
 un numero non eccessivo di grafici nella relazione)
"""

if __name__ == "__main__":
    random.seed(2)
    # SMALL SAMPLE

    j = 1
    m = 2
    print("TESTING WITH m=", m)
    n = []
    tempo1 = []
    tempo2 = []
    tempo3 = []
    tempo4 = []
    tempo5 = []
    tempo6 = []
    tempo7 = []
    tempo8 = []
    tempo9 = []
    tempo10 = []
    tempo11 = []
    while j <= 16385:
        # while j<=32769:  # NOTA: gia con questa dimensione dell'input l'algoritmo impiega anche piu' di 60 secondi
        # percio' si puo' optare per questo while che lascia comunque apprezzare l'andamento dell'algoritmo
        A = []
        print("")
        print("TESTING WITH n=", j)
        print("")
        for i in range(0, j):
            A.append(random.randint(0, j))
        #mergeSort(A)  # queste due righe commentate servono per fare la prova con array ordinato e ordinato al contrario
        #A.reverse()
        B = A
        j = 2 * j

        # SAMPLE WITH SELECTION

        start = time()
        Test13.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo1.append(temp)
        print("Sample's median chosen with trivialSelect time -->", temp)

        A = B
        start = time()
        test14.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo2.append(temp)
        print("Sample's median chosen with heapSelect time -->", temp)

        A = B
        start = time()
        test15.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo3.append(temp)
        print("Sample's median chosen with selectRand time -->", temp)

        A = B
        start = time()
        test16.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo4.append(temp)
        print("Sample's median chosen with selectDet time -->", temp)

        # SMALL SAMPLE WITH SORTING

        A = B
        start = time()
        Test5.QuickSort(A, m)  # Sample ordered with selectionSort
        end = time()
        temp = end - start
        tempo5.append(temp)
        print("Sample sorted with selectionSort time -->", temp)

        A = B
        start = time()
        Test1.QuickSort(A, m)  # Sample ordered with inserctionSort
        end = time()
        temp = end - start
        tempo6.append(temp)
        print("Sample sorted with inserctionSort time -->", temp)

        A = B
        start = time()
        test9.QuickSort(A, m)  # Sample ordered with bubbleSort
        end = time()
        temp = end - start
        tempo7.append(temp)
        print("Sample sorted with bubbleSort time -->", temp)

        # OTHER SORTING ALGHORITMS

        A = B
        start = time()
        mergeSort(A)  # mergeSort
        end = time()
        temp = end - start
        tempo8.append(temp)
        print("Array sorted with mergeSort time-->", temp)

        A = B
        start = time()
        heapSort(A)  # heapSort
        end = time()
        temp = end - start
        tempo9.append(temp)
        print("Array sorted with heapSort time-->", temp)

        A = B
        start = time()
        quickSort(A, False)  # non-deterministic quickSort
        end = time()
        temp = end - start
        tempo10.append(temp)
        print("Array sorted with classic non-deterministic quickSort time-->", temp)

        A = B
        start = time()
        A.sort()  # pythonSort
        end = time()
        temp = end - start
        tempo11.append(temp)
        print("Array sorted with pythonSort time-->", temp)

    print("n array is", n)
    print("Sample's median chosen with trivialSelect array time -->", tempo1)
    print("Sample's median chosen with heapSelect array time -->", tempo2)
    print("Sample's median chosen with selectRand array time -->", tempo3)
    print("Sample's median chosen with selectDet array time -->", tempo4)
    print("Sample sorted with selectionSort array time -->", tempo5)
    print("Sample sorted with inserctionSort array time -->", tempo6)
    print("Sample sorted with bubbleSort classic array time -->", tempo7)
    print("Array sorted with mergeSort array time-->", tempo8)
    print("Array sorted with heapSort array time-->", tempo9)
    print("Array sorted with classic non-deterministic quickSort array time-->", tempo10)
    print("Array sorted with pythonSort array time-->", tempo11)

    j = 1
    m = 10
    print("")
    print("TESTING WITH m=", m)
    print("")
    n = []
    tempo1 = []
    tempo2 = []
    tempo3 = []
    tempo4 = []
    tempo5 = []
    tempo6 = []
    tempo7 = []
    tempo8 = []
    tempo9 = []
    tempo10 = []
    tempo11 = []
    while j <= 16385:
        # while j<=32769:  # NOTA: gia con questa dimensione dell'input l'algoritmo impiega anche piu' di 60 secondi
        # percio' si puo' optare per questo while che lascia comunque apprezzare l'andamento dell'algoritmo
        A = []
        print("")
        print("TESTING WITH n=", j)
        print("")
        for i in range(0, j):
            A.append(random.randint(0, j))
        #mergeSort(A)  # queste due righe commentate servono per fare la prova con array ordinato e ordinato al contrario
        #A.reverse()
        B = A
        j = 2 * j

        # SAMPLE WITH SELECTION

        start = time()
        Test13.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo1.append(temp)
        print("Sample's median chosen with trivialSelect time -->", temp)

        A = B
        start = time()
        test14.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo2.append(temp)
        print("Sample's median chosen with heapSelect time -->", temp)

        A = B
        start = time()
        test15.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo3.append(temp)
        print("Sample's median chosen with selectRand time -->", temp)

        A = B
        start = time()
        test16.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo4.append(temp)
        print("Sample's median chosen with selectDet time -->", temp)

        # SMALL SAMPLE WITH SORTING

        A = B
        start = time()
        Test5.QuickSort(A, m)  # Sample ordered with selectionSort
        end = time()
        temp = end - start
        tempo5.append(temp)
        print("Sample sorted with selectionSort time -->", temp)

        A = B
        start = time()
        Test1.QuickSort(A, m)  # Sample ordered with inserctionSort
        end = time()
        temp = end - start
        tempo6.append(temp)
        print("Sample sorted with inserctionSort time -->", temp)

        A = B
        start = time()
        test9.QuickSort(A, m)  # Sample ordered with bubbleSort
        end = time()
        temp = end - start
        tempo7.append(temp)
        print("Sample sorted with bubbleSort time -->", temp)

        # OTHER SORTING ALGHORITMS

        A = B
        start = time()
        mergeSort(A)  # mergeSort
        end = time()
        temp = end - start
        tempo8.append(temp)
        print("Array sorted with mergeSort time-->", temp)

        A = B
        start = time()
        heapSort(A)  # heapSort
        end = time()
        temp = end - start
        tempo9.append(temp)
        print("Array sorted with heapSort time-->", temp)

        A = B
        start = time()
        quickSort(A, False)  # non-deterministic quickSort
        end = time()
        temp = end - start
        tempo10.append(temp)
        print("Array sorted with classic non-deterministic quickSort time-->", temp)

        A = B
        start = time()
        A.sort()  # pythonSort
        end = time()
        temp = end - start
        tempo11.append(temp)
        print("Array sorted with pythonSort time-->", temp)

    print("n array is", n)
    print("Sample's median chosen with trivialSelect array time -->", tempo1)
    print("Sample's median chosen with heapSelect array time -->", tempo2)
    print("Sample's median chosen with selectRand array time -->", tempo3)
    print("Sample's median chosen with selectDet array time -->", tempo4)
    print("Sample sorted with selectionSort array time -->", tempo5)
    print("Sample sorted with inserctionSort array time -->", tempo6)
    print("Sample sorted with bubbleSort classic array time -->", tempo7)
    print("Array sorted with mergeSort array time-->", tempo8)
    print("Array sorted with heapSort array time-->", tempo9)
    print("Array sorted with classic non-deterministic quickSort array time-->", tempo10)
    print("Array sorted with pythonSort array time-->", tempo11)

    j = 1
    m = 20
    print("")
    print("TESTING WITH m=", m)
    print("")
    n=[]
    tempo1=[]
    tempo2=[]
    tempo3=[]
    tempo4=[]
    tempo5=[]
    tempo6=[]
    tempo7=[]
    tempo8=[]
    tempo9=[]
    tempo10=[]
    tempo11=[]
    while j <= 16385:
        # while j<=32769:  # NOTA: gia con questa dimensione dell'input l'algoritmo impiega anche piu' di 60 secondi
        # percio' si puo' optare per questo while che lascia comunque apprezzare l'andamento dell'algoritmo
        A = []  # in più o meno 5- secondi per variante di quickSort
        print("")
        print("TESTING WITH n=", j)
        print("")
        for i in range(0, j):
            A.append(random.randint(0, j))
        #mergeSort(A)  # queste due righe commentate servono per fare la prova con array ordinato e ordinato al contrario
        #A.reverse()
        B = A
        j = 2 * j

        # SAMPLE WITH SELECTION

        start = time()
        Test13.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo1.append(temp)
        print("Sample's median chosen with trivialSelect time -->", temp)

        A = B
        start = time()
        test14.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo2.append(temp)
        print("Sample's median chosen with heapSelect time -->", temp)

        A = B
        start = time()
        test15.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo3.append(temp)
        print("Sample's median chosen with selectRand time -->", temp)

        A = B
        start = time()
        test16.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo4.append(temp)
        print("Sample's median chosen with selectDet time -->", temp)

        # SMALL SAMPLE WITH SORTING

        A = B
        start = time()
        Test5.QuickSort(A, m)  # Sample ordered with selectionSort
        end = time()
        temp = end - start
        tempo5.append(temp)
        print("Sample sorted with selectionSort time -->", temp)

        A = B
        start = time()
        Test1.QuickSort(A, m)  # Sample ordered with inserctionSort
        end = time()
        temp = end - start
        tempo6.append(temp)
        print("Sample sorted with inserctionSort time -->", temp)

        A = B
        start = time()
        test9.QuickSort(A, m)  # Sample ordered with bubbleSort
        end = time()
        temp = end - start
        tempo7.append(temp)
        print("Sample sorted with bubbleSort time -->", temp)

        # OTHER SORTING ALGHORITMS

        A = B
        start = time()
        mergeSort(A)  # mergeSort
        end = time()
        temp = end - start
        tempo8.append(temp)
        print("Array sorted with mergeSort time-->", temp)

        A = B
        start = time()
        heapSort(A)  # heapSort
        end = time()
        temp = end - start
        tempo9.append(temp)
        print("Array sorted with heapSort time-->", temp)

        A = B
        start = time()
        quickSort(A, False)  # non-deterministic quickSort
        end = time()
        temp = end - start
        tempo10.append(temp)
        print("Array sorted with classic non-deterministic quickSort time-->", temp)

        A = B
        start = time()
        A.sort()  # pythonSort
        end = time()
        temp = end - start
        tempo11.append(temp)
        print("Array sorted with pythonSort time-->", temp)

    print("n array is", n)
    print("Sample's median chosen with trivialSelect array time -->", tempo1)
    print("Sample's median chosen with heapSelect array time -->", tempo2)
    print("Sample's median chosen with selectRand array time -->", tempo3)
    print("Sample's median chosen with selectDet array time -->", tempo4)
    print("Sample sorted with selectionSort array time -->", tempo5)
    print("Sample sorted with inserctionSort array time -->", tempo6)
    print("Sample sorted with bubbleSort classic array time -->", tempo7)
    print("Array sorted with mergeSort array time-->", tempo8)
    print("Array sorted with heapSort array time-->", tempo9)
    print("Array sorted with classic non-deterministic quickSort array time-->", tempo10)
    print("Array sorted with pythonSort array time-->", tempo11)

    # BIG SAMPLE

    j = 1
    m = 50
    print("")
    print("TESTING WITH m=", m)
    print("")
    n = []
    tempo1 = []
    tempo2 = []
    tempo3 = []
    tempo4 = []
    tempo5 = []
    tempo6 = []
    tempo7 = []
    tempo8 = []
    tempo9 = []
    tempo10 = []
    tempo11 = []
    tempo12 = []

    while j <= 16385:
        n.append(j)
        # while j<=32769:  # NOTA: gia con questa dimensione dell'input l'algoritmo impiega anche piu' di 60 secondi
        # percio' si puo' optare per questo while che lascia comunque apprezzare l'andamento dell'algoritmo
        A = []
        print("")
        print("TESTING WITH n =", j)  # in più o meno 15 secondi per variante di quickSort
        print("")
        for i in range(0, j):
            A.append(random.randint(0, j))
        #mergeSort(A)  # queste due righe commentate servono per fare la prova con array ordinato e ordinato al contrario
        #A.reverse()
        B = A
        j = 2 * j
        # SAMPLE WITH SELECTION

        start = time()
        Test13.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo1.append(temp)
        print("Sample's median chosen with trivialSelect time -->", temp)

        A = B
        start = time()
        test14.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo2.append(temp)
        print("Sample's median chosen with heapSelect time -->", temp)

        A = B
        start = time()
        test15.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo3.append(temp)
        print("Sample's median chosen with selectRand time -->", temp)

        A = B
        start = time()
        test16.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo4.append(temp)
        print("Sample's median chosen with selectDet time -->", temp)

        # HIGH SAMPLE WITH SORTING
        A = B
        start = time()
        Test1.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo5.append(temp)
        print("Sample sorted with pythonSort time -->", temp)

        A = B
        start = time()
        Test2.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo6.append(temp)
        print("Sample sorted with mergeSort time -->", temp)

        A = B
        start = time()
        Test3.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo7.append(temp)
        print("Sample sorted with quickSort classic time -->", temp)

        A = B
        start = time()
        Test4.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo8.append(temp)
        print("Sample sorted with heapSort time -->", temp)

        # OTHER SORTING ALGHORITMS

        A = B
        start = time()
        mergeSort(A)  # mergeSort
        end = time()
        temp = end - start
        tempo9.append(temp)
        print("Array sorted with mergeSort time-->", temp)

        A = B
        start = time()
        heapSort(A)  # heapSort
        end = time()
        temp = end - start
        tempo10.append(temp)
        print("Array sorted with heapSort time-->", temp)

        A = B
        start = time()
        quickSort(A, False)  # non-deterministic quickSort
        end = time()
        temp = end - start
        tempo11.append(temp)
        print("Array sorted with classic non-deterministic quickSort time-->", temp)

        A = B
        start = time()
        A.sort()  # pythonSort
        end = time()
        temp = end - start
        tempo12.append(temp)
        print("Array sorted with pythonSort time-->", temp)

    print("n array is", n)
    print("Sample's median chosen with trivialSelect array time -->", tempo1)
    print("Sample's median chosen with heapSelect array time -->", tempo2)
    print("Sample's median chosen with selectRand array time -->", tempo3)
    print("Sample's median chosen with selectDet array time -->", tempo4)
    print("Sample sorted with pythonSort array time -->", tempo5)
    print("Sample sorted with mergeSort array time -->", tempo6)
    print("Sample sorted with quickSort classic array time -->", tempo7)
    print("Sample sorted with heapSort array time -->", tempo8)
    print("Array sorted with mergeSort array time-->", tempo9)
    print("Array sorted with heapSort array time-->", tempo10)
    print("Array sorted with classic non-deterministic quickSort array time-->", tempo11)
    print("Array sorted with pythonSort array time-->", tempo12)

    j = 1
    m = 300
    print("")
    print("TESTING WITH m=", m)
    print("")
    n = []
    tempo1 = []
    tempo2 = []
    tempo3 = []
    tempo4 = []
    tempo5 = []
    tempo6 = []
    tempo7 = []
    tempo8 = []
    tempo9 = []
    tempo10 = []
    tempo11 = []
    tempo12 = []

    while j <= 16385:
        n.append(j)
        # while j<=32769:  # NOTA: gia con questa dimensione dell'input l'algoritmo impiega anche piu' di 60 secondi
        # percio' si puo' optare per questo while che lascia comunque apprezzare l'andamento dell'algoritmo
        A = []
        print("")
        print("TESTING WITH n =", j)  # in più o meno 15 secondi per variante di quickSort
        print("")
        for i in range(0, j):
            A.append(random.randint(0, j))
        #mergeSort(A)  # queste due righe commentate servono per fare la prova con array ordinato e ordinato al contrario
        #A.reverse()
        B = A
        j = 2 * j
        # SAMPLE WITH SELECTION

        start = time()
        Test13.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo1.append(temp)
        print("Sample's median chosen with trivialSelect time -->", temp)

        A = B
        start = time()
        test14.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo2.append(temp)
        print("Sample's median chosen with heapSelect time -->", temp)

        A = B
        start = time()
        test15.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo3.append(temp)
        print("Sample's median chosen with selectRand time -->", temp)

        A = B
        start = time()
        test16.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo4.append(temp)
        print("Sample's median chosen with selectDet time -->", temp)

        # HIGH SAMPLE WITH SORTING
        A = B
        start = time()
        Test1.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo5.append(temp)
        print("Sample sorted with pythonSort time -->", temp)

        A = B
        start = time()
        Test2.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo6.append(temp)
        print("Sample sorted with mergeSort time -->", temp)

        A = B
        start = time()
        Test3.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo7.append(temp)
        print("Sample sorted with quickSort classic time -->", temp)

        A = B
        start = time()
        Test4.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo8.append(temp)
        print("Sample sorted with heapSort time -->", temp)

        # OTHER SORTING ALGHORITMS

        A = B
        start = time()
        mergeSort(A)  # mergeSort
        end = time()
        temp = end - start
        tempo9.append(temp)
        print("Array sorted with mergeSort time-->", temp)

        A = B
        start = time()
        heapSort(A)  # heapSort
        end = time()
        temp = end - start
        tempo10.append(temp)
        print("Array sorted with heapSort time-->", temp)

        A = B
        start = time()
        quickSort(A, False)  # non-deterministic quickSort
        end = time()
        temp = end - start
        tempo11.append(temp)
        print("Array sorted with classic non-deterministic quickSort time-->", temp)

        A = B
        start = time()
        A.sort()  # pythonSort
        end = time()
        temp = end - start
        tempo12.append(temp)
        print("Array sorted with pythonSort time-->", temp)

    print("n array is", n)
    print("Sample's median chosen with trivialSelect array time -->", tempo1)
    print("Sample's median chosen with heapSelect array time -->", tempo2)
    print("Sample's median chosen with selectRand array time -->", tempo3)
    print("Sample's median chosen with selectDet array time -->", tempo4)
    print("Sample sorted with pythonSort array time -->", tempo5)
    print("Sample sorted with mergeSort array time -->", tempo6)
    print("Sample sorted with quickSort classic array time -->", tempo7)
    print("Sample sorted with heapSort array time -->", tempo8)
    print("Array sorted with mergeSort array time-->", tempo9)
    print("Array sorted with heapSort array time-->", tempo10)
    print("Array sorted with classic non-deterministic quickSort array time-->", tempo11)
    print("Array sorted with pythonSort array time-->", tempo12)

    j = 1
    m = 500
    print("")
    print("TESTING WITH m=", m)
    print("")
    n=[]
    tempo1 = []
    tempo2 = []
    tempo3 = []
    tempo4 = []
    tempo5 = []
    tempo6 = []
    tempo7 = []
    tempo8 = []
    tempo9 = []
    tempo10 = []
    tempo11 = []
    tempo12 = []


    while j <= 16385:
        n.append(j)
        # while j<=32769:  # NOTA: gia con questa dimensione dell'input l'algoritmo impiega anche piu' di 60 secondi
        # percio' si puo' optare per questo while che lascia comunque apprezzare l'andamento dell'algoritmo
        A = []
        print("")
        print("TESTING WITH n =", j)  # in più o meno 15 secondi per variante di quickSort
        print("")
        for i in range(0, j):
            A.append(random.randint(0, j))
        #mergeSort(A)  # queste due righe commentate servono per fare la prova con array ordinato e ordinato al contrario
        #A.reverse()
        B = A
        j = 2 * j
        # SAMPLE WITH SELECTION

        start = time()
        Test13.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo1.append(temp)
        print("Sample's median chosen with trivialSelect time -->", temp)

        A = B
        start = time()
        test14.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo2.append(temp)
        print("Sample's median chosen with heapSelect time -->", temp)

        A = B
        start = time()
        test15.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo3.append(temp)
        print("Sample's median chosen with selectRand time -->", temp)

        A = B
        start = time()
        test16.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo4.append(temp)
        print("Sample's median chosen with selectDet time -->", temp)

        # HIGH SAMPLE WITH SORTING
        A = B
        start = time()
        Test1.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo5.append(temp)
        print("Sample sorted with pythonSort time -->", temp)

        A = B
        start = time()
        Test2.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo6.append(temp)
        print("Sample sorted with mergeSort time -->", temp)

        A = B
        start = time()
        Test3.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo7.append(temp)
        print("Sample sorted with quickSort classic time -->", temp)

        A = B
        start = time()
        Test4.QuickSort(A, m)
        end = time()
        temp = end - start
        tempo8.append(temp)
        print("Sample sorted with heapSort time -->", temp)

        # OTHER SORTING ALGHORITMS

        A = B
        start = time()
        mergeSort(A)  # mergeSort
        end = time()
        temp = end - start
        tempo9.append(temp)
        print("Array sorted with mergeSort time-->", temp)

        A = B
        start = time()
        heapSort(A)  # heapSort
        end = time()
        temp = end - start
        tempo10.append(temp)
        print("Array sorted with heapSort time-->", temp)

        A = B
        start = time()
        quickSort(A, False)  # non-deterministic quickSort
        end = time()
        temp = end - start
        tempo11.append(temp)
        print("Array sorted with classic non-deterministic quickSort time-->", temp)

        A = B
        start = time()
        A.sort()  # pythonSort
        end = time()
        temp = end - start
        tempo12.append(temp)
        print("Array sorted with pythonSort time-->", temp)

    print("n array is",n)
    print("Sample's median chosen with trivialSelect array time -->", tempo1)
    print("Sample's median chosen with heapSelect array time -->", tempo2)
    print("Sample's median chosen with selectRand array time -->", tempo3)
    print("Sample's median chosen with selectDet array time -->", tempo4)
    print("Sample sorted with pythonSort array time -->", tempo5)
    print("Sample sorted with mergeSort array time -->", tempo6)
    print("Sample sorted with quickSort classic array time -->", tempo7)
    print("Sample sorted with heapSort array time -->", tempo8)
    print("Array sorted with mergeSort array time-->", tempo9)
    print("Array sorted with heapSort array time-->", tempo10)
    print("Array sorted with classic non-deterministic quickSort array time-->", tempo11)
    print("Array sorted with pythonSort array time-->", tempo12)

