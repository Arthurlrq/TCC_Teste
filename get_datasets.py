import numpy as np
import glob
import h5py

for filename in glob.glob("*.*"):
    #
    if 'rank' in filename:
        print("--------------------------")
        dataset = h5py.File(filename, 'r')
        print(filename)
        print(dataset.keys())
        print(dataset['rpkm'])
        #
        arquivo = open("datasets.txt", "a")
        arquivo.write("--------------------------")
        arquivo.write(filename)
        arquivo.write(dataset.keys())
        arquivo.write(dataset['rpkm'])

    #
    if 'bulk' in filename:
        print("--------------------------")
        dataset = h5py.File(filename, 'r')
        print(filename)
        print(dataset.keys())
        print(dataset['rpkm'])
        #
        arquivo = open("datasets.txt", "a")
        arquivo.write("--------------------------")
        arquivo.write(filename)
        arquivo.write(dataset.keys())
        arquivo.write(dataset['rpkm'])

    #
    if 'bone' in filename:
        print("--------------------------")
        dataset = h5py.File(filename, 'r')
        print(filename)
        print(dataset.keys())
        print(dataset['RPKMs'])
        #
        arquivo = open("datasets.txt", "a")
        arquivo.write("--------------------------")
        arquivo.write(filename)
        arquivo.write(dataset.keys())
        arquivo.write(dataset['RPKMs'])

    #
    if 'dendritic' in filename:
        print("--------------------------")
        dataset = h5py.File(filename, 'r')
        print(filename)
        print(dataset.keys())
        print(dataset['RPKMs'])
        #
        arquivo = open("datasets.txt", "a")
        arquivo.write("--------------------------")
        arquivo.write(filename)
        arquivo.write(dataset.keys())
        arquivo.write(dataset['RPKMs'])

    #
    if 'mesc' in filename:
        print("--------------------------")
        dataset = h5py.File(filename, 'r')
        print(filename)
        print(dataset.keys())
        print(dataset['RPKMs'])
        #
        arquivo = open("datasets.txt", "a")
        arquivo.write("--------------------------")
        arquivo.write(filename)
        arquivo.write(dataset.keys())
        arquivo.write(dataset['RPKMs'])















        #
        #print("Keys: %s" % dataset.keys())
        #a_group_key = list(dataset.keys())[0]
        #
        #data = list(dataset[a_group_key])
        #print(data)
        #


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