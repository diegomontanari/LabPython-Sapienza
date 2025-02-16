def Ex6(fileName):
    f=open(fileName,"r",encoding="UTF-8")
    d = {}
    j=1
    for riga in f:
        lista = riga.strip().split(',')
        for i in range(len(lista)):
            numero = int(lista[i])
            if numero in d:
                d[numero].add(j)
            else:
                d[numero] = set()
                d[numero].add(j)
        j=j+1
    f.close()
    return d 

 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex6, ['numeri1.txt'] , {10: {1,2}, -5: {1,2}, 0: {1}, 8: {2}, -3: {2}})
    counter_test_positivi += tester_fun(Ex6, ['numeri2.txt'] , {10: {1,2}, 0: {2}})
    counter_test_positivi += tester_fun(Ex6, ['numeri3.txt'] , {3: {1,2}, 4: {1}, 5: {1}, 2: {2,3}, 0: {2,3}})
    counter_test_positivi += tester_fun(Ex6, ['numeri4.txt'] , {2: {1,2,3,4,5}, 1: {1,2,6}, 3: {6}})
    counter_test_positivi += tester_fun(Ex6, ['numeri5.txt'] , {})

    counter_test_positivi += tester_fun(Ex6, ['numeri6.txt'] , {1: {1, 3}, -1: {2, 3}})
    counter_test_positivi += tester_fun(Ex6, ['numeri7.txt'] , {1: {1, 2, 3, 4}, 2: {1, 2, 3, 4}, 3: {1, 2, 3, 4}})
    counter_test_positivi += tester_fun(Ex6, ['numeri8.txt'] , {1: {1, 5}, -1: {1, 2}, 10: {3}, 15: {3}, -100: {3}, 40: {3, 4}, -40: {4}, 90: {5}, 20: {5}})
    counter_test_positivi += tester_fun(Ex6, ['numeri9.txt'] , {0: {1, 2, 3}, -1: {1, 2, 3}})
    counter_test_positivi += tester_fun(Ex6, ['numeri10.txt'] , {1: {1}, 2: {1}, 3: {1}, 4: {1}, 5: {1}, 6: {1}})

    print('La funzione',Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)