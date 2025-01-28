def Ex3(nomeFile):
    import pandas as pd
    import numpy as np
    
    csv = pd.read_csv(fileName, header="intestazione")
    ar = np.array(csv.values)
    shape = ar.shape
    rows = shape[0]
    columns = shape[1]
    res = set()
    maxRoad = 0
    zig = 1 #zig-> We go down; zag -> We go right (zig+zag = diagonal)
    
    for i in range(1, rows-1): #iteration on the "middle" rows
        


    

 
###############################################################################
nomeFile='m1.csv'
"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['m1.csv'],{1})
    counter_test_positivi += tester_fun(Ex3, ['m2.csv'],set())
    counter_test_positivi += tester_fun(Ex3, ['m3.csv'],{2})
    counter_test_positivi += tester_fun(Ex3, ['m4.csv'],{2})
    counter_test_positivi += tester_fun(Ex3, ['m5.csv'],{1,2})
    
    
    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
