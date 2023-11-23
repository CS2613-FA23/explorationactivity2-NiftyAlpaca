
#%%
import numpy as np
from skimage import io;
from skimage.color import rgb2hsv;
from skimage.morphology import skeletonize
from skimage.util import invert
import matplotlib.pyplot as plt;
import picfunc as pf
import glob

done = False
imageList = glob.glob("*.jpg")

##Feel free to add any JPG image you want! It just has to be in the same folder as the code
print("Choose an image from the list: ")
for i in range(len(imageList)):
    print(str(i) + " " + imageList[i])

index =int(input())
print(str(index))
try:
    photo = io.imread(imageList[index])
except:
    print("Choose an image from the list: ")
    for i in range(len(imageList)):
        print(str(i) + " " + imageList[i])
        index =int(input())

originalPhoto = photo

plt.imshow(photo)
plt.show()
print("Select an option: ")
print("     1. Decrease Resolution")
print("     2. Crop Picture")
print("     3. Flip Picture")
print("     4. Get Stats")
print("     5. Change Color Scheme")
print("     6. Skeletonize")
print("     0. Quit")
while(not done):
    try:
        option = int(input())
        print(str(option))
    except:
        print("Invalid value")
        break
    if(option == 0):
        done = True
        print("Save? (Y/N)")
        YN = str(input())
        if(YN == "Y"):
            print("What do you want to name the picture file? Please include jpg extension")
            response = str(input())
            print(response)
            if(".jpg" not in response):
                print("please make sure file name has .jpg extension")
                response = str(input())
                print(response)
            io.imsave(response, photo)
            print("QUIT")
            break
        else:
            print("QUIT")
            break
    elif(option == 1):
        print("Input magnitude to decrease resolution as integer")
        try:
            num = int(input())
            print(str(num))
        except:
            print("Invalid value")
            break
        print(num)
        photo = pf.skipPixels(photo,num)
        plt.imshow(photo)
    elif(option == 2):
        print("Give input in form 'r1,r2,c1,c2' ")
        val = str(input())
        print(val)
        x = val.split(',')
        photo = pf.cropPictureInRange(photo, int(x[0]), int(x[1]),int(x[2]),int(x[3]))
        plt.imshow(photo)
    elif(option == 3):
        photo = photo[::-1]
        plt.imshow(photo)
    elif(option == 4):
        print(" ")
        print("Sum: " + str(np.sum(photo)))
        print("Average: " + str(np.average(photo)))
        print("Max: " + str(np.max(photo)))
        print("Min: " + str(np.min(photo)))
        print(" ")
    elif(option == 5):
        print("\n Select an option:")
        print("\t 1.HSV")
        print("\t 2.Hue")
        print("\t 3.Value Channel")
        
        select = int(input())
        hsv_img = rgb2hsv(originalPhoto)
        if(select == 1):
            photo = hsv_img
        elif(select == 2):
            photo = hsv_img[:,:,0]
        elif(select == 3):
            photo = hsv_img[:,:,2]
        
        plt.imshow(photo)
    elif(option == 6):
         print("loading...may take a while")
         photo = invert(photo)
         photo = skeletonize(photo)
         plt.imshow(photo)    
    plt.show()
    print("Select an option: ")
    print("     1. Decrease Resolution")
    print("     2. Crop Picture")
    print("     3. Flip Picture")
    print("     4. Get Stats")
    print("     5. Change Color Scheme")
    print("     6. Skeletonize")
    print("     0. Quit")


1# %%

