from json import tool
import math
import csv

from bokeh.plotting import figure, show
from bokeh.models import Panel, Tabs, ranges, HoverTool, DatetimeTickFormatter
from bokeh.palettes import all_palettes

from rich.console import Console
import rich.traceback

console = Console()
console.clear()
rich.traceback.install()

#Sekcja wczytywania danych
with open('dane_covid.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ";")
    dane_csv = []
    line_count = 0
    for row in csv_reader:
        if line_count == 0:    
            line_count += 1
        else:
            line_count += 1
            dane_csv.append(row)
    console.print(f'Processed {line_count} lines.')

dataDict = dict()
terDict = dict()
sexDict = dict()
woj = ['Dolnyśląskie','Kujawsko-Pomorskie','Lubelskie','Lubuskie','Łódzkie','Małopolskie','Mazowieckie','Opolskie','Podkarpackie','Podlaskie','Pomorskie','Śląskie','Świętokrzyskie','Warmińsko-Mazurskie','Wielkopolskie','Zachodnio-Pomorskie']

for elem in dane_csv:
    if elem[0] in dataDict:
        dataDict[elem[0]] +=1
    else:
        dataDict[elem[0]] = 1
    if int(elem[1]) in terDict:
        terDict[int(elem[1])] +=1
    else:
        terDict[int(elem[1])] = 1
    if elem[3] in sexDict:
        sexDict[elem[3]] +=1
    else:
        sexDict[elem[3]] = 1

#Zamiana nazw
n = 2
for i in woj:
    terDict[i] = terDict.pop(n)
    n+=2

#Sekcja rysowania wykresów
HOVER_TOOLTIPS = [("(x,y)", "(@x, @y)")]

graph1 = figure(
    title = "Zgony/daty",  
    plot_width=600, 
    plot_height=600,
    #x_axis_type='datetime',
    x_range=list(dataDict.keys()),
    y_range= ranges.Range1d(start=0,end=len(list(dataDict.keys()))),
    x_axis_label ='Daty', 
    y_axis_label='Zgony', 
    sizing_mode = 'stretch_width',
    tools = "box_select,zoom_in,zoom_out,save,reset",
    tooltips = HOVER_TOOLTIPS,
)

graph1.circle(
    x = list(dataDict.keys()),
    y = list(dataDict.values()), 
    line_color='green',
)

graph1.toolbar.logo = None
graph1.toolbar.autohide = True
graph1.add_tools(HoverTool(tooltips=HOVER_TOOLTIPS))
#graph1.xaxis[0].formatter = DatetimeTickFormatter(months="%b %Y")
graph1.xaxis.major_label_orientation = math.pi/4

tab1 = Panel(child=graph1, title="Zgony/daty")


graph2 = figure(
    title = "Zgony/województwa", 
    plot_width=600, 
    plot_height=600, 
    x_range = list(terDict.keys()),
    sizing_mode = 'stretch_width',
)
graph2.vbar(
    x = list(terDict.keys()), 
    top = list(terDict.values()), 
    width = 0.5,
    fill_color = all_palettes['Turbo'][256][0]
)
graph2.xaxis.major_label_orientation = math.pi/4
tab2 = Panel(child=graph2, title="Zgony/województwa")

graph3 = figure(
    plot_width=600, 
    plot_height=600, 
    x_range = list(sexDict.keys()),
    y_range= ranges.Range1d(start=0,end=len(list(sexDict.keys()))),
    sizing_mode = 'fixed',
)

graph3.vbar(
    x = list(sexDict.keys()), 
    top = list(sexDict.values()), 
    line_color='red', 
    width=0.9
)
tab3 = Panel(child=graph3, title="Zgony/płeć")

all_tabs = Tabs(tabs=[tab1, tab2, tab3])
#all_tabs = Tabs(tabs=[tab1])
show(all_tabs)