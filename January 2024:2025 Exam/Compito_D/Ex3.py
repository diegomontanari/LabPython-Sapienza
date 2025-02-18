def Ex3(nomeFile,anno):  
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

                
###############################################################################
#nomeFile='m1.csv'
"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5


    counter_test_positivi += tester_fun(Ex3, ['eventi1.csv',2022],{'Concerto'})
    counter_test_positivi += tester_fun(Ex3, ['eventi1.csv',2021],{'Concerto'})
    counter_test_positivi += tester_fun(Ex3, ['eventi1.csv',2020],{'Sport'})
    counter_test_positivi += tester_fun(Ex3, ['eventi1.csv',2019],set())
    counter_test_positivi += tester_fun(Ex3, ['eventi2.csv',2022],{'Concerto', 'Sport', 'Teatro'})

     
    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
