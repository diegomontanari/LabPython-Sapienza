def Ex2(file):
    x = set()
    max_dist = 0
    with open(file, 'r', encoding='UTF-8') as f:
        parole = f.read().strip().split() # Ho una lista di parole perché ho usato split()

        for parola in parole:  # Iteriamo direttamente sulle parole
            for i in range(len(parola)):  # Indice del primo carattere
                if parola[i] == 'a':
                    for j in range(i + 1, len(parola)): # Indice del secondo carattere
                        if parola[j] == 'a':
                            dist = j - i - 1 # GENIALE (!!) non ci avevo pensato
                            if dist >= max_dist:
                                max_dist = dist
                                x.add(parola)
    return x




                            
# DA QUESTO ESERCIZIO HO CAPITO CHE:

    #-> 1) Dare il giusto nome ai contatori ti SALVA
    #-> 2) Sapere se stai iterando su tutti indici o su tutte stringhe è FONDAMENTALE
    #-> 3) Fondamentale saper ragionare algebricamente: DISTANZA tra 2 elementi ti dovrebbe
    #      immediatamente far pensare a DIFFERENZA DEGLI INDICI.








            




###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, ['testoa1.txt'],{'cassata','sassata'})    
    counter_test_positivi += tester_fun(Ex2, ['testoa2.txt'],set())   
    counter_test_positivi += tester_fun(Ex2, ['testoa3.txt'],{'cassa','massa'})   
    counter_test_positivi += tester_fun(Ex2, ['testoa4.txt'],{'aaa','aba','aca'}) 
    counter_test_positivi += tester_fun(Ex2, ['testoa5.txt'],{'aaaa'}) 
    
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
