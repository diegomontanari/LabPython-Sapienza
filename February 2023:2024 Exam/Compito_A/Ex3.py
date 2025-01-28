#NOTIONS:
    #-> A DataFrame is a bidimensional struct in the pandas library. 
    #-> It's similar to an Excel table, it's made of rows and colums.
#DIFFERENCE:
    #-> np.array(df) creates an array with labels, 
    #-> np.array(df.values) creates the same array but without labels (etichette)
#ARTRIBUTE VS METHOD:
    #-> Attribute: A property of an object that contains data. Does not require parentheses. (Example: df.values, df.shape)
    #-> Method: A function associated with an object that performs an action. Requires parentheses. (Example: df.head(), df.describe())

def Ex3(fileName):
    import pandas as pd
    import numpy as np
    
    res = set()
    maxSum = 0

    df = pd.read_csv(fileName, header=None)  # Correct function to read CSV
    ar = np.array(df.values)
    rows = ar.shape[0]  # the first element of the tuple (number of rows)
    columns = ar.shape[1]  # second element of the tuple (number of columns)
    
    for i in range(rows):
        minimum = min(ar[i])
        minValue = list(ar[i]).index(minimum)
        sumValues = 0

        # Calculate the sum of the numbers starting from the minimum
        for j in range(minValue, columns):
            sumValues += ar[i, j]

        if sumValues > maxSum:
            res = {i}
            maxSum = sumValues
        elif sumValues == maxSum:
            res.add(i)
    return res


 
###############################################################################
nomeFile='m1.csv'
"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['m1.csv'],{0,2})

    counter_test_positivi += tester_fun(Ex3, ['m2.csv'],{0})

    counter_test_positivi += tester_fun(Ex3, ['m3.csv'],{0,2})

    counter_test_positivi += tester_fun(Ex3, ['m4.csv'],{0,1})

    counter_test_positivi += tester_fun(Ex3, ['m5.csv'],{0,1,2,3})
    
    
    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
