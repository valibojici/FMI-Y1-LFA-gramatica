from collections import defaultdict

class WordGenerator:
    def __init__(self, type = 'right'):
        self.productions = defaultdict(set)
        # dictionar -> cheie = neterminal; valoare = set de stringuri (terminale + 1 neterminal optional)
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
            for char in string:
                if char != '$' and (char not in self.nonterminals and char not in self.terminals):
                    raise invalidLetter(char)

        self.productions[symbol].update(strings)


    def wordGen(self, n):
        words = defaultdict(list)

        result = ['' for _ in range(n+1)]
        
        def bkt(step, curr_len, symbol):
            for string in self.productions[symbol]:
                nonterminal = string[-1] if self.type == 'right' else string[0]

                if nonterminal == '$' or nonterminal not in self.nonterminals:
                    result[step] = '' if nonterminal == '$' else string
                    
                    if len(result[step]) + curr_len <= n:
                        if step == 0 and result[0] == '':
                            words[0].append('$')
                        else:
                            word = ''.join(result[:step+1])
                            words[len(word)].append(word)
                else:
                    result[step] = string[:-1] if self.type == 'right' else string[1:]

                    if len(result[step]) + curr_len <= n:
                        bkt(step+1, len(result[step]) + curr_len, nonterminal)

        bkt(0,0,self.startSymbol)
        return words

    def printWords(self, max_length, file_path = None):
        wordDict = self.wordGen(max_length)
        
        if file_path is not None:
            with open(file_path, 'w') as g:
                for len, words in sorted(wordDict.items()):
                    g.write(f'{len} ->' + str(words) + '\n')
        else:
            for len, words in sorted(wordDict.items()):
                    print(f'{len} ->',words)


class invalidLetter(Exception):
    def __init__(self, letter):
        super().__init__(f'{letter} is not terminal or nonterminal')