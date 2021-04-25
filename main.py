import regularGrammar as  reg
import sys


options = list(sys.argv)[1:]            # iau optiuni din cmd line daca exista
wordGen = reg.RegularGrammar()
file_path = ''

for i in range(0, len(options) - 1):    # setez optiunile din cmd line
    if options[i] == '-t' and (options[i+1] == 'left' or options[i+1] == 'right'):
        wordGen.setType(options[i+1])
    elif options[i] == '-f':
        file_path = options[i+1]


wordGen.setNonterminals(input('\nNeterminale (litere mari separate prin spatiu): ').split())
wordGen.setTerminals(input('\nTerminale (litere mici separate prin spatiu): ').split())
wordGen.setStartSymbol(input('\nSimbol start: '))

nrProd = int(input('\nNumar productii: '))
for i in range(nrProd):
    prod = input('\nProdutie ( <simbol> = <string>[|<string>...] $ = lambda) ')
    
    simbol = prod.split('=')[0].strip()                                         
    strings = [string.strip() for string in prod.split('=')[1].strip().split('|')]
    
    wordGen.addProduction(simbol, strings)


ok = True

while ok:
    n = input('\nLungime maxima: ')
    if n.find('-') != -1:
        min_len, max_len = map(int, n.split('-'))
    else:
        min_len = max_len = int(n)
        
    if file_path != '':
        wordGen.printWords(min_len, max_len , file_path)
    else:
        wordGen.printWords(min_len, max_len)
    ok = True if input('\nIntroduceti alta lungime maxima? (y/n)') == 'y' else False
