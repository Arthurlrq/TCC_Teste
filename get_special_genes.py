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
for par in pares:
	print(par)

#
for gene in genes:
	print(gene)

#
for chance in chances:
	print(chance)