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
arquivo_gene = open('unique_genes.txt')
genes = arquivo_gene.readlines()

#
arquivo_chances = open('chances.txt')
chances = arquivo_chances.readlines()

#
d_genes = {}

#
for gene in genes:
	d_genes[gene] = {}
	d_genes[gene]['Grau'] = 0
	i = 0
	for par in pares:
		#
		if chances[i] >= 0.8:
			A = par.split()[0]
			B = par.split()[1]
			# SE O GENE TA NA ESQUERDA
			if gene == A:
				d_genes[gene][B] = chances[i]
			# SE O GENE TA NA DIREITA
			elif gene == B:
				d_genes[gene][A] = chances[i]
		#
		i = i + 1

# DESCOMENTAR ISSO EEEEM - ISSO CALCULA OS GRAUS DOS GENES
#
#for gene in genes:
#	grau = len(d_genes[gene].keys())
#	d_genes[gene]['Grau'] = grau

#
d_items = d_genes.items()
#
for item in d_items:
    print(item)