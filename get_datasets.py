import numpy as np
import glob
import h5py

for filename in glob.glob("*.*"):
    if 'bulk' in filename:
        #
        print("--------------------------")
        dataset = h5py.File(filename, 'r')
        #list(dataset.keys())
        print(filename)
        print(dataset.keys())
        print(dataset['rpkm'])
        #
        #print(dataset)
        #dataset_name = filename
        #np.savetxt(dataset_name,dataset)
#
#for filename in glob.glob("*.*"):
#    if 'bone' in filename:
#        print("--------------------------")