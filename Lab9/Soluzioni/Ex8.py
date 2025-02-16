def Ex8(file):
    f = open(file,'r',encoding='utf-8')
    d = {}
    f.readline() #legge la prima riga
    
    for relazione in f:
        riga = relazione.strip().split(',')
        nome1 = riga[0].strip()
        if nome1 not in d:
            d[nome1] = []
        nome2 = riga[1].strip()
        if nome2 not in d:
            d[nome2] = []
        rel = riga[2].strip()
        if rel == 'amici':
            if nome1 not in d[nome2]:
                d[nome2].append(nome1)
                d[nome2].sort()
            if nome2 not in d[nome1]:
                d[nome1].append(nome2)
                d[nome1].sort()
        else:
            if nome1 in d[nome2]:
                d[nome2].remove(nome1)
            if nome2 in d[nome1]:
                d[nome1].remove(nome2)
    f.close()
    return d   
 
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex8, ["amici1.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
    counter_test_positivi += tester_fun(Ex8, ["amici2.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria'], 'Maria': ['Anna'], 'Paola': [], 'Giorgio': []})
    counter_test_positivi += tester_fun(Ex8, ["amici3.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
    counter_test_positivi += tester_fun(Ex8, ["amici4.csv"] , {'Marco': ['Giorgio', 'Paolo'], 'Giorgio': ['Marco'], 'Paolo': ['Marco'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna']})
    counter_test_positivi += tester_fun(Ex8, ["amici5.csv"] , {'Marco': [], 'Giorgio': [], 'Paola': [], 'Anna': []})

    counter_test_positivi += tester_fun(Ex8, ["amici6.csv"] , {'Paolo': [], 'Marco': []})
    counter_test_positivi += tester_fun(Ex8, ["amici7.csv"] , {'Paolo': ['Marco', 'Sandro'], 'Marco': ['Paolo'], 'Michele': [], 'Sandro': ['Paolo'], 'Giuditta': ['Enesto'], 'Enesto': ['Giuditta']})
    counter_test_positivi += tester_fun(Ex8, ["amici8.csv"] , {})
    counter_test_positivi += tester_fun(Ex8, ["amici9.csv"] , {'Minnie': ['Topolino'], 'Topolino': ['Minnie', 'Paperino'], 'Paperino': ['Paperina', 'Topolino'], 'Paperina': ['Paperino'], 'Jafar': [], 'Jago': []})
    counter_test_positivi += tester_fun(Ex8, ["amici10.csv"] , {'Anna': ['Annetta'], 'Annetta': ['Anna'], 'Bea': ['Beluna', 'Bibbi'], 'Bibbi': ['Bea'], 'Beluna': ['Bea']})

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
