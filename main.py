import wordGenerator as  wg
import sys

options = list(sys.argv)[1:]
wordGen = wg.WordGenerator()
file_path = ''

for i in range(0, len(options) - 1):
    if options[i] == '-t' and (options[i+1] == 'left' or options[i+1] == 'right'):
        wordGen.setType(option[i+1])
    elif options[i] == '-f':
        file_path = options[i+1]


wordGen.setNonterminals(input('nonterminale : ').split())
wordGen.setTerminals(input('terminale : ').split())
wordGen.setStartSymbol(input('start : '))

nrProd = int(input('nrprod = '))
for i in range(nrProd):
    prod = input('productie : ')
    prod = prod.split(' ')
    
    wordGen.addProduction(prod[0], prod[1].strip().split('|'))


n = int(input('n = '))

if file_path != '':
    wordGen.printWords(n, file_path)
else:
    wordGen.printWords(n)
