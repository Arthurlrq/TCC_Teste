import numpy as np
import glob
import h5py

for filename in glob.glob("*.*"):
    if '.h5' in filename:
        #
        dataset = h5py.File(filename, 'r')
        list(dataset.keys())
        #
        #print(dataset)
        #dataset_name = filename
        #np.savetxt(dataset_name,dataset)

