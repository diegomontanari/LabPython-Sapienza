def Ex9(s1,s2):
    
        

"""Ex9(s1,s2) Scrivere una funzione che riceve in ingresso due
stringhe s1 ed s2 e calcola la lunghezza della più lunga
sottosequenza comune alle due stringhe."""
   

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
if __name__ == '__main__':
    from tester import tester_fun
    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione
  
    counter_test_positivi += tester_fun(Ex9, ['casa','cappello'], 2)
    counter_test_positivi += tester_fun(Ex9, ['carcassa','cassapanca'], 5)
    counter_test_positivi += tester_fun(Ex9, ['sorpasso','passo e sorpasso'], 8)
    counter_test_positivi += tester_fun(Ex9, ['casa',''], 0)
    counter_test_positivi += tester_fun(Ex9, ['a','a'], 1)



    print('La funzione',Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
    
