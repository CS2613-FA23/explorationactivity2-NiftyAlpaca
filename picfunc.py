import numpy as np
from skimage import io;
import matplotlib.pyplot as plt;

##This method lowers the resolution by a integer magnitude, lowering the amount of pixels allowed into the pool.
## If the integer is 1, then every second pixel (an element in the nd array) will be exluded from the returning data type.

def skipPixels(photo, numToSkip):
    num = numToSkip + 1
    return photo[::num, ::num]
    
##Crops pictures based on given row or column ranges
def cropPictureInRange(photo, startRow, endRow, startCol, endCol):
    return photo[startRow:endRow,startCol:endCol]
    