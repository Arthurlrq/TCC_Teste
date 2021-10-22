import numpy as np
import glob

for filename in glob.glob("*.*"):
    if '.h5' in filename:
        dataset = np.load(filename)
        print(dataset)
        dataset_name = filename
        np.savetxt(dataset_name,dataset)