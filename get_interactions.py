#

arquivo_interacoes = open('results.txt')
interacoes = arquivo_interacoes.readlines()

inter_list = []

for interacao in interacoes:
	inter = gene.split()[0]
	print(inter)
	inter_list.append(inter)
	print(inter_list)
