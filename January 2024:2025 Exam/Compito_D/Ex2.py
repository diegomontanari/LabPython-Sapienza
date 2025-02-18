def Ex2(nomeFile):

    ris = {}

    with open(nomeFile, 'r', encoding='UTF-8') as f:
        for r in f:
            r = r.strip().split()  # Divido la riga in parole
            for i in range(len(r) - 1):  # Itero su ogni parola
                for j in range(i + 1, len(r)):  # Confronto la parola i con le parole successive
                    if len(r[i]) == len(r[j]):  # Se le lunghezze sono uguali
                        if len(r[i]) in ris:
                            ris[len(r[i])].add(r[i])  # Aggiungi r[i] al set
                            ris[len(r[i])].add(r[j])  # Aggiungi r[j] al set
                        else:
                            ris[len(r[i])] = {r[i], r[j]}  # Inizializza il set con entrambe le parole

    return ris


###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5


    counter_test_positivi += tester_fun(Ex2, ['testod1.txt'],{5: {'vanno', 'lardo', 'tanto', 'gatti'}, 2: {'ci', 'al'}, 3: {'che', 'gli'}, 11: {'pascolavano', 'superlativi'}})    
    counter_test_positivi += tester_fun(Ex2, ['testod2.txt'],{6: {'questo', 'noioso', 'sembra'}, 9: {'veramente', 'esercizio'}, 2: {'ma', 'lo'}, 4: {'fare', 'devo'}})   
    counter_test_positivi += tester_fun(Ex2, ['testod3.txt'],{3: {'sia', 'che', 'non', 'mai'}, 6: {'questo', 'quanto', 'noioso'}, 9: {'risolvere', 'esercizio'}, 10: {'concepirlo', 'soffermati'}})
    counter_test_positivi += tester_fun(Ex2, ['testod4.txt'],{3: {'sei', 'zio', 'mio', 'uno', 'tre', 'due'}})
    counter_test_positivi += tester_fun(Ex2, ['testod5.txt'],{})

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
