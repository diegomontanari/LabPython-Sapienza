def Ex2(file):
    d = {}
    num_riga = 1
    with open(file, 'r', encoding='UTF-8') as f:
        for riga in f:
            lista = riga.strip().split()  # Rimuove gli spazi bianchi all'inizio e alla fine della riga e divide la riga in una lista di parole
            for elem in lista:
                if elem in d:
                    d[elem].add(num_riga) # I set non conengono duplicati quindi se stessa riga non viene ri-aggiunto
                else:
                    d[elem] = {num_riga}
        num_riga += 1
    return d 

    
     
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex2, ['testo1.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2}, 'al': {1}, 'lardo': {1}, 'che': {1}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1, 3}})
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2, 4}, 'al': {1}, 'lardo': {1}, 'che': {1}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1, 3, 4}})
    counter_test_positivi += tester_fun(Ex2, ['testo3.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2, 4}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1, 3, 4}})
    counter_test_positivi += tester_fun(Ex2, ['testo4.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2, 4}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1}, 'zampone': {3}, 'zampina': {4}})
    counter_test_positivi += tester_fun(Ex2, ['testo5.txt'] , {'tanto': {1, 2}, 'va': {1, 2}, 'la': {1, 2}, 'gatta': {1, 2, 4}, 'ci': {1}, 'lascia': {1, 3}, 'lo': {1, 3}, 'zampino': {1}, 'zampone': {3, 6}, 'zampina': {4}, 'palla': {5}})

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
