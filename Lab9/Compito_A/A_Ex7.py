#FUNCTION .get(key, optional)!
   #-> get ACCESS a KEY VALUE, RETURNS None or Standard if it does not exist.

# .get(key, default) is AMAZING!
   #-> get prevents KeyError and allows initializing a dictionary key in one line.  
   #-> If the key exists, it returns its value; otherwise, it returns the default value (e.g., 0).[if you use .get(key) the key does not exists it returns None]
   #-> You cannot do this in one line with d[key] = value because you get a key error if the key does not exist. 

def A_Ex7(fileName):
    d = {}
    with open(fileName, 'r', encoding='utf-8') as f:
        f.readline()  # Salta la prima riga (intestazione)
        for partita in f:
            ris = partita.strip().split(',')
            team1 = ris[0].strip()
            team2 = ris[1].strip()
            gol1 = int(ris[2])
            gol2 = int(ris[3])
            if gol1 > gol2:
                d[team1] = d.get(team1, 0) + 3
                d[team2] = d.get(team2, 0) + 0
            elif gol1 == gol2:
                d[team1] = d.get(team1, 0) + 1
                d[team2] = d.get(team2, 0) + 1
            else:
                d[team2] = d.get(team2, 0) + 3
                d[team1] = d.get(team1, 0) + 0
    return d

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # Esempio di test
    counter_test_positivi += tester_fun(A_Ex7, ['partite.txt'], {'Chelsea': 6, 'Everton': 3, 'Arsenal': 4, 'Tottenham': 1})

    print('La funzione', A_Ex7.__name__, 'ha superato', counter_test_positivi, 'test su', total_tests)

 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex7, ["partite1.csv"] , {'Chelsea': 3, 'Everton': 3, 'Arsenal': 4, 'Tottenham': 1})
    counter_test_positivi += tester_fun(A_Ex7, ["partite2.csv"] , {'Chelsea': 4, 'Everton': 6, 'Arsenal': 4, 'Tottenham': 2})
    counter_test_positivi += tester_fun(A_Ex7, ["partite3.csv"] , {'Bayern': 4, 'Schalke': 3, 'Amburgo': 4, 'Werder': 1, 'Colonia': 4, 'Stoccarda': 0})
    counter_test_positivi += tester_fun(A_Ex7, ["partite4.csv"] , {'Bayern': 8, 'Schalke': 6, 'Amburgo': 8, 'Werder': 2, 'Colonia': 8, 'Stoccarda': 0})
    counter_test_positivi += tester_fun(A_Ex7, ["partite5.csv"] , {'Bayern': 5, 'Schalke': 6, 'Amburgo': 5, 'Werder': 5, 'Colonia': 5, 'Stoccarda': 6})

    print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
