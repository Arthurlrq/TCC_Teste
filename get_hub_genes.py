#criar um dicionário de dicionários. Cada chave do primeiro dicionário é o nome de um gene
#para cada gene (genes.txt):
#- criar uma chave "grau" iniciando em 0
#- procurar em quais pares ele aparece (mmukegg_new_new_unique_rand_labelx.txt)
#- se a chance de interação dos 2 genes for >= 0.8 então salvar o gene e a chance (chances.txt)
#- alterar o valor da chave grau com base em com quantos genes interage

#
arquivo_pares = open('mmukegg_new_new_unique_rand_labelx.txt')
pares = arquivo_pares.readlines()

#
arquivo_genes = open('unique_genes.txt')
#genes = arquivo_genes.readlines()
genes_tudo = arquivo_genes.read()
genes = genes_tudo.splitlines()

#
#arquivo_chances = open('chances.txt')
#chances_tudo = arquivo_chances.read()
#chances = chances_tudo.splitlines()

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
		if float(chances[i]) >= 0.8:
			if gene in par:
				d_genes[gene]['Grau'] = d_genes[gene]['Grau'] + 1
		#
		i = i + 1
	#
	print(i)

#
arquivo_hub = open('hub_genes.txt', 'w')
#
for gene in genes:
	#
	if d_genes[gene]['Grau'] > 100:
		frase = gene + ' ' + str(d_genes[gene]['Grau'])
		arquivo_hub.write(frase)

# TALVEZ PRECISE COLOCAR O \N NO FIM DA FRASE

