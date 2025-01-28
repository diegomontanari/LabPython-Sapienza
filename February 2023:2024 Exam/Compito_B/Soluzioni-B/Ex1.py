def Ex1(l):
    if len(l) == 0:
        return -1
    trovati = 0
    for i in range(len(l)-1):
        app=0
        for j in range(i+1,min(i+3,len(l))):
            app+=l[j]
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


    counter_test_positivi += tester_fun(Ex1, [ [352,300,52,49,1,2,2]],2)
    counter_test_positivi += tester_fun(Ex1, [ [352,352,52,53,54,55]],1)
    counter_test_positivi += tester_fun(Ex1, [ []],-1)
    counter_test_positivi += tester_fun(Ex1, [ [5]],0)
    counter_test_positivi += tester_fun(Ex1, [ [8,2,2,9]],1)
    


    # # # test aggiuntivi
    
    counter_test_positivi += tester_fun(Ex1, [ [3,300,52,49,1,2,2]],1)
    counter_test_positivi += tester_fun(Ex1, [ [1,1,1,1]],3)
    counter_test_positivi += tester_fun(Ex1, [ [5,0,0,0,0,0,5]],4)
    counter_test_positivi += tester_fun(Ex1, [ [5,6]],0)
    counter_test_positivi += tester_fun(Ex1, [ [3,3]],1)

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
