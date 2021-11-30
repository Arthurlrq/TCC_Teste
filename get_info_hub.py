#
arquivo_pares = open('mmukegg_new_new_unique_rand_labelx.txt')
pares = arquivo_pares.readlines()
arquivo_pares.close()

#
arquivo_chances = open('results.txt')
chances = arquivo_chances.readlines()
arquivo_chances.close()

#
arquivo_genes = open('hub_genes.txt')
genes = arquivo_genes.readlines()
arquivo_genes.close()

#
d_genes = {}

# GENE : [{GRAU TOTAL: X, GRAU DE ENTRADA: X, GRAU DE SAIDA: X}, {GENE: 1, CHANCE: 0.131312}, {GENE: 2, CHANCE: 0.131312}]

#number_of_dictionaries = 3
#list_of_dictionaries = [dict() for number in range(number_of_dictionaries)]

# para cada 1 dos 9 genes
for gene in genes:
	i = 0
	#
	g_saida = 0
	#
	g_entrada = 0
	# pegar o nome do gene
	gene_name = gene.split()[0]
	# pegar o grau total do gene
	gene_grau = gene.split()[1]
	# criar uma lista de dicionarios para o gene
	d_genes[gene_name] = [dict() for number in range(int(gene_grau))]
	#d_genes[gene_name] = []
	# salva o grau total do gene
	d_genes[gene_name][i]['Grau total'] = gene_grau
	i = i + 1
	# cria o grau de entrada do gene
	d_genes[gene_name][i]['Grau entrada'] = 0
	i = i + 1
	# cria o grau de saida do gene
	d_genes[gene_name][i]['Grau saida'] = 0
	i = i + 1
	#
	j = 0
	# PRINTS
	print("\n")
	print(gene_name)
	print("\n")
	print(gene_grau)
	print("\n")
	for keys,values in d_genes.items():
	   print(keys)
	   print(values)
	print("\n")
	# PRINTS
	# para cada par de genes
	for par in pares:
		if gene_name in par:
			# pega a chance de interacao do par
			chance_0 = 1 - float(chances[j].split()[0])
			# se a chance de interacao eh maior ou igual a 0.8
			if float(chance_0) >= 0.8:
				# pega o gene da esquerda
				gene_a = par.split()[0]
				# pega o gene da direita
				gene_b = par.split()[1]
				# pega a chance do label 1
				chance_1 = chances[j].split()[1]
				# pega a chance do label 2
				chance_2 = chances[j].split()[2]
				# se a chance do label 1 eh maior
				if float(chance_1) > float(chance_2):
					label = 1
					chance = chance_1
				# se a chance do label 2 eh maior
				else:
					label = 2
					chance = chance_2
				# se o gene atual ta na esquerda
				if gene == gene_a:
					d_genes[gene_name][i]['Gene'] = gene_b
					# se o gene atual regula o outro
					if label == 1:
						g_saida = g_saida + 1
					# se o gene atual eh regulado pelo outro
					else:
						g_entrada = g_entrada + 1
				# se o gene atual ta na direita
				else:
					d_genes[gene_name][i]['Gene'] = gene_a
					# se o gene atual eh regulado pelo outro
					if label == 1:
						g_entrada = g_entrada + 1
					# se o gene atual regula o outro
					else:
						g_saida = g_saida + 1
				#	salva o label predito para o par
				d_genes[gene_name][i]['Label'] = label
				# salva a chance da predicao
				d_genes[gene_name][i]['Chance'] = chance
				# avanca na lista de dicionarios do gene
				i = i + 1
		# avanca na lista de chances
		j = j + 1
	#FIM DO FOR DOS PARES - JA OLHOU TODOS OS PARES
	# o grau de entrada eh por quantos genes o gene atual eh regulado
	d_genes[gene_name][i]['Grau entrada'] = g_entrada
	# o grau de saida eh quantos genes o gene atual regula
	d_genes[gene_name][i]['Grau saida'] = g_saida

#
for keys,values in d_genes.items():
   print(keys)
   print(values)