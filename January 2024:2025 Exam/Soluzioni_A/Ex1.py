def Ex1(l,n):
    maxlung = 0
    ris = (-1,-1)
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            lista = l[i:j+1]
            minimo = min(lista)
            massimo = max(lista)
            if massimo - minimo <= n and len(lista) > maxlung:
                maxlung = len(lista)
                ris = (i,j)
    return ris
    

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione


    counter_test_positivi += tester_fun(Ex1, [[3, 5, 7, 2, 8],4 ],(0,2))
    counter_test_positivi += tester_fun(Ex1, [ [],2],(-1,-1))
    counter_test_positivi += tester_fun(Ex1, [ [9, 3, 5, 5, 2, 8], 4 ],(1,4))
    counter_test_positivi += tester_fun(Ex1, [[-3, 1],4 ],(0,1))
    counter_test_positivi += tester_fun(Ex1, [[3, 5, 7, 2, 8],100 ],(0,4))
 
    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex1, [ [8],2],(-1,-1))
    counter_test_positivi += tester_fun(Ex1, [ [18,12,6,0],5],(-1,-1))
    counter_test_positivi += tester_fun(Ex1, [ [18,12,6,1],5],(2,3))
    counter_test_positivi += tester_fun(Ex1, [ [18,-18,12,-12,2,-2],4],(4,5))
    counter_test_positivi += tester_fun(Ex1, [ [18,-18],18],(-1,-1))
    #counter_test_positivi += tester_fun(Ex1, [ [2],3],(0,0))
    #counter_test_positivi += tester_fun(Ex1, [ [2,3],3],(0,0))
    
    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
