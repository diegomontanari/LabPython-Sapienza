def Ex3(fileName):
    f=open(fileName, "r", encoding="UTF-8")
    f.readline()
    d={}
    for riga in f:
        l=riga.strip().split(",")
        matricola = int(l[0])
        voto=int(l[1])
        materia = l[2]
        if voto>=18:
            if materia in d:
                d[materia].append(matricola)
                d[materia].sort()
            else:
                d[materia] = [matricola]
    f.close()
    return d

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex3, ["esami1.csv"] , {'Fisica': [1345, 1753], 'Analisi': [1346], 'Geometria': [1896]})
    counter_test_positivi += tester_fun(Ex3, ["esami2.csv"] , {'Analisi': [1346]})
    counter_test_positivi += tester_fun(Ex3, ["esami3.csv"] , {'Analisi': [1347, 1348], 'Ricerca Operativa': [1347, 1349]})
    counter_test_positivi += tester_fun(Ex3, ["esami4.csv"] , {'Basi di Dati': [1012, 1100], 'Analisi': [1021]})
    counter_test_positivi += tester_fun(Ex3, ["esami5.csv"] , {'Fisica': [1345], 'Fondamenti': [1987], 'Analisi': [1346], 'Geometria': [1896]})

    counter_test_positivi += tester_fun(Ex3, ["esami6.csv"] , {})
    counter_test_positivi += tester_fun(Ex3, ["esami7.csv"] , {})
    counter_test_positivi += tester_fun(Ex3, ["esami8.csv"] , {'Analisi': [1346, 1896], 'Geometria': [1896], 'Fisica': [1345, 1753]})
    counter_test_positivi += tester_fun(Ex3, ["esami9.csv"] , {'Analisi': [1346], 'Geometria': [1896], 'Fisica': [1753]})
    counter_test_positivi += tester_fun(Ex3, ["esami10.csv"] , {'Fisica': [1345, 1753], 'Analisi': [1346], 'Informatica': [1753, 1896]})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
