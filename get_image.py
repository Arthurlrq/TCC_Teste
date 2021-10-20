import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import glob

for filename in glob.glob("*.*"):
    #if '.npy' in filename:
    if 'Nxdata' in filename:
        #print(filename.shape)
        img_array = np.load(filename)
        print(img_array.shape)
        img_array = img_array.squeeze()
        plt.imshow(img_array, cmap="gray")
        plt.show()
        img_name = filename+".png"
        matplotlib.image.imsave(img_name, img_array)
        #print(filename)