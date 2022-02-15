import requests, re, time
from bs4 import BeautifulSoup
from os.path  import basename
import multiprocessing as mp

from rich.console import Console
console = Console()

#import numpy as np
#from PIL import Image

def download_image():
    url = 'http://www.if.pw.edu.pl/~mrow/dyd/wdprir/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    url_tab = []
    for a in soup.find_all("a" , href=True):
        if re.findall(r".png",a['href']): 
            lnk = url + a['href']
            url_tab.append(lnk)
    return url_tab

def save_image(url_tab):
    for lnk in url_tab:
        with open(basename(lnk), "wb") as f:
            f.write(requests.get(lnk).content)
            console.print(f'{f} done')

if __name__ == '__main__':
    start = time.time()
    ix = download_image()
    #save_image(ix)

    p = mp.Process(target = save_image, args = (ix,))
    p.start()
    p.join()
    
    stop = time.time()
    console.print(f'{stop - start = }')

        

'''
def change_image(i):
    im = np.array(Image.open(i).convert('L'))
    Image.fromarray(im).save(i)
'''
        