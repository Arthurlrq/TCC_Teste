# PEGAR CADA GENE UNICO QUE APARECE NA LISTA DE PARES PELO MENOS UMA VEZ
# VERIFICAR A CHANCE DE INTERACAO DO PAR QUE ELE APARECE E SE FOR MAIOR OU IGUAL QUE 0.8 SALVA O GENE

#
arquivo_pares = open('mmukegg_new_new_unique_rand_labelx.txt')
pares = arquivo_pares.readlines()
arquivo_pares.close()

#
arquivo_results = open('results.txt')
results = arquivo_results.readlines()
arquivo_results.close()

#
arquivo_genes = open('hub_genes.txt')
genes = arquivo_genes.readlines()
arquivo_genes.close()

#
d_genes = {}

#
print("o total de pares eh:")
print(len(pares))

#
print("o total de results eh:")
print(len(results))

#
print("o total de genes eh:")
print(len(genes))

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
	#print(gene_name)
	# pegar o grau total do gene
	gene_grau = gene.split()[1]
	#print(gene_grau)
	#
	tam_list = int(gene_grau) + 3
	#print(tam_list)
	# criar uma lista de dicionarios para o gene
	d_genes[gene_name] = [dict() for number in range(tam_list)]
	#print(d_genes[gene_name])
	#d_genes[gene_name] = []
	#print("a lista contem tantos elementos: ")
	#print(len(d_genes[gene_name]))
	#print("\n")
	# salva o grau total do gene
	d_genes[gene_name][i]['Grau total'] = gene_grau
	#print(d_genes[gene_name][i]['Grau total'])
	i = i + 1
	# cria o grau de entrada do gene
	d_genes[gene_name][i]['Grau entrada'] = 0
	#print(d_genes[gene_name][i]['Grau entrada'])
	i = i + 1
	# cria o grau de saida do gene
	d_genes[gene_name][i]['Grau saida'] = 0
	#print(d_genes[gene_name][i]['Grau saida'])
	i = i + 1
	#
	j = 0
	# PRINTS
	#print("\n")
	#print(gene_name)
	#print("\n")
	#print(gene_grau)
	#print("\n")
	#for keys,values in d_genes.items():
	#   print(keys)
	#   print(values)
	#print("\n")
	# PRINTS
	# para cada par de genes
	for par in pares:
		if 'olfr' not in par:
			#
			gene_foi_salvo = False
			# pega o gene da esquerda
			gene_a = par.split()[0]
			# pega o gene da direita
			gene_b = par.split()[1]
			#if(gene_name in par):
			if gene_name == gene_a or gene_name == gene_b:

				# FAZER FOR PARA PERCORRER LISTA DE DICIONARIOS DO GENE ATUAL
				# SE O GENE DA INTERACAO JA ESTIVER PRESENTE ENTAO IGNORE O GENE DA INTERACAO


				# pega a chance de interacao do par
				chance_0 = 1 - float(results[j].split()[0])
				# se a chance de interacao eh maior ou igual a 0.8
				if float(chance_0) >= 0.8:
					# pega o gene da esquerda
					#gene_a = par.split()[0]
					# pega o gene da direita
					#gene_b = par.split()[1]
					# pega a chance do label 1
					chance_1 = results[j].split()[1]
					# pega a chance do label 2
					chance_2 = results[j].split()[2]
					# se a chance do label 1 eh maior
					if float(chance_1) > float(chance_2):
						label = 1
						chance = chance_1
					# se a chance do label 2 eh maior
					else:
						label = 2
						chance = chance_2
					#
					#print("\n")
					#print(i)
					#print("\n")
					# se o gene atual ta na esquerda
					if gene_name == gene_a:
						# SE O GENE_B JA EXISTIR NO DICIONARIO DO GENE_A ENTAO NAO FAZ NADA
						# VAI PRO PROXIMO PAR

						#
						#if value in word_freq.values():
						for dict in d_genes[gene_name]:
							if gene_b in dict.values():
								gene_foi_salvo = True
								break

						#if gene_foi_salvo == False:
						d_genes[gene_name][i]['Gene'] = gene_b
						#d_genes[gene_name][i]['Label'] = label
						#d_genes[gene_name][i]['Chance'] = chance
						i = i + 1
						# se o gene atual regula o outro
						if label == 1:
							g_saida = g_saida + 1
						# se o gene atual eh regulado pelo outro
						else:
							g_entrada = g_entrada + 1
					# se o gene atual ta na direita
					elif gene_name == gene_b:
						#print("\n")

						#
						#if value in word_freq.values():
						for dict in d_genes[gene_name]:
							if gene_a in dict.values():
								gene_foi_salvo = True
								break

						#
						#if gene_foi_salvo == False:
						d_genes[gene_name][i]['Gene'] = gene_a
						#d_genes[gene_name][i]['Label'] = label
						#d_genes[gene_name][i]['Chance'] = chance
						i = i + 1
						# se o gene atual eh regulado pelo outro
						if label == 1:
							g_entrada = g_entrada + 1
						# se o gene atual regula o outro
						else:
							g_saida = g_saida + 1
		# PARAR O i
		if i == tam_list:
			break;
		# avanca na lista de results
		j = j + 1
	#FIM DO FOR DOS PARES - JA OLHOU TODOS OS PARES
	# o grau de entrada eh por quantos genes o gene atual eh regulado
	d_genes[gene_name][1]['Grau entrada'] = g_entrada
	# o grau de saida eh quantos genes o gene atual regula
	d_genes[gene_name][2]['Grau saida'] = g_saida

#
#for keys,values in d_genes.items():
#   print(keys)
#   print(values)
#
#for gene in genes:
#	gene_name = gene.split()[0]
#	print(d_genes[gene_name][0]['Grau total'])
#	print("\n")
#	print(d_genes[gene_name][1]['Grau entrada'])
#	print("\n")
#	print(d_genes[gene_name][2]['Grau saida'])
#	print("\n")



for gene in genes:
	gene_name = gene.split()[0]
	for d in d_genes[gene_name]:




#
arquivo_info = open('info_hub_genes.txt', 'w')
arquivo_info.write("Informações quanto ao grau dos possíveis genes hub:\n\n")
#
for gene in genes:
	gene_name = gene.split()[0]
	arquivo_info.write("- ")
	arquivo_info.write(str(gene_name))
	arquivo_info.write(":\n")
	arquivo_info.write("Grau total:   ")
	arquivo_info.write(str(d_genes[gene_name][0]['Grau total']))
	arquivo_info.write("\nGrau entrada: ")
	arquivo_info.write(str(d_genes[gene_name][1]['Grau entrada']))
	arquivo_info.write("\nGrau saida:   ")
	arquivo_info.write(str(d_genes[gene_name][2]['Grau saida']))
	arquivo_info.write("\n\n")
#
arquivo_info.write("\n----------------------------------------------------------------------\n")
arquivo_info.write("Genes: \n\n")
#
for gene in genes:
	gene_name = gene.split()[0]
	arquivo_info.write("- ")
	arquivo_info.write(str(gene_name))
	arquivo_info.write(":\n")
	for d in d_genes[gene_name]:
		arquivo_info.write(str(d))
		arquivo_info.write("\n")
	arquivo_info.write("\n----------------------------------------------------------------------\n\n")

	
