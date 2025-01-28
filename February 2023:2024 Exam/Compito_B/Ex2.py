def Ex2(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, ['testob1.txt'],2)
    counter_test_positivi += tester_fun(Ex2, ['testob2.txt'],1)
    counter_test_positivi += tester_fun(Ex2, ['testob3.txt'],0)
    counter_test_positivi += tester_fun(Ex2, ['testob4.txt'],1)
    counter_test_positivi += tester_fun(Ex2, ['testob5.txt'],2)
    
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
