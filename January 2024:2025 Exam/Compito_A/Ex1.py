def Ex1(l,n):
    if not l:
        return -1, -1
    maxsub = []
    for i in range(len(l)):
        j = i + 1
       # print(f"For esterno: iterando in {range(len(l))} con contatore = {i}")
        for j in range(j, len(l)):
            # print(f"For interno: iterando in {range(j, len(l))} con contatore = {j} ")
            subseq = l[i:j+1] 
            # print(f"La mia subseq è: {subseq}")
            if max(subseq) - min(subseq) <= n and len(maxsub) < len(subseq):
                maxsub = subseq
                # print(f"Ho trovato una nuova maxseq: {maxsub}")
    if len(maxsub) >= 2:
        # print(f"Sto per returnare: {maxsub.index(maxsub[0]), maxsub.index(maxsub[-1])}")
        return l.index(maxsub[0]), l.index((maxsub[-1]))
    else:
        return -1, -1

# Using .index is not a best practice as it returns the first occurrence of something and this could create problems,
#   This is a better code:
"""
def Ex1(l, n):
    if not l:
        return -1, -1
    maxsub = []
    start, end = -1, -1

    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            subseq = l[i:j+1]
            if max(subseq) - min(subseq) <= n and len(maxsub) < len(subseq):
                maxsub = subseq
                start, end = i, j

    return (start, end) if len(maxsub) >= 2 else (-1, -1)

"""
# WHAT CHANGES? 
# Now we store the indices i and j directly every time we find a new maxsub. 
# We don't use .index(), which avoids the issue with duplicates. 
# The function is now more reliable and should always return the correct result.

             
             

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [[3, 5, 7, 2, 8],4 ],(0,2))
    counter_test_positivi += tester_fun(Ex1, [ [],2],(-1,-1))
    counter_test_positivi += tester_fun(Ex1, [ [9, 3, 5, 5, 2, 8], 4 ],(1,4))
    counter_test_positivi += tester_fun(Ex1, [[-3, 1],4 ],(0,1))
    counter_test_positivi += tester_fun(Ex1, [[3, 5, 7, 2, 8],100 ],(0,4))
    
   
    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
