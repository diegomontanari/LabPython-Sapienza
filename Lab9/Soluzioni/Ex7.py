def A_Ex7(fileName):
    f = open(fileName,'r',encoding='utf-8')
    d = {}
    f.readline()
    for partita in f:
        ris = partita.strip().split(',')
        team1 = ris[0].strip()
        team2 = ris[1].strip()
        gol1 = int(ris[2])
        gol2 = int(ris[3])
        if gol1 > gol2:
            d[team1] = d.get(team1,0) + 3
            d[team2] = d.get(team2,0) + 0
        elif gol1 == gol2:
            d[team1] = d.get(team1,0) + 1
            d[team2] = d.get(team2,0) + 1
        else:
            d[team2] = d.get(team2,0) + 3
            d[team1] = d.get(team1,0) + 0
    f.close()
    return d


 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(A_Ex7, ["partite1.csv"] , {'Chelsea': 3, 'Everton': 3, 'Arsenal': 4, 'Tottenham': 1})
    counter_test_positivi += tester_fun(A_Ex7, ["partite2.csv"] , {'Chelsea': 4, 'Everton': 6, 'Arsenal': 4, 'Tottenham': 2})
    counter_test_positivi += tester_fun(A_Ex7, ["partite3.csv"] , {'Bayern': 4, 'Schalke': 3, 'Amburgo': 4, 'Werder': 1, 'Colonia': 4, 'Stoccarda': 0})
    counter_test_positivi += tester_fun(A_Ex7, ["partite4.csv"] , {'Bayern': 8, 'Schalke': 6, 'Amburgo': 8, 'Werder': 2, 'Colonia': 8, 'Stoccarda': 0})
    counter_test_positivi += tester_fun(A_Ex7, ["partite5.csv"] , {'Bayern': 5, 'Schalke': 6, 'Amburgo': 5, 'Werder': 5, 'Colonia': 5, 'Stoccarda': 6})

    counter_test_positivi += tester_fun(A_Ex7, ["partite6.csv"] , {})
    counter_test_positivi += tester_fun(A_Ex7, ["partite7.csv"] , {'Chelsea': 3, 'Everton': 3, 'Arsenal': 3, 'Tottenham': 3})
    counter_test_positivi += tester_fun(A_Ex7, ["partite8.csv"] , {'Chelsea': 6, 'Everton': 3, 'Arsenal': 3, 'Tottenham': 6})
    counter_test_positivi += tester_fun(A_Ex7, ["partite9.csv"] , {'Everton': 6, 'Chelsea': 3, 'Tottenham': 3, 'Arsenal': 6})
    counter_test_positivi += tester_fun(A_Ex7, ["partite10.csv"] , {'Chelsea': 3, 'Everton': 0})

    print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
