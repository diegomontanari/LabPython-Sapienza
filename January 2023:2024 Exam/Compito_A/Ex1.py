def Ex1(l):    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""###############################################################################"""NON MODIFICARE IL CODICE (codice di test della funzione)"""if __name__ == '__main__':    from tester import tester_fun    counter_test_positivi = 0    total_tests = 5    # test distribuzione    counter_test_positivi += tester_fun(Ex1, [ ['io','mio','tu','mio','il','mio']],1)    counter_test_positivi += tester_fun(Ex1, [ []],-1)    counter_test_positivi += tester_fun(Ex1, [ ['a','b','c','d','e','f']],3)    counter_test_positivi += tester_fun(Ex1, [ ['io','mio','tuo','io','il','i']],0)    counter_test_positivi += tester_fun(Ex1, [ ['io','a','il']],1)           print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)