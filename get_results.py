import numpy as np
import glob

for filename in glob.glob("*.*"):
    if '.npy' in filename:
        results = np.load(filename)
        print(results)

np.savetxt('results.txt',results)