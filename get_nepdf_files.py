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
        fig, ax = subplots(figsize=(10,10)) # TIRA ISSO AQI EM
        ax.imshow(img_array, interpolation='none')
        plt.show()
        plt.tight_layout()
        plt.savefig(img_name)
        #
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