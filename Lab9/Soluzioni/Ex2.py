def Ex2(file):
    f = open(file,encoding = 'UTF-8')
    d = {}
    numero = 1
    for riga in f:
        lista = riga.strip().split()
        for elem in lista:
            if elem in d:
                d[elem].add(numero)
            else:
                d[elem] = {numero}
        numero += 1
    return d 

     
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex2, ['testo1.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2}, 'al': {1}, 'lardo': {1}, 'che': {1}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1, 3}})
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2, 4}, 'al': {1}, 'lardo': {1}, 'che': {1}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1, 3, 4}})
    counter_test_positivi += tester_fun(Ex2, ['testo3.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2, 4}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1, 3, 4}})
    counter_test_positivi += tester_fun(Ex2, ['testo4.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2, 4}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1}, 'zampone': {3}, 'zampina': {4}})
    counter_test_positivi += tester_fun(Ex2, ['testo5.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2, 4}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1}, 'zampone': {3, 6}, 'zampina': {4}, 'palla': {5}})

    counter_test_positivi += tester_fun(Ex2, ['testo6.txt'] , {'tanto': {1}, 'va': {1}, 'la': {1}, 'gatta': {1, 4}, 'lascia': {3}, 'lo': {3}, 'zampone': {3, 6}, 'zampina': {4}, 'palla': {5}})
    counter_test_positivi += tester_fun(Ex2, ['testo7.txt'] , {'tanto': {1}, 'va': {1}, 'la': {1}, 'gatta': {1, 4}, 'lascia': {3}, 'lo': {3}, 'zampone': {3, 6}, 'zampina': {4}, 'palla': {5, 6}})
    counter_test_positivi += tester_fun(Ex2, ['testo8.txt'] , {'tanto': {1}, 'va': {1}, 'la': {1}, 'gatta': {1, 4}, 'lascia': {3}, 'lo': {3}, 'zampone': {3, 6}, 'palla': {4, 5, 6}, 'zampina': {4}})
    counter_test_positivi += tester_fun(Ex2, ['testo9.txt'] , {'tanto': {1}, 'va': {1}, 'la': {1}, 'gatta': {1, 4}, 'lascia': {8, 3}, 'lo': {3}, 'zampone': {3, 7}, 'palla': {4, 5, 7}, 'zampina': {4}})
    counter_test_positivi += tester_fun(Ex2, ['testo10.txt'] , {'tanto': {1}, 'va': {1}, 'la': {1}, 'gatta': {1, 4}, 'lascia': {8, 3}, 'lo': {3}, 'zampone': {3, 7}, 'palla': {4, 5, 7}, 'zampina': {4}, 'casa': {8, 10}})

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
