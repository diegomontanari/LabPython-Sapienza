# Dato che questo esercizio è complesso, è intelligente separare il codice in 2 frammenti più piccoli.
# -> Per prima cosa, salviamo i dati in una struttura, poi lavoriamo sull'elaborazione dell'output.

def Ex3(file, partenza, n):
    d = {}
    with open(file, 'r', encoding='UTF-8') as f:
        # Fase di lettura dati
        for i in f:
            riga = i.strip().split(',')
            d[(riga[0], riga[1])] = (int(riga[2]), int(riga[3]))  # Converti i valori numerici

    # Fase elaborazione output
    max_distanza = -1
    migliore_citta = 'nessuna'
    
    for (citta_partenza, citta_arrivo), (distanza_andata, tempo_andata) in d.items():
        if citta_partenza == partenza and (citta_arrivo, citta_partenza) in d:
            distanza_ritorno, tempo_ritorno = d[(citta_arrivo, citta_partenza)]
            tempo_totale = tempo_andata + tempo_ritorno
            distanza_max = max(distanza_andata, distanza_ritorno)
            
            if tempo_totale <= n:
                if distanza_max > max_distanza or (distanza_max == max_distanza and citta_arrivo < migliore_citta):
                    max_distanza = distanza_max
                    migliore_citta = citta_arrivo
    
    return migliore_citta


        







                



###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""
if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['viaggi1.csv','roma',400],'milano')
    counter_test_positivi += tester_fun(Ex3, ['viaggi2.csv','roma',350],'napoli')
    counter_test_positivi += tester_fun(Ex3, ['viaggi3.csv','roma',350],'firenze')
    counter_test_positivi += tester_fun(Ex3, ['viaggi4.csv','roma',350],'nessuna')
    counter_test_positivi += tester_fun(Ex3, ['viaggi5.csv','roma',350],'nessuna')
    
    
    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
