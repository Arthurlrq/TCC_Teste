import numpy as np
import glob

for filename in glob.glob("*.*"):
    if '.npy' in filename:
        predicoes = np.load(filename)
        print(filename)

np.save('predicoes_texto',predicoes)