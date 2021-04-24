from collections import defaultdict

class WordGenerator:
    def __init__(self, type = 'right'):
        self.productions = defaultdict(set)     # dictionar -> cheie = neterminal; valoare = set de stringuri (terminale + 1 neterminal optional)
        self.nonterminals = set()
        self.terminals = set()
        self.startSymbol = ''
        self.type = type
    
    def setType(self, type):
        self.type = type

    def setStartSymbol(self, symbol):
        self.startSymbol = symbol
    
    def setTerminals(self, terminals):
        self.terminals = set(terminals)

    def setNonterminals(self, nonterminals):
        self.nonterminals = set(nonterminals)

    def addProduction(self, symbol, strings):
        if symbol not in self.nonterminals:
            self.nonterminals.add(symbol)
        
        for string in strings:                            
            for index, letter in enumerate(string):     # testez daca literele sunt neterminale sau terminale si sunt puse unde trebuie
                if letter == '$':
                    continue
                if letter not in self.nonterminals and letter not in self.terminals:
                    raise badProduction(f'{letter} not a terminal or nonterminal')
                elif letter in self.nonterminals:
                    if self.type == 'left' and index != 0:
                        raise badProduction(f'{letter} not at start')
                    elif self.type == 'right' and index != len(string) - 1:
                        raise badProduction(f'{letter} not at end')
        
        self.productions[symbol].update(strings)


    def wordGen(self, n):
        words = defaultdict(set)                # dictionar in care pun cuvintele generate

        result = ['' for _ in range(n+1)]       # 'stiva' in care generez cu backtracking partile din cuvinte
        
        def bkt(step, curr_len, symbol):
            for string in self.productions[symbol]:
                nonterminal = string[-1] if self.type == 'right' else string[0]     # neterminalul este ori la inceput ori la final

                if nonterminal == '$' or nonterminal not in self.nonterminals:      # daca nu exista neterminal (ultima sau prima litera e lambda sau terminal)
                    result[step] = '' if nonterminal == '$' else string             # daca e lambda pun '' in loc de $
                    
                    if len(result[step]) + curr_len <= n:                           # daca lungimea cuv format pana acum e <= ca n atunci afisez
                        word = ''.join(result[:step+1])
                        words[len(word)].add(word)
                else:                                                                   # daca exista neterminal la inceput sau sfarsit
                    result[step] = string[:-1] if self.type == 'right' else string[1:]  # iau stringul fara neterminal

                    if len(result[step]) + curr_len <= n:                               # daca lungimea curenta e inca <= ca n atunci continui cu backtrackingul
                        bkt(step+1, len(result[step]) + curr_len, nonterminal)

        bkt(0,0,self.startSymbol)
        return words

    def printWords(self, max_length, file_path = None):
        # functie care printeaza toate cuvintele de maxim max_length litere pe console sau in fisier
        wordDict = self.wordGen(max_length)
        
        if file_path is not None:                               # daca file_path exista atunci afisez in fisier
            with open(file_path, 'w') as g:
                for len, words in sorted(wordDict.items()):
                    g.write(f'{len} -> ' + str(words) + '\n')
        else:                                                   # altfel afisez pe consola
            for len, words in sorted(wordDict.items()):
                    print(f'{len} ->',words)


class badProduction(Exception):
    def __init__(self, msg):
        super().__init__(msg)