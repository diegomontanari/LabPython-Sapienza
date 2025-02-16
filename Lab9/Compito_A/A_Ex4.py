def Ex4(fileName):
   with open(fileName, 'r', encoding='UTF-8') as f:
       next(f)
       d = {}
       for riga in f:
           l = riga.strip().split(',')
           matricola = int(l[0])
           voto = int(l[1])
           if voto >= 18:
               if matricola not in d:
                   d[matricola] = 1
               else:
                   d[matricola] += 1
       return d

       
   


"""if matricola not in d:
          d[matricola] = int(0)"""


###############################################################################


"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex4, ["esami1.csv"] , {1345: 1, 1346: 1, 1896: 1, 1753: 1})
    counter_test_positivi += tester_fun(Ex4, ["esami2.csv"] , {1346: 1})
    counter_test_positivi += tester_fun(Ex4, ["esami3.csv"] , {1347: 2, 1348: 1, 1349: 1})
    counter_test_positivi += tester_fun(Ex4, ["esami4.csv"] , {1100: 1, 1012: 1, 1021: 1})
    counter_test_positivi += tester_fun(Ex4, ["esami5.csv"] , {1345: 1, 1987: 1, 1346: 1, 1896: 1})

    print('La funzione',Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
