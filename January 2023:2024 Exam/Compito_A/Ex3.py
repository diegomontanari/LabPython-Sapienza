# In the exam I cannot use pandas. 
    #-> I can use np.loadtxt(filename, delimiter= ',') which does the job of both pd.read_csv and np.array(df.values)
    #-> There is a catch: pd.read_csv() is much more powerful in handling complicated situations, but np.loadtxt still gets the job done.

def Ex3(filename):
    import pandas as pd
    import numpy as np
    result = {}
    df = pd.read_csv(filename, header=None)
    matrix = np.array(df.values)
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    max_path = 0
    result = set()
    
    for i in range(1, rows - 1):
        path = matrix[i, 0]
        print(i, path, end='+')
        current_row = i
        direction = -1

        for j in range(1, columns):
            if current_row == 0:
                direction = 1  # change direction downwards
            elif current_row == rows - 1:
                direction = -1  # change direction upwards

            #diagonal movement
            current_row += direction #salgo o scendo
            path += matrix[current_row, j] #diagonale completato
            print(matrix[current_row, j], end='+')

        print('=', path)
        if path > max_path:
            result = {i}
            max_path = path
        elif path == max_path:
            result.add(i)

    return result


    

 
###############################################################################
nomeFile='m1.csv'
"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['m1.csv'],{1})
    counter_test_positivi += tester_fun(Ex3, ['m2.csv'],set())
    counter_test_positivi += tester_fun(Ex3, ['m3.csv'],{2})
    counter_test_positivi += tester_fun(Ex3, ['m4.csv'],{2})
    counter_test_positivi += tester_fun(Ex3, ['m5.csv'],{1,2})
    
    
    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
