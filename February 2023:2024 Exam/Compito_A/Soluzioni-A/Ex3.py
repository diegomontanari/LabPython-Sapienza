def Ex3(fileName):
    import pandas as pd
    import numpy as np
    ris = {}
    df=pd.read_csv(fileName,header=None)
    m=np.array(df.values)
    righe=m.shape[0]
    colonne=m.shape[1]
    sommaMax=0
    ris=set()
    for i in range(righe):
        minimo=min(m[i])
        j_minimo=list(m[i]).index(minimo)
        somma=0
        for j in range(j_minimo,colonne):
            somma+=m[i,j]
        if somma>sommaMax:
            ris={i}
            sommaMax=somma
        elif somma==sommaMax:
            ris.add(i)   
    return ris

###############################################################################
#nomeFile='m1.csv'
"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['m1.csv'],{0,2})
    counter_test_positivi += tester_fun(Ex3, ['m2.csv'],{0})
    counter_test_positivi += tester_fun(Ex3, ['m3.csv'],{0,2})
    counter_test_positivi += tester_fun(Ex3, ['m4.csv'],{0,1})
    counter_test_positivi += tester_fun(Ex3, ['m5.csv'],{0,1,2,3})
    

    # # test aggiuntivi

    counter_test_positivi += tester_fun(Ex3, ['m6.csv'],{0,1,2})
    counter_test_positivi += tester_fun(Ex3, ['m7.csv'],{0,1,2})
    counter_test_positivi += tester_fun(Ex3, ['m8.csv'],{0})
    counter_test_positivi += tester_fun(Ex3, ['m9.csv'],{3})
    counter_test_positivi += tester_fun(Ex3, ['m10.csv'],{3})
    
    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
