import argparse
import os
import nltk
from random import randint
from collections import defaultdict
from yaml import parse
from ascii_graph import Pyasciigraph
from ascii_graph.colors import *
from ascii_graph.colordata import vcolor

parser = argparse.ArgumentParser(description="Opis:")
parser.add_argument('file', help = "Użytkowniku podaj nazwę pliku do oczytania")
parser.add_argument('-n','--number', help = "Użytkowniku podaj liczbę dla ilu wyrazów histogram wyświetlić (domyślnie 10)", type = int, default=10)
parser.add_argument('-his','--histogram', help = "Użytkowniku podaj liczbę określającą minimalną długość histogramowanego słowa (domyślnie 0)", type = int, default=10)
args = parser.parse_args()

print(f'File name: {args.file}')
print(f'Number of worlds: {args.number}')
print(f'Min of histogram: {args.histogram}')

with open(f'{args.file}', encoding='utf8') as f:
    
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)
    
    words = f.read()
    world_list = nltk.tokenize.word_tokenize(words)

    for i in world_list:
        if i.isalpha():
            dict1[i] +=1
   
    for i in dict1:
        if len(i) >= args.histogram:
            dict2[i] = dict1[i]

    #Tworzenie danych i sortowanie ich
    graph = Pyasciigraph()

    pattern = [Yel, Cya, Pur]
    data = vcolor([(f'{i}', dict2[i]) for i in dict2], pattern)
    data.sort(key=lambda e:e[1], reverse=True)

    #Rysowanie histogramu
    for line in graph.graph(f'Histogram {args.file = }', data[:int(args.number)]):
        print(line) 
    