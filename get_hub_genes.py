#
arquivo_pares = open('mmukegg_new_new_unique_rand_labelx.txt')
pares = arquivo_pares.readlines()

#
arquivo_genes = open('unique_genes.txt')
genes_tudo = arquivo_genes.read()
genes = genes_tudo.splitlines()

#
arquivo_results = open('results.txt')
results = arquivo_results.readlines()
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
	d_genes[gene] = {}
	d_genes[gene]['Grau'] = 0
	i = 0
	for par in pares:
		# SE O OLFR N ESTVER NO PAR ENTAO CONSIDERAR O PAR
		if 'olfr' not in gene:
			if float(chances[i]) >= 0.8:
				if gene in par:
					d_genes[gene]['Grau'] = d_genes[gene]['Grau'] + 1
		#
		i = i + 1

#
d_genes_ordem = {}

#
for i in sorted(d, key = d_genes.get, reverse=True):
    print(i, d_genes[i])
    d_genes_ordem[i] = d_genes[i]
    print(i, d_genes_ordem[i])
    print("----------------------\n")

#
arquivo_hub = open('hub_genes.txt', 'w')
#
for gene in genes:
	#
	#if d_genes_ordem[gene]['Grau'] > 100:
	frase = gene + ' ' + str(d_genes_ordem[gene]['Grau']) + '\n'
	arquivo_hub.write(frase)



