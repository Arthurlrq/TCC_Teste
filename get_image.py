import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import glob

for filename in glob.glob("*.*"):
    #if '.npy' in filename:
    if 'Nxdata' in filename:
        #print(filename.shape)
        nx_array = np.load(filename)
        #print(nx_array.shape)
        img_array = nx_array[0,:,:,:]
        #print(img_array.shape)
        img_array = img_array.squeeze()
        #print(img_array.shape)
        plt.imshow(img_array)
        #plt.imshow(img_array, cmap="gray", vmin=0, vmax=255)
        plt.show()
        img_name = filename+".png"
        matplotlib.image.imsave(img_name, img_array)
        print(filename)

#print("DIVISAAAAAO MALUUUCAAAAAA")

#for filename in glob.glob("*.*"):
#    if 'zdata' in filename:
#        nx_array = np.load(filename)
#        print(nx_array.shape)
#        print(filename)