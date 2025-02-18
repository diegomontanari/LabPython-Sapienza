def Ex2(file):
    f=open(file,'r',encoding='UTF-8')
    parole = f.read().strip().split()
    f.close()
    ris = {}
    for parola in parole:
        if len(parola) in ris:
            if parola > ris[len(parola)]:
                ris[len(parola)] = parola
        else:
            ris[len(parola)] = parola
    return ris   
    
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, ['testoa1.txt'],{5: 'tanto', 2: 'va', 3: 'chi', 6: 'lascia', 7: 'zampino', 1: 'l', 4: 'roma', 8: 'poltrona'})    
    counter_test_positivi += tester_fun(Ex2, ['testoa2.txt'],{5: 'tanto', 2: 'va', 3: 'chi', 6: 'lascia', 7: 'zampino', 1: 'l', 4: 'sano', 8: 'poltrona'})   
    counter_test_positivi += tester_fun(Ex2, ['testoa3.txt'],{4: 'vero', 3: 'uno', 1:'e'})   
    counter_test_positivi += tester_fun(Ex2, ['testoa4.txt'],{}) 
    counter_test_positivi += tester_fun(Ex2, ['testoa5.txt'],{6: 'sembra', 5: 'molto', 3: 'non', 9: 'difficile', 2: 'mi', 7: 'sbaglio'})
 
    
    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex2, ['testoa6.txt'],{6: 'sembra', 5: 'molto', 3: 'non', 9: 'difficile', 2: 'mi', 7: 'sbaglio'})
    counter_test_positivi += tester_fun(Ex2, ['testoa7.txt'],{6: 'sembra', 5: 'molto', 3: 'non', 9: 'difficile', 2: 'mi', 7: 'sbaglio'})
    counter_test_positivi += tester_fun(Ex2, ['testoa8.txt'],{6: 'sembra', 5: 'molto', 3: 'non', 9: 'difficile', 2: 'mi', 7: 'sbaglio'})
    counter_test_positivi += tester_fun(Ex2, ['testoa8.txt'],{1:'i', 2: 'la', 3: 'una', 4: 'fece', 5: 'tutti', 6: 'vedere', 7: 'vennero' })   
    counter_test_positivi += tester_fun(Ex2, ['testoa9.txt'],{6: 'vedere'}) 
    counter_test_positivi += tester_fun(Ex2, ['testoa10.txt'],{1:'g', 2:'gg'}) 
     
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
