import numpy as np

def Ex3(file,n):
    pos = {}
    with open(file, 'r', encoding='UTF-8') as f:
        giocatori = f.readline().strip().split(',')
        for nome in giocatori:
            pos[nome] = 0 # Inizializzare i giocatori a posizione 0
    ar = np.loadtxt(file, delimiter=',')
    for turno in ar:
        for i in range(len(turno)): # for i in turno non va bene perché mi serve l'indice, non l'elemento e basta.
            tiro = int(turno[i]) # (Brilliant!!)
            giocatore = giocatori[i] # (Brilliant!!) Così accoppio il giocatore al suo lancio, usando lo stesso contatore!
            fermo = False
            if pos[giocatore] + tiro == n:
                return giocatore
            if pos[giocatore] + tiro < n:
                for altro in giocatori:
                    if altro != giocatore and pos[altro] == pos[giocatore] + tiro: # {if altro != giocatore} Per evitare di confrontare il giocatore con sé stesso
                        fermo=True                  
            if pos[giocatore] + tiro > n:
                fermo=True
            if not fermo:
                pos[giocatore] = pos[giocatore] + tiro
    return 'Nessuno'      
                   
             




             

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    # counter_test_positivi += tester_fun(Ex3, ['mosse1.csv',10],'Paolo')    
    # counter_test_positivi += tester_fun(Ex3, ['mosse1.csv',8],'Miriam')    
    # counter_test_positivi += tester_fun(Ex3, ['mosse2.csv',10],'Paolo')    
    # counter_test_positivi += tester_fun(Ex3, ['mosse2.csv',9],'Flavio')    
    # counter_test_positivi += tester_fun(Ex3, ['mosse2.csv',7],'Paolo')  
    counter_test_positivi += tester_fun(Ex3, ['mosse1.csv',10],'Paolo')    
    counter_test_positivi += tester_fun(Ex3, ['mosse1.csv',8],'Nessuno')    
    counter_test_positivi += tester_fun(Ex3, ['mosse2.csv',10],'Paolo')    
    counter_test_positivi += tester_fun(Ex3, ['mosse2.csv',9],'Flavio')    
    counter_test_positivi += tester_fun(Ex3, ['mosse2.csv',7],'Paolo')         
    
    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

