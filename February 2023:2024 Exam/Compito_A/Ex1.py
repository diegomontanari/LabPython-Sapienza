#IMPORTANT INFO:
    #-> range(len(l)) is different than for insieme in l because:
    #-> 1st treats the sets as INDEXES, 2nd as their TYPE (e.g: sets).
# If you need to CONFRONT things, always use the 2nd method (as you will need indexes)

def Ex1(l):
    if not l:  # Verifica se la lista è vuota
        return -1

    count = 0

    for insieme in range(len(l) - 2):
        if l[insieme] == l[insieme + 1]:
            count += 1
        elif isinstance(l[insieme], set) and isinstance(l[insieme + 1], set) and isinstance(l[insieme + 2], set):
            if l[insieme + 1].union(l[insieme + 2]) == l[insieme]:
                count += 1

    return count
    

    

###############################################################################

#NON MODIFICARE IL CODICE (codice di test della funzione)

if __name__ == '__main__':
    from tester import tester_fun
    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione


    counter_test_positivi += tester_fun(Ex1, [ [{5,7,2},{5,7},{5,2},{5},{5},{2},{5},{7}]],2)

    counter_test_positivi += tester_fun(Ex1, [ [{5,7,2},{5,7},{5,2},{5},{9},{2}]],1)

    counter_test_positivi += tester_fun(Ex1, [ []],-1)

    counter_test_positivi += tester_fun(Ex1, [ [{1,2,3,4,5},{1},{2},set(),{3},{4},{5}]],0)

    counter_test_positivi += tester_fun(Ex1, [ [{7,2,3,4,5},{1},{3,4},{3},{4},{5}]],1)
    
                                              
    
    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
