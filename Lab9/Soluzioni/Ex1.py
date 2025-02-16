def Ex1(l):
    d = {}
    for elem in l:
        d[elem] = d.get(elem,0) + 1
    return d 

     
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex1, [['casa','orso','cane','casa','orso','casa']] , {'casa': 3, 'orso': 2, 'cane': 1})
    counter_test_positivi += tester_fun(Ex1, [['casa','casa','casa']] , {'casa': 3})
    counter_test_positivi += tester_fun(Ex1, [['casa','orso','cane','cassa','osso','casta']] , {'casa': 1, 'orso': 1, 'cane': 1, 'cassa': 1, 'osso': 1, 'casta': 1})
    counter_test_positivi += tester_fun(Ex1, [['casa']] , {'casa': 1})
    counter_test_positivi += tester_fun(Ex1, [[]] , {})

    counter_test_positivi += tester_fun(Ex1, [['','']] , {'': 2})
    counter_test_positivi += tester_fun(Ex1, [['due parole']] , {'due parole': 1})
    counter_test_positivi += tester_fun(Ex1, [['due due', 'tre tre']] , {'due due': 1, 'tre tre': 1})
    counter_test_positivi += tester_fun(Ex1, [['123', '124','123']] , {'123': 2, '124':1})
    counter_test_positivi += tester_fun(Ex1, [['tre\tparole\ninsieme']] , {'tre\tparole\ninsieme':1})

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
