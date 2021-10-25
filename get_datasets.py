import numpy as np
import glob
import h5py

for filename in glob.glob("*.*"):
    if 'bulk' in filename:
        #
        print("Keys: %s" % dataset.keys())
        a_group_key = list(dataset.keys())[0]
        #
        data = list(dataset[a_group_key])
        print(data)
        #
        #print("--------------------------")
        #dataset = h5py.File(filename, 'r')
        #list(dataset.keys())
        #print(filename)
        #print(dataset.keys())
        #print(dataset['rpkm'])
        #
        #print(dataset)
        #dataset_name = filename
        #np.savetxt(dataset_name,dataset)

#with h5py.File(filename, "r") as f:
    # List all groups
    #print("Keys: %s" % f.keys())
    #a_group_key = list(f.keys())[0]

    # Get the data
    #data = list(f[a_group_key])




#for filename in glob.glob("*.*"):
#    if 'bone' in filename:
#        print("--------------------------")