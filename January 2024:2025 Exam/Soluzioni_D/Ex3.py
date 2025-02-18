def Ex3(nomeFile,anno):    
    f = open(nomeFile,'r', encoding='UTF8')
    eventiAnno ={}
    for riga in f:
        dati = riga.strip().split(',')
        anno0=int(dati[2])
        nome=dati[0]
        evento=dati[1]
        if anno0 == anno:
            if nome in eventiAnno:
                eventiAnno[nome].add(evento)
            else:
                eventiAnno[nome]={evento}
    fatti=list(eventiAnno.values())
    inComune=set()
    if len(fatti)>0:
        inComune=fatti[0]
        for s in fatti[1:]:
            inComune.intersection_update(s)
    return inComune

 
     
    print(eventiAnno)
                
###############################################################################
#nomeFile='m1.csv'
"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['eventi1.csv',2022],{'Concerto'})
    counter_test_positivi += tester_fun(Ex3, ['eventi1.csv',2021],{'Concerto'})
    counter_test_positivi += tester_fun(Ex3, ['eventi1.csv',2020],{'Sport'})
    counter_test_positivi += tester_fun(Ex3, ['eventi1.csv',2019],set())
    counter_test_positivi += tester_fun(Ex3, ['eventi2.csv',2022],{'Concerto', 'Sport', 'Teatro'})
    
    counter_test_positivi += tester_fun(Ex3, ['eventi2.csv',2021],{'Mostra'})
    counter_test_positivi += tester_fun(Ex3, ['eventi3.csv',2022],set())
    counter_test_positivi += tester_fun(Ex3, ['eventi1.csv',2000],set())
    counter_test_positivi += tester_fun(Ex3, ['eventi4.csv',2000],{'Sport'})
    counter_test_positivi += tester_fun(Ex3, ['eventi5.csv',2000],{'Mostra'})
     
    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
