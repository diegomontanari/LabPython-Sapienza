def Ex1(s,n):
    maxlung = 0
    ris = (-1,-1)
    ll=[]
    for p in s:
        ll.append(len(p))  
    for i in range(len(ll)):
        for j in range(i+1,len(ll)):
            lista = ll[i:j+1]
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

    counter_test_positivi += tester_fun(Ex1, [['tanto', 'va', 'la', 'gatta', 'al', 'lardo', 'che', 'ci', 'lascia', 'lo', 'zampino'],2],(1,2))
    counter_test_positivi += tester_fun(Ex1, [['tanto', 'va', 'la', 'gatta', 'al', 'lardo', 'che', 'ci', 'lascia', 'lo', 'zampino'],4],(0, 9))
    counter_test_positivi += tester_fun(Ex1, [['questi', 'esercizi', 'sembrano', 'facili'],0],(1, 2))
    counter_test_positivi += tester_fun(Ex1, [['questi', 'esercizi', 'sembrerebbero', 'facili'],1],(-1,-1))
    counter_test_positivi += tester_fun(Ex1, [['questi', 'esercizi', 'sembrano', 'facili'],1],(1, 2))
 
    
    # test aggiuntivi
    
    counter_test_positivi += tester_fun(Ex1, [['nel', 'mezzo', 'del', 'cammin', 'di', 'nostra', 'vita'],1],(-1, -1))
    counter_test_positivi += tester_fun(Ex1, [['nel', 'mezzo', 'del', 'cammin', 'di', 'nostra', 'vita'],3],(0, 3))
    counter_test_positivi += tester_fun(Ex1, [['Notevole', 'esempio', 'di', 'lista', 'di', 'stringhe'],2],(0, 1))
    counter_test_positivi += tester_fun(Ex1, [['Notevole', 'esempio', 'di', 'lista', 'di', 'stringhe'],3],(2, 4))
    counter_test_positivi += tester_fun(Ex1, [['Notevole'],0],(-1, -1))

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
