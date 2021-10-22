import glob
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

for filename in glob.glob("*.*"):
    if 'Nxdata' in filename:
        nx_array = np.load(filename)
        img_array = nx_array[0,:,:,:]
        img_array = img_array.squeeze()
        img_name = filename+".png"
        #
        plt.imshow(img_array, interpolation='nearest', origin='upper')
        plt.show()
        plt.savefig(img_name)
        #
        print(filename)

#matplotlib.image.imsave(img_name, img_array)
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