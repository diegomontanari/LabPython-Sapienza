# POWERFUL USE OF min() max() functions:
    #-> max(iterable, key, default) the last 2 arguments are optional
    #-> default is easy to understand, key applied a rule to each element of the iterable
    #-> see the code down below to see an example

def Ex1(s, n):
    maxsub = []         # Sottosequenza migliore trovata
    start, end = -1, -1  # Indici iniziali e finali della sottosequenza migliore

    # Iteriamo sugli indici di inizio
    for i in range(len(s)):
        # La sottosequenza deve avere almeno 2 parole: j va da i+1 a len(s)-1
        for j in range(i+1, len(s)):
            subseq = s[i:j+1]
            # Calcoliamo la differenza tra la lunghezza della parola più lunga
            # e quella della parola più corta nella sottosequenza.
            diff = len(max(subseq, key=len)) - len(min(subseq, key=len))
            # Se la differenza è minore o uguale a n e la sottosequenza è più lunga
            if diff <= n and len(subseq) > len(maxsub):
                maxsub = subseq
                start, end = i, j

    # Se abbiamo trovato almeno una sottosequenza valida (minimo 2 parole)
    if len(maxsub) >= 2:
        return start, end
    else:
        return -1, -1

# QUICK INFO:
    #-> max(subseq, key=len) returns the longest string in the list. But this cannot work,
    #-> as it DOESN'T MAKE SENSE to SUBTRACT TWO STRINGS, which will happen if i also compute min(subseq, key=len)
    #-> using len(max(subseq, key=len)) is the RIGHT APPROACH as i'm subtracting two integers.
    

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [['tanto', 'va', 'la', 'gatta', 'al', 'lardo', 'che', 'ci', 'lascia', 'lo', 'zampino'],2],(1,2))
    counter_test_positivi += tester_fun(Ex1, [['tanto', 'va', 'la', 'gatta', 'al', 'lardo', 'che', 'ci', 'lascia', 'lo', 'zampino'],4],(0, 9))
    counter_test_positivi += tester_fun(Ex1, [['questi', 'esercizi', 'sembrano', 'facili'],0],(1, 2))
    counter_test_positivi += tester_fun(Ex1, [['questi', 'esercizi', 'smbrerebbero', 'facili'],1],(-1,-1))
    counter_test_positivi += tester_fun(Ex1, [['questi', 'esercizi', 'sembrano', 'facili'],1],(1, 2))


    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
