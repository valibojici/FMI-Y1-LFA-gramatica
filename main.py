from collections import defaultdict

class WordGenerator:
    def __init__(self):
        self.productions = defaultdict(set)
        # dictionar -> cheie = neterminal; valoare = set de stringuri (terminale + 1 neterminal optional)
        self.nonterminals = set()
        self.terminals = set()
        self.startSymbol = ''
    
    def setStartSymbol(self, symbol):
        self.startSymbol = symbol
    
    def setTerminals(self, terminals):
        self.terminals = set(terminals)

    def setNonterminals(self, nonterminals):
        self.nonterminals = set(nonterminals)

    def addProduction(self, symbol, strings):
        if symbol not in self.nonterminals:
            self.nonterminals.add(symbol)
        self.productions[symbol].update(strings)


    def wordGen(self, n):
        result = ['' for _ in range(n+1)]
        print(self.nonterminals, self.productions)
        def bkt(step, curr_len, symbol):
            for string in self.productions[symbol]:
                nonterminal = string[-1]
                if nonterminal == '$' or nonterminal not in self.nonterminals:
                    result[step] = '' if nonterminal == '$' else string
                    
                    if len(result[step]) + curr_len <= n:
                        if step == 0 and result[0] == '':
                            yield '$'
                        else:
                            yield ''.join(result[:step+1])
                else:
                    result[step] = string[:-1]

                    if len(result[step]) + curr_len <= n:
                        for word in bkt(step+1, len(result[step]) + curr_len, nonterminal):
                            yield word


        return bkt(0, 0, self.startSymbol)    

    # def wordGen(self, n):
    #     stack = [(0, 0, self.startSymbol)]  # stiva pentru argumentele din backtracking
    #     result = ['' for _ in range(n+1)]     # lista in care pun cuvintele(nu litere) din backtracking (are cel mult lungime n)
        
    #     while len(stack) > 0:           # backtracking dar iterativ nu recursiv
    #         step = stack[-1][0]         # al catelea pas din backtracking
    #         curr_len = stack[-1][1]     # lungime curenta a cuvantului format pana acum
    #         symbol = stack[-1][2]       # simbolul (neterminal) la care suntem acum  
    #         stack.pop()

    #         for string in self.productions[symbol]:         # iterez prin toate productiile posibile cu simbolul curent
    #             nonterminal = string[-1]                    # neterminalul daca exista e ultima litera
    #             # print('nonterminal :',nonterminal, string[:-1])
    #             if nonterminal == '$' or nonterminal not in self.nonterminals:    
    #                 #  daca neterminalul nu exista (terminal sau lambda pe ultima poz)
    #                 result[step] = '' if nonterminal == '$' else string[0:-1]  #  atunci adaug tot stringul la rezultat
                    
    #                 if len(result[step]) + curr_len <= n:   
    #                         print(*result[:step+1],sep='')              # daca lungimea cuvintelor concatenate este < n atunci afisez                            
    #             else:
    #                 result[step] = string[0:-1]              # altfel adaug tot stringul fara neterminalul de pe ultima poz
    #                 if len(result[step]) + curr_len <= n:
    #                     stack.append((step+1,len(result[step]) + curr_len, nonterminal))  # backtracking mai departe 





c = WordGenerator()

stack = [0 for _ in range(100)]

nonterminals = set(('S', 'A'))


productii = {
    'S' : ['abS', 'cA', 't'],
    'A' : ['aA', 'x']}

# def bkt(k, curr_len, max_len, symbol):
    
#     global stack, nonterminals, productii

#     if symbol not in nonterminals:
#         if k == 1 and stack[1] == '':
#             print('$')
#         else:
#             print(*stack[:k],sep='')
#     else:
#         for prod in productii[symbol]:
#             curr_symbol = prod[-1]
#             curr_word = prod[:-1] if curr_symbol in nonterminals else prod
            
#             if curr_word == '$':
#                 curr_word = ''

#             stack[k] = curr_word
#             if curr_len + len(curr_word) <= max_len:
#                 bkt(k+1, curr_len + len(curr_word), max_len, curr_symbol)


# bkt(0, 0, 6, 'S')
c.setNonterminals(['S'])
c.setStartSymbol('S')
c.addProduction('S', ['abS','cA' ,'$'])
c.addProduction('A', ['aA', 'x'])

wgen = c.wordGen(2000)

for word in wgen:
    print(word)
