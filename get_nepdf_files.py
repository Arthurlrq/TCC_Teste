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
        plt.figure(figsize = (64,32))
        plt.imshow(img_array, interpolation='nearest')
        plt.show()
        plt.savefig(img_name)
        #
        print(filename)




        # PROXIMO
        #fig = plt.figure()
        #ax = fig.add_subplot(2,2,1) 
        #ax.imshow(img_array, interpolation='nearest')
        #plt.show()
        #plt.savefig(img_name)

#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.imshow(img_array, interpolation='nearest')
#ax.set_aspect(5)
#plt.show()
#plt.savefig(img_name)

#plt.imshow(img_array, interpolation='nearest', origin='upper')
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