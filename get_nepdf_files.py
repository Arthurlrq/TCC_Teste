import glob
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

"""
for filename in glob.glob("*.*"):
    if 'Nxdata' in filename:
        nx_array = np.load(filename)
        img_array = nx_array[0,:,:,:]
        img_array = img_array.squeeze()
        img_name = filename+".png"
        #
        fig = plt.figure(figsize = (10,10))
        ax = fig.add_subplot(111)
        #
        ax.imshow(img_array, interpolation='none')
        plt.show()
        plt.tight_layout()
        plt.savefig(img_name)
        #
        print(filename)
"""

for filename in glob.glob("*.*"):
    if 'ydata' in filename:
        label = np.load(filename)
        label_name = filename+'.txt'
        print(filename)
        print(label)
        np.savetxt(label_name,label)

for filename in glob.glob("*.*"):
    if 'zdata' in filename:
        genes = np.load(filename)
        genes_name = filename+'.txt'
        print(filename)
        print(genes)
        np.savetxt(genes_name,genes)