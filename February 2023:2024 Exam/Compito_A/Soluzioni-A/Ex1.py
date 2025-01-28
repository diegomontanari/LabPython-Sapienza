def Ex1(l):
    if len(l) == 0:
        return -1
    trovati = 0
    for i in range(len(l)-1):
        app=set()
        for j in range(i+1,min(i+3,len(l))):
            app=app.union(l[j])
            if app==l[i]:
                trovati+=1
                #print(i,l[i])
                break
    return trovati
    

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione


    counter_test_positivi += tester_fun(Ex1, [ [{5,7,2},{5,7},{5,2},{5},{5},{2},{5},{7}]],2)
    counter_test_positivi += tester_fun(Ex1, [ [{5,7,2},{5,7},{5,2},{5},{9},{2}]],1)
    counter_test_positivi += tester_fun(Ex1, [ []],-1)
    counter_test_positivi += tester_fun(Ex1, [ [{1,2,3,4,5},{1},{2},set(),{3},{4},{5}]],0)
    counter_test_positivi += tester_fun(Ex1, [ [{7,2,3,4,5},{1},{3,4},{3},{4},{5}]],1)
    


    # # test aggiuntivi
    
    counter_test_positivi += tester_fun(Ex1, [ [{5,7,2},{5,7},{2},{2},{2}] ],3)
    counter_test_positivi += tester_fun(Ex1, [ [{5,2},{5},{5,2},{2},{5}]],2)
    counter_test_positivi += tester_fun(Ex1, [ [set()]],0)
    counter_test_positivi += tester_fun(Ex1, [ [set(),set(),{3},{4},{5}]],1)
    counter_test_positivi += tester_fun(Ex1, [ [{5,2},{5},{2},{5},{2}]],1)

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
