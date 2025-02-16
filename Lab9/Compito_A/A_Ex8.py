
def Ex8(file):
    d = {}
    with open(file, 'r', encoding='UTF-8') as f:
        next(f)  # It's next(f) or f = f.readline(), (f = next(f) is WRONG !!), you cannot assing a variable to next.
        for line in f:
            name, name2, rel = line.strip().split(',')
            name, name2 = name.strip(), name2.strip()
            
            # Initializes the key if it does not exist
            if name not in d:
                d[name] = []
            if name2 not in d:
                d[name2] = []

            if rel.strip() == 'amici':
                # Adds the bidirectional friendship if not already present"
                if name2 not in d[name]:
                    d[name].append(name2)
                    d[name].sort()
                if name not in d[name2]:
                    d[name2].append(name)
                    d[name2].sort()
            else:  # If they are not friends, removes the connection
                if name2 in d[name]:
                    d[name].remove(name2)
                if name in d[name2]:
                    d[name2].remove(name)
    
    return d

                    


            


    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex8, ["amici1.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
    counter_test_positivi += tester_fun(Ex8, ["amici2.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria'], 'Maria': ['Anna'], 'Paola': [], 'Giorgio': []})
    counter_test_positivi += tester_fun(Ex8, ["amici3.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
    counter_test_positivi += tester_fun(Ex8, ["amici4.csv"] , {'Marco': ['Giorgio', 'Paolo'], 'Giorgio': ['Marco'], 'Paolo': ['Marco'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna']})
    counter_test_positivi += tester_fun(Ex8, ["amici5.csv"] , {'Marco': [], 'Giorgio': [], 'Paola': [], 'Anna': []})

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
