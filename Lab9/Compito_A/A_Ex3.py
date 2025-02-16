# REMEMBER:
    #-> dictName[key] IS EQUAL TO THE value (!!!).

def Ex3(fileName):
    d = dict()
    with open(fileName, 'r', encoding='UTF-8') as f:
        f.readline() #skips the 1st line, similar to the function next(f) (which is more idiomatic as it's more explicit) (next() gets the next element from an iterator)
        for riga in f:
            l = riga.strip().split(",") #Una lista di parole per riga
            matricola = int(l[0])
            voto = int(l[1])
            materia = l[2]
            if voto >= 18:
                if materia in d:
                    d[materia].append(matricola) #this appends the value
                    d[materia].sort()
                else:
                    d[materia] = [matricola] #This creates the list from the key materia (with matricola as 1st element)
    return d

            







        

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex3, ["esami1.csv"] , {'Fisica': [1345, 1753], 'Analisi': [1346], 'Geometria': [1896]})
    counter_test_positivi += tester_fun(Ex3, ["esami2.csv"] , {'Analisi': [1346]})
    counter_test_positivi += tester_fun(Ex3, ["esami3.csv"] , {'Analisi': [1347, 1348], 'Ricerca Operativa': [1347, 1349]})
    counter_test_positivi += tester_fun(Ex3, ["esami4.csv"] , {'Basi di Dati': [1012, 1100], 'Analisi': [1021]})
    counter_test_positivi += tester_fun(Ex3, ["esami5.csv"] , {'Fisica': [1345], 'Fondamenti': [1987], 'Analisi': [1346], 'Geometria': [1896]})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
