#INFO ABOUT np.load.txt()
    #-> np.load.txt(fileName, delimeter=",") reads and already creates the NumPy array.
#BUT:
    #-> If you have a string and not integers, you need to use np.getfromtxt and choose the dtype...
    #->... Like this: np.genfromtxt('testob1.txt', delimiter='\n', dtype=str)
#HIM BUT BETTER
    #->  gen(generalized)fromtxt is the same but for more data types
    #->  If you have mixed data types (e.g., integers+strings), you can set dtype=None to let NumPy automatically determine the appropriate data type.

def Ex3(nomeFile):
    import pandas as pd
    import numpy as np
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""


###############################################################################
#nomeFile='m1.csv'
"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione
    counter_test_positivi += tester_fun(Ex3, ['m1.csv'],{0,2})
    counter_test_positivi += tester_fun(Ex3, ['m2.csv'],{4})
    counter_test_positivi += tester_fun(Ex3, ['m3.csv'],{0,1,2,3,4})
    counter_test_positivi += tester_fun(Ex3, ['m4.csv'],{1})
    counter_test_positivi += tester_fun(Ex3, ['m5.csv'],{0,1,2})    

    
    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
