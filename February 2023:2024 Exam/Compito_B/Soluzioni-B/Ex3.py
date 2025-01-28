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
    for j in range(colonne):
        massimo=max(m[:,j])
        i_massimo=list(m[:,j]).index(massimo)
        somma=0
        for i in range(i_massimo,righe):
            somma+=m[i,j]
        if somma>sommaMax:
            ris={j}
            sommaMax=somma
        elif somma==sommaMax:
            ris.add(j)   
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
    counter_test_positivi += tester_fun(Ex3, ['m2.csv'],{4})
    counter_test_positivi += tester_fun(Ex3, ['m3.csv'],{0,1,2,3,4})
    counter_test_positivi += tester_fun(Ex3, ['m4.csv'],{1})
    counter_test_positivi += tester_fun(Ex3, ['m5.csv'],{0,1,2})
  

    # # test aggiuntivi
    
    counter_test_positivi += tester_fun(Ex3, ['m6.csv'],{0,1})
    counter_test_positivi += tester_fun(Ex3, ['m7.csv'],{0})
    counter_test_positivi += tester_fun(Ex3, ['m8.csv'],{0})
    counter_test_positivi += tester_fun(Ex3, ['m9.csv'],{0,1,2,3,4,5})
    counter_test_positivi += tester_fun(Ex3, ['m10.csv'],{0,1,4,5,6})

    
    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
