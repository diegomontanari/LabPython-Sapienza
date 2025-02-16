def Ex5(s,n):
    d = {}
    parole = s.strip().split()
    for elem in parole:
        if len(elem) >= n:
            d[elem[0]] = d.get(elem[0],0) + 1
    return d

 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex5, ['tanto va la gatta al lardo che ci lascia lo zampino',3] , {'t': 1, 'g': 1, 'l': 2, 'c': 1, 'z': 1})
    counter_test_positivi += tester_fun(Ex5, ['tanto va la gatta al lardo che ci lascia lo zampino',5] , {'t': 1, 'g': 1, 'l': 2, 'z': 1})
    counter_test_positivi += tester_fun(Ex5, ['scrivere una funzione che prende in ingresso una stringa s composta di caratteri alfabetici e spazi bianchi e restituisce una lista con tutte le parole diverse della stringa',5] , {'s': 4, 'f': 1, 'p': 2, 'i': 1, 'c': 2, 'a': 1, 'b': 1, 'r': 1, 'l': 1, 't': 1, 'd': 2})
    counter_test_positivi += tester_fun(Ex5, ['calcoli il dizionario che ha come chiavi le lettere minuscole e come valore il numero di parole di s che cominciano per quella lettera e sono lunghe almeno n caratteri',3] , {'c': 8, 'd': 1, 'l': 3, 'm': 1, 'v': 1, 'n': 1, 'p': 2, 'q': 1, 's': 1, 'a': 1})
    counter_test_positivi += tester_fun(Ex5, ['',2] , {})

    counter_test_positivi += tester_fun(Ex5, ['ab ab ab ab',3] , {})
    counter_test_positivi += tester_fun(Ex5, ['abcd abcd abcd',4] , {'a': 3})
    counter_test_positivi += tester_fun(Ex5, ['a dire il vero immacolato',3] , {'i': 1, 'v': 1, 'd': 1})
    counter_test_positivi += tester_fun(Ex5, ['a a a a a a a a a a a a a',5] , {})
    counter_test_positivi += tester_fun(Ex5, ['a aa aaa aaaa ee',3] , {'a':2})


    print('La funzione',Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
