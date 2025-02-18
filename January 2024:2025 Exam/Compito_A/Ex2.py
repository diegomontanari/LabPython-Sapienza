"""
1.	Calcola la lunghezza della parola.
2.	Se non esiste ancora una voce per quella lunghezza, aggiungi la parola.
3.	Se esiste già una parola per quella lunghezza, confronta quella che hai già con la parola corrente; se la parola corrente è alfabeticamente maggiore, sostituiscila.
"""
def Ex2(file):
    d = {}
    with open(file, 'r', encoding='UTF-8') as f:
        fil = f.read().strip().split()
        for word in fil:
            lw = len(word)
            if lw not in d:
                d[lw] = word
            else: # se lw è già una chiave, quindi se ha la stessa lunghezza
                if word > d[lw]: # Sono entrambi stringhe, se l'ultima maggiore della vecchia
                    d[lw] = word  # Aggiorna con la nuova parola
    return d

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, ['testoa1.txt'],{5: 'tanto', 2: 'va', 3: 'chi', 6: 'lascia', 7: 'zampino', 1: 'l', 4: 'roma', 8: 'poltrona'})    
    counter_test_positivi += tester_fun(Ex2, ['testoa2.txt'],{5: 'tanto', 2: 'va', 3: 'chi', 6: 'lascia', 7: 'zampino', 1: 'l', 4: 'sano', 8: 'poltrona'})   
    counter_test_positivi += tester_fun(Ex2, ['testoa3.txt'],{4: 'vero', 3: 'uno', 1:'e'})   
    counter_test_positivi += tester_fun(Ex2, ['testoa4.txt'],{}) 
    counter_test_positivi += tester_fun(Ex2, ['testoa5.txt'],{6: 'sembra', 5: 'molto', 3: 'non', 9: 'difficile', 2: 'mi', 7: 'sbaglio'})
    
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
