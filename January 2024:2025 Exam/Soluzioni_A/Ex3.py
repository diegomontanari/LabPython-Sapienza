def Ex3(file, partenza, n):
    with open(file, 'r', encoding='UTF-8') as f:
        dest = {}
        arrivi = {}
        for riga in f:
            dati = riga.strip().split(',')
            if dati[0] == partenza:
                dest[dati[1]] = [int(dati[2]),int(dati[3])] # Dict con chiave dest e valori distanza e tempo
            if dati[1] == partenza:
                arrivi[dati[0]] = [int(dati[2]),int(dati[3])] # Dict con chiave arrivi e valori distanza e tempo
        ris = 'nessuna'

        maxdist = 0
        for citta in dest:
            if citta in arrivi: # Quindi se esiste anche il viaggio di ritorno
                tempo = dest[citta][1]+ arrivi[citta][1] # Calcola il tempo sommato di partenza + arrivo
                dista = max(dest[citta][0], arrivi[citta][0]) # Il testo chiede solo la città più lontana raggiungibile
                if tempo <= n and dista > maxdist:
                    ris = citta
                    maxdist=dista
                if tempo <= n and dista == maxdist and  citta < ris: # citta<ris è un confronto alfabetico (gestisco il caso di parità)
                    ris = citta
    return ris

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['viaggi1.csv','roma',400],'milano')
    counter_test_positivi += tester_fun(Ex3, ['viaggi2.csv','roma',350],'napoli')
    counter_test_positivi += tester_fun(Ex3, ['viaggi3.csv','roma',350],'napoli')
    counter_test_positivi += tester_fun(Ex3, ['viaggi4.csv','roma',350],'nessuna')
    counter_test_positivi += tester_fun(Ex3, ['viaggi5.csv','roma',350],'nessuna')

    

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex3, ['viaggi6.csv','roma',400],'milano')
    counter_test_positivi += tester_fun(Ex3, ['viaggi7.csv','roma',350],'firenze')
    counter_test_positivi += tester_fun(Ex3, ['viaggi8.csv','roma',300],'firenze')
    counter_test_positivi += tester_fun(Ex3, ['viaggi9.csv','roma',400],'milano')
    counter_test_positivi += tester_fun(Ex3, ['viaggi10.csv','roma',300],'siena')

    
    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
