def Ex1(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [ [352,300,52,49,1,2,2]],2)
    counter_test_positivi += tester_fun(Ex1, [ [352,352,52,53,54,55]],1)
    counter_test_positivi += tester_fun(Ex1, [ []],-1)
    counter_test_positivi += tester_fun(Ex1, [ [5]],0)
    counter_test_positivi += tester_fun(Ex1, [ [8,2,2,9]],1)
    
    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
