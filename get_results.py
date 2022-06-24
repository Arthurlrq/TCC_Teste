# PEGA AS SAIDAS DA REDE E SALVA EM UM ARQUIVO DE TEXTO
# AS SAIDAS DA REDE SAO 3 PROBABILIDADADES (LABELS) PARA CADA PAR DA LISTA DE PARES DE GENES

#
import numpy as np
import glob

#
for filename in glob.glob("*.*"):
    if '.npy' in filename:
        results = np.load(filename)
        print(results)

#
np.savetxt('results.txt',results)