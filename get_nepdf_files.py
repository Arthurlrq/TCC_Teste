import glob
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
#from skimage.transform import resize

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
        #img_array = resize(img_array, (256,128))
        plt.imshow(img_array, aspect='auto', interpolation='nearest', origin='upper')
        #plt.imshow(img_array, cmap="gray", vmin=0, vmax=255)
        plt.show()
        img_name = filename+".png"
        matplotlib.image.imsave(img_name, img_array)
        print(filename)

#for filename in glob.glob("*.*"):
#    if 'ydata' in filename:
#        labels = np.load(filename)
#        #print(labels)
#np.savetxt('labels',labels)
#
#for filename in glob.glob("*.*"):
#    if 'zdata' in filename:
#        genes = np.load(filename)
#        #print(genes)
#np.savetxt('genes',genes)