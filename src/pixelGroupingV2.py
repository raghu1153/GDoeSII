import numpy as np
from scipy import misc
import pylab as py
from gdsCAD import *
from tqdm import *

fileLoc = "C:/Users/Raghu/Desktop/Test.jpeg"
imArray = misc.imread(fileLoc, flatten= 1)
maxVal = np.max(imArray)
minVal = np.min(imArray)
bins = []
levels = 2
for b in range(levels+1):
    interval = (maxVal-minVal+1)/float(levels)
    bins.append(minVal+b*interval)
mask = np.digitize(imArray, bins)
imArray = mask -1
# py.imshow(imArray)
# py.show()

def gA2(im):
    rows = np.shape(im)[0]
    cols = np.shape(im)[1]
    check = np.zeros((rows,cols))
    cell = core.Cell('GDSII')
    layout = core.Layout('Test',1e-6)
    print rows,cols
    for i in tqdm(range(rows)):
        for j in range(cols):
            a = 1
            if check[i,j] == 1:
                    continue
            elif im[i,j] == 0:
                continue
            else:
                while(i+a < rows and j+a < cols):
                    if np.sum(im[i:i+a,j:j+a]) == a**2:
                        a = a + 1
                    else:
                        break
                while(np.sum(check[i:i+a-1,j:j+a-1]) != 0):
                    a = a-1    
                if a == 2:
                    cell.add(core.Path([(j,rows-i-0.5),(j+a-1,rows-i-0.5)]))
                    check[i:i+a-1,j:j+a-1] = 1
                else:
                    cell.add(shapes.Rectangle((j,rows-i),(j+a-1,rows-(i+a-1))))
                    check[i:i+a-1,j:j+a-1] = 1
            j = j+a-1
    flatCell = core.Cell('GDSII Flat')
    flatCell.add(cell.flatten())
    layout.add(flatCell)
    layout.save('C:/Users/Raghu/Desktop/sample.gds')
                 
gA2(imArray)