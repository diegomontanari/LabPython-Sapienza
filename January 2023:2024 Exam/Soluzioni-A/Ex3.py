def Ex3(nomeFile):
    import pandas as pd
    import numpy as np
    ris = {}
    df=pd.read_csv(nomeFile,header=None)
    m=np.array(df.values)
    righe=m.shape[0]
    colonne=m.shape[1]
    camminoMax=0
    ris=set()
    for i in range(1, righe - 1):
    road = m[i, 0]
    print(i,  road, end='+')
    riga_corrente = i
    direzione = -1  # inizialmente verso l'alto

    for j in range(1, colonne):
        if riga_corrente == 0:
            road = 1  # cambia direzione verso il basso
        elif riga_corrente == righe - 1:
            direzione = -1  # cambia direzione verso l'alto

        riga_corrente += direzione
        cammino += m[riga_corrente, j]
        print(m[riga_corrente, j], end='+')

    print('=', cammino)
    if cammino > camminoMax:
        ris = {i}
        camminoMax = cammino
    elif cammino == camminoMax:
        ris.add(i)

    return ris
###############################################################################


if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['m1.csv'],{1})
    counter_test_positivi += tester_fun(Ex3, ['m2.csv'],set())
    counter_test_positivi += tester_fun(Ex3, ['m3.csv'],{2})
    counter_test_positivi += tester_fun(Ex3, ['m4.csv'],{2})
    counter_test_positivi += tester_fun(Ex3, ['m5.csv'],{1,2})
    

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex3, ['m6.csv'],{1})
    counter_test_positivi += tester_fun(Ex3, ['m7.csv'],{1})
    counter_test_positivi += tester_fun(Ex3, ['m8.csv'],set())
    counter_test_positivi += tester_fun(Ex3, ['m9.csv'],{2})
    counter_test_positivi += tester_fun(Ex3, ['m10.csv'],{2})
    
    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
