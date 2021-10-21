import numpy as np
import glob

for filename in glob.glob("*.*"):
    if '.npy' in filename:
        predicoes = np.load(filename)
        print(predicoes)

np.savetxt('predicoes_texto',predicoes)