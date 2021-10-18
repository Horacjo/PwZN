import argparse
import os
import nltk
from collections import defaultdict
from yaml import parse
from ascii_graph import Pyasciigraph

parser = argparse.ArgumentParser(description="Opis:")
parser.add_argument('file', help = "Użytkowniku podaj nazwę pliku do oczytania")
parser.add_argument('-n','--number', help = "Użytkowniku podaj liczbę dla ilu wyrazów histogram wyświetlić (domyślnie 10)", type = int, default=10)
parser.add_argument('-his','--histogram', help = "Użytkowniku podaj liczbę określającą minimalną długość histogramowanego słowa (domyślnie 0)", type = int, default=10)
args = parser.parse_args()

print(f'File name: {args.file}')
print(f'Number of worlds: {args.number}')
print(f'Min of histogram: {args.histogram}')

with open(os.path.join(r'C:\Users\Widokowa\Desktop\PwZN_1',f'{args.file}'), encoding='utf8') as f:
    
    dict = defaultdict(int)
    
    words = f.read()
    world_list = nltk.tokenize.word_tokenize(words)

    for i in world_list:
        if i.isalpha():
            dict[i] +=1
   
    #Tworzenie danych i sortowanie ich
    graph = Pyasciigraph(
        line_length=120,
        min_graph_length=args.number,
        separator_length=4,
        graphsymbol='*',
        float_format='{0:,.2f}',
        force_max_value=2000,
    )

    data = [(f'{i}', dict[i]) for i in dict]
    data.sort(key=lambda e:e[1], reverse=True)

    #Rysowanie histogramu
    for line in graph.graph(f'Histogram {args.file = }', data):
        print(line) 
    