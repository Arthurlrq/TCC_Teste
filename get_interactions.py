import numpy as np
from matplotlib import pyplot as plt

arquivo_interacoes = open('results.txt')
interacoes = arquivo_interacoes.readlines()

inter_list = []

for interacao in interacoes:
	inter = interacao.split()[0]
	inter = 1 - float(inter)
	inter_list.append(inter)

#
media = np.average(inter_list)
#
variancia = np.var(inter_list)
#
desvio = np.std(inter_list)
#
maximo = max(inter_list)
#
minimo = min(inter_list)

#
arquivo_inter = open('interactions.txt', 'w')
arquivo_inter.write("Média entre as chances de interação: ")
arquivo_inter.write(str(media))
arquivo_inter.write('\n')
#
arquivo_inter.write("Variância das chances de interação: ")
arquivo_inter.write(str(variancia))
arquivo_inter.write('\n')
#
arquivo_inter.write("Desvio padrão das chances de interação: ")
arquivo_inter.write(str(desvio))
arquivo_inter.write('\n')
#
arquivo_inter.write("Máximo entre as chances de interação: ")
arquivo_inter.write(str(maximo))
arquivo_inter.write('\n')
#
arquivo_inter.write("Mínimo entre as chances de interação: ")
arquivo_inter.write(str(minimo))
arquivo_inter.write('\n')

#
arquivo_inter.write("Chances de interação: ")
arquivo_inter.write('\n')
for inter in inter_list:
	arquivo_inter.write(str(inter))
	arquivo_inter.write('\n')

#
num_00 = 0
num_01 = 0
num_02 = 0
num_03 = 0
num_04 = 0
num_05 = 0
num_06 = 0
num_07 = 0
num_08 = 0
num_09 = 0

#
for inter in inter_list:
	if inter < 0.1:
		num_00 = num_00 + 1
	elif inter >= 0.1 and inter < 0.2:
		num_01 = num_01 + 1
	elif inter >= 0.2 and inter < 0.3:
		num_02 = num_02 + 1
	elif inter >= 0.3 and inter < 0.4:
		num_03 = num_03 + 1
	elif inter >= 0.4 and inter < 0.5:
		num_04 = num_04 + 1
	elif inter >= 0.5 and inter < 0.6:
		num_05 = num_05 + 1
	elif inter >= 0.6 and inter < 0.7:
		num_06 = num_06 + 1
	elif inter >= 0.7 and inter < 0.8:
		num_07 = num_07 + 1
	elif inter >= 0.8 and inter < 0.9:
		num_08 = num_08 + 1
	elif inter >= 0.9 and inter < 1.0:
		num_09 = num_09 + 1

#
intervalos = [num_00, num_01, num_02, num_03, num_04, num_05, num_06, num_07, num_08, num_09]
print(intervalos)
"""
#
plt.bar(intervalos)
plt.show()
plt.savefig('intervalos.png')