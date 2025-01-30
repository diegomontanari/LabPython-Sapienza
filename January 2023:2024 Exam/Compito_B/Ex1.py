def Ex1(l):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [ ['oro','mio','alla','mio','ara','mio']],1)
    counter_test_positivi += tester_fun(Ex1, [ []],-1)
    counter_test_positivi += tester_fun(Ex1, [ ['allegra brigata','b','c','f','elemento soave','e','f']],1)
    counter_test_positivi += tester_fun(Ex1, [ ['ioi','mioo','tuu','ioo','il','i']],0)
    counter_test_positivi += tester_fun(Ex1, [ ['oo','a','ii']],1)

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
