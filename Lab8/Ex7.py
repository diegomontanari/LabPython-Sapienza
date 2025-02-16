def Ex7(fileName):
    with open(fileName, 'r', encoding='UTF-8') as f:
        nums = []
        for line in f:
            words = line.split()
            for word in words:
                if word.isdigit():
                    nums.append(int(word))
    return sum(nums)

"""
NOTES: there is a powerful other way to do this, using REGEX:

import re
def Ex7(fileName):
    with open(fileName, 'r', encoding='UTF-8') as f:
        content = f.read()
        nums = map(int, re.findall(r'\d+', content))
    return sum(nums)

"""

 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex7, ["file1.txt"] , 14)
    counter_test_positivi += tester_fun(Ex7, ["file2.txt"] , 17)
    counter_test_positivi += tester_fun(Ex7, ["file3.txt"] , 18)
    counter_test_positivi += tester_fun(Ex7, ["file4.txt"] , 20)
    counter_test_positivi += tester_fun(Ex7, ["file5.txt"] , 0)

    print('La funzione',Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
