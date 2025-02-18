def Ex2(nomeFile):

    ris={}

    f=open(nomeFile,'r',encoding='UTF-8')
    for r in f:
        r=r.strip().split()
        for i in range(len(r)-1):
            for j in range(i+1,len(r)):
                if len(r[i])==len(r[j]):
                    if len(r[i]) in ris:
                        ris[len(r[i])].add(r[i])
                    else:               
                        ris[len(r[i])]={r[i]}
                    ris[len(r[i])].add(r[j])
    f.close()
    return ris
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, ['testod1.txt'],{5: {'vanno', 'lardo', 'tanto', 'gatti'}, 2: {'ci', 'al'}, 3: {'che', 'gli'}, 11: {'pascolavano', 'superlativi'}})    
    counter_test_positivi += tester_fun(Ex2, ['testod2.txt'],{6: {'questo', 'noioso', 'sembra'}, 9: {'veramente', 'esercizio'}, 2: {'ma', 'lo'}, 4: {'fare', 'devo'}})   
    counter_test_positivi += tester_fun(Ex2, ['testod3.txt'],{3: {'sia', 'che', 'non', 'mai'}, 6: {'questo', 'quanto', 'noioso'}, 9: {'risolvere', 'esercizio'}, 10: {'concepirlo', 'soffermati'}})
    counter_test_positivi += tester_fun(Ex2, ['testod4.txt'],{3: {'sei', 'zio', 'mio', 'uno', 'tre', 'due'}})
    counter_test_positivi += tester_fun(Ex2, ['testod5.txt'],{})
 
    
    # # test aggiuntivi

    counter_test_positivi += tester_fun(Ex2, ['testod6.txt'],{})
    counter_test_positivi += tester_fun(Ex2, ['testod7.txt'], {3: {'uno', 'due'}})
    counter_test_positivi += tester_fun(Ex2, ['testod8.txt'],{1: {'e', 'l', 'f', 'm', 'h', 'a', 'g', 'i', 'c', 'd', 'b', 'n'}})   
    counter_test_positivi += tester_fun(Ex2, ['testod9.txt'],{7: {'stufato', 'proprio'}}) 
    counter_test_positivi += tester_fun(Ex2, ['testod10.txt'],{5: {'prova', 'lunga'}, 3: {'tre', 'uno', 'due'}}) 
     
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
