import re

def Ex2(file):
    with open(file, 'r', encoding='UTF-8').read() as f:
        count_ok = 0
        count_ko = 0
        pattern = r'(\d{1,2})([.:])(\d{1,2})\2(\d{1,2})'
        res = re.finditer(pattern, f) #Returns an iterator that produces MATCH OBJECTS for each match found in the text.
        for i in res: #Iterates on every Match object
            hours = int(i.group(1)) #Group 
            minutes = int(i.group(3)) 
            seconds = int(i.group(4))
            if hours > 24 or minutes >= 60 or seconds >= 60:
            count_ok += 1
        else:
            count_ko += 1
        
    return count_ok, count_ko

    


            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, ['testo1d.txt'], (3,2))
    counter_test_positivi += tester_fun(Ex2, ['testo2d.txt'], (3,4))
    counter_test_positivi += tester_fun(Ex2, ['testo3d.txt'], (3,4))
    counter_test_positivi += tester_fun(Ex2, ['testo4d.txt'], (4,5))
    counter_test_positivi += tester_fun(Ex2, ['testo5d.txt'], (5,5))
    
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
