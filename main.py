import wordGenerator as  wg
import sys

options = list(sys.argv)[1:]            # iau optiuni din cmd line daca exista
wordGen = wg.WordGenerator()
file_path = ''

for i in range(0, len(options) - 1):    # setez optiunile din cmd line
    if options[i] == '-t' and (options[i+1] == 'left' or options[i+1] == 'right'):
        wordGen.setType(options[i+1])
    elif options[i] == '-f':
        file_path = options[i+1]


wordGen.setNonterminals(input('Neterminale (litere mari separate prin spatiu): ').split())
wordGen.setTerminals(input('Terminale (litere mici separate prin spatiu): ').split())
wordGen.setStartSymbol(input('Simbol start: '))

nrProd = int(input('Numar productii: '))
for i in range(nrProd):
    prod = input('Produtie ( <simbol> = <string>[|<string>...] $ = lambda) ')
    
    simbol = prod.split('=')[0].strip()                                         
    strings = [string.strip() for string in prod.split('=')[1].strip().split('|')]
    
    wordGen.addProduction(simbol, strings)


n = int(input('Lungime maxima: '))

if file_path != '':
    wordGen.printWords(n, file_path)
else:
    wordGen.printWords(n)
