from operator import itemgetter

#
arquivo_pares = open('mmukegg_new_new_unique_rand_labelx.txt')
pares = arquivo_pares.readlines()
arquivo_pares.close()

#
arquivo_genes = open('unique_genes.txt')
genes_tudo = arquivo_genes.read()
genes = genes_tudo.splitlines()
arquivo_genes.close()

#
arquivo_results = open('results.txt')
results = arquivo_results.readlines()
arquivo_results.close()
#
chances = []
#
for result in results:
	chance = result.split()[0]
	chance = 1 - float(chance)
	chances.append(chance)

#
d_genes = {}

#
print('o numero de pares eh: ')
print(len(pares))

#
print('o numero de chances eh: ')
print(len(chances))

#
for gene in genes:
	#d_genes[gene] = {}
	#d_genes[gene]['Grau'] = 0
	d_genes[gene] = 0
	i = 0
	for par in pares:
		# SE O OLFR N ESTVER NO PAR ENTAO CONSIDERAR O PAR
		if 'olfr' not in par:
			if float(chances[i]) >= 0.8:
				# pega o gene da esquerda
				gene_a = par.split()[0]
				# pega o gene da direita
				gene_b = par.split()[1]
				#if(gene_name in par):
				if gene == gene_a or gene == gene_b:
					d_genes[gene] = d_genes[gene] + 1
		#
		i = i + 1
	#
	if d_genes[gene] < 10:
		del d_genes[gene]

#
d_genes_ordem = {}

#
d_genes_ordem = {k: v for k, v in sorted(d_genes.items(), key=lambda item: item[1], reverse=True)}

#
print(d_genes_ordem)

#
arquivo_hub = open('hub_genes.txt', 'w')

#
for nome, grau in d_genes_ordem.items():
	frase = nome + ' ' + str(grau) + '\n'
	arquivo_hub.write(frase)

