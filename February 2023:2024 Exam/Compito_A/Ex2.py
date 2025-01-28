#REMEMBER:
    #.split() splits a list into a LIST OF SUBSTRINGS
#IMPORTANT:
    #I'm using NESTED INDEXING (indicizzazione nidificata) to access
    #the i-th character of the word
  
def Ex2(fileName):
    counter = 0
    with open(fileName, 'r', encoding='UTF-8') as f:
        for riga in f:
            l=riga.strip().split()
            for word in range(1, len(l) - 1):
                if (ord(l[word][0]) - ord(l[word-1][-1]) == 1) and (ord(l[word +1][0]) - ord(l[word][-1]) == 1):
                    counter += 1
                    break
    return counter

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, ['testoa1.txt'],2)
    counter_test_positivi += tester_fun(Ex2, ['testoa2.txt'],3)
    counter_test_positivi += tester_fun(Ex2, ['testoa3.txt'],0)
    counter_test_positivi += tester_fun(Ex2, ['testoa4.txt'],1)   
    counter_test_positivi += tester_fun(Ex2, ['testoa5.txt'],1)
    
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
