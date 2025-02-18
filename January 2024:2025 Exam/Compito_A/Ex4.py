def veroFalso():
    ##############################################################################################
    # Modificare il valore di ris elencando le lettere delle domande che valutate essere vere
    # Ad esempio, se pensate che B, C, e D siano vere ris deve valere 'BCD'
    ##############################################################################################

    d=eval(open('VeroFalsoA.txt',encoding="UTF-8").read())
    
    #################### modificare solo il valore di ris ###############
    ris= 'ABCCDEFGH'
    #####################################################################
    
    for dom in 'ABCDEFGH':
        print(dom+')', end='')
        print(d[dom]['premessa'])
        print(d[dom]['domanda'])
        if dom in ris.upper():
            print('VERA')
        else:
            print('FALSA')
        print()
    return ris

veroFalso()
print('**** Modificare il valore di ris ****')
