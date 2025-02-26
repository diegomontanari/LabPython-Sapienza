def Ex2(fileName):
    conta = 0
    f=open(fileName,'r',encoding='UTF-8')
    for riga in f:
        l=riga.strip().split()
        if len(l)>2:
            for i in range(1,len(l)-1):
                if ord(l[i-1][-1])==ord(l[i][0])+1 and ord(l[i][-1])==ord(l[i+1][0])+1:
                    conta += 1
                    break
    f.close()
    return conta  
            
###############################################################################




"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, ['testob1.txt'],2)
    counter_test_positivi += tester_fun(Ex2, ['testob2.txt'],1)
    counter_test_positivi += tester_fun(Ex2, ['testob3.txt'],0)
    counter_test_positivi += tester_fun(Ex2, ['testob4.txt'],1)
    counter_test_positivi += tester_fun(Ex2, ['testob5.txt'],2)


    # # test aggiuntivi

    counter_test_positivi += tester_fun(Ex2, ['testob6.txt'],1)
    counter_test_positivi += tester_fun(Ex2, ['testob7.txt'],0)
    counter_test_positivi += tester_fun(Ex2, ['testob8.txt'],0)
    counter_test_positivi += tester_fun(Ex2, ['testob9.txt'],6)
    counter_test_positivi += tester_fun(Ex2, ['testob10.txt'],0)

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
