

            
 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex8, ["file1.txt"] , 2)
    counter_test_positivi += tester_fun(Ex8, ["file2.txt"] , 2)
    counter_test_positivi += tester_fun(Ex8, ["file3.txt"] , 2)
    counter_test_positivi += tester_fun(Ex8, ["file4.txt"] , 3)
    counter_test_positivi += tester_fun(Ex8, ["file5.txt"] , 3)

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
