def Ex1(s, l):
    x = set()
    cont = 0
    
    for i in s:
        x.add(i)
        
    for parola in l:
        tutti_validi = True
        parola_set = set(parola)  # Creiamo un set dei caratteri della parola (!!)
        
        # Verifichiamo che ogni carattere della parola sia in x (come facevi tu)
        for carattere in parola:
            if carattere not in x:
                tutti_validi = False
                print(f"Ho trovato una parola non valida: {parola}")
                break
                
        # Verifichiamo che ogni carattere di x sia nella parola
        if tutti_validi:  # Solo se il primo controllo è passato
            for carattere in x:
                if carattere not in parola_set:
                    tutti_validi = False
                    print(f"Ho trovato una parola non valida: {parola}")
                    break
                    
        if tutti_validi:
            cont += 1
            
    return cont


#REMEMBER: Proprietà dellesequenze di interi o di caratteri

# In Python, strings are iterable sequences of characters. When converting a string to 
# another iterable type (list, set, tuple), each character becomes a separate element,
# preserving its original properties (case, whitespace, special characters)
"""
text = "Hello World"
char_list = list(text)  # ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
"""


#Step:
# Creo un set in cui ci inserisco ogni carattere di s
# Passi parola, se tutti i caratteri in set aumenti contatore             
                            
            
#Past big mistake:
# Remember that counters have the type of the element they're iterating on. (In Python)
# So, to store a char in a set, i's x.add(i) because i it's already a char, no need to access the i-th position of the str. This will not work.
"""
for i in s:
        x.add(s[i]) 
This code got me this error: string indices must be integers.
"""

                    
        
   
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, ['canto',['canto', 'conto', 'cotanto', 'taccone']],2)
    counter_test_positivi += tester_fun(Ex1, ['canto',['canto', 'conta', 'cotta', 'tacco', 'cccaa', 'acnott']],3)
    counter_test_positivi += tester_fun(Ex1, ['canta',['canto', 'conta', 'tanca', 'tacconata']],1)
    counter_test_positivi += tester_fun(Ex1, ['pappa',['papa', 'appare', 'aappp', 'tacco']],2)
    counter_test_positivi += tester_fun(Ex1, ['papa',['pappe', 'papato']],0)  
    
    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
