def Ex6(fileName):
    d = {}
    if not fileName:
        return d
    with open(fileName, 'r', encoding='UTF-8') as f:
        j_row = 1
        for line in f:
            lista = line.strip().split(',')
            for num in lista:
                num = int(num)
                if num in d:
                    d[num].add(j_row)
                else:
                    d[num] = {j_row}
            j_row += 1
    return d 
           

"""for row in f:
           lista = row.strip().split(',') #list of numbers in a row
           for num in lista:
               if num not in d: 
                   d[num] = {1}
               else:
                   d[num].add()"""
 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex6, ['numeri1.txt'] , {10: {1,2}, -5: {1,2}, 0: {1}, 8: {2}, -3: {2}})
    counter_test_positivi += tester_fun(Ex6, ['numeri2.txt'] , {10: {1,2}, 0: {2}})
    counter_test_positivi += tester_fun(Ex6, ['numeri3.txt'] , {3: {1,2}, 4: {1}, 5: {1}, 2: {2,3}, 0: {2,3}})
    counter_test_positivi += tester_fun(Ex6, ['numeri4.txt'] , {2: {1,2,3,4,5}, 1: {1,2,6}, 3: {6}})
    counter_test_positivi += tester_fun(Ex6, ['numeri5.txt'] , {})

    print('La funzione',Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)