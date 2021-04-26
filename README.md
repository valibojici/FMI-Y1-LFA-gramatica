# Generare cuvinte gramatica regulata
Pentru o gramatica regulata, sa se genereze toate cuvintele avand o lungime maxima data.

Pentru gramatica liniara la stanga (implicit la dreapta)
```
python main.py -t left
```

Pentru citire din fisier (implicit in consola)
```
python main.py -f <file_path>
```

Lungimea maxima poate sa fie un numar sau un range (de ex. 2-4)
```
Lungime maxima: 2-4
2 -> ['aa', 'bb']
3 -> []
4 -> ['abca', 'abba', 'abbc']
```
