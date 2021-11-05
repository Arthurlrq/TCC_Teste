# Descobrir quantos genes diferentes tem na lista de pares
# - SERÁ O NUMERO DE CHAVES DO DICIONARIO

# Descobrir quantos genes da lista de pares interagem entre si
# - QUANTOS PARES DA LISTA DE PARES POSSUEM LABEL 0

# Descobrir quantos genes a rede acertou que interagem entre si?

# Descobrir com quantos genes cada gene interage

# Criar um dicionário de dicionários
# Chave é o nome do gene

import json

arquivo_pares = open('mmukegg_new_new_unique_rand_labelx.txt')
pares = arquivo_pares.readlines()

arquivo_bulk = open('bulk_gene_list.txt')
genes_bulk = arquivo_bulk.readlines()

arquivo_sc = open('sc_gene_list.txt')
genes_sc = arquivo_sc.readlines()

d_genes = {}

# BULK
print("BULK")
for gene in genes_bulk:
	gene_name = gene.split()[0]
	d_genes[gene_name] = {}
	d_genes[gene_name]['aparicoes'] = 0
	d_genes[gene_name]['bulk_set'] = 'sim'
	# PEGA CADA GENE BULK E OLHA SE APARECE NA LISTA DE PARES
	for par in pares:
		if(gene_name in par):
			d_genes[gene_name]['aparicoes'] = d_genes[gene_name]['aparicoes'] + 1
	# REMOVER GENE QUE NÃO APARECE
	if(d_genes[gene_name]['aparicoes'] == 0):
		del d_genes[gene_name]

print(len(d_genes.keys()))

# SC
print("SC")
for gene in genes_sc:
	gene_name = gene.split()[0]
	#
	if(gene_name in d_genes):
		d_genes[gene_name]['sc_set'] = 'sim'
	else:
		d_genes[gene_name] = {}
		d_genes[gene_name]['aparicoes'] = 0
		d_genes[gene_name]['sc_set'] = 'sim'
		# PEGA CADA GENE SC E OLHA SE APARECE NA LISTA DE PARES
		for par in pares:
			if(gene_name in par):
				d_genes[gene_name]['aparicoes'] = d_genes[gene_name]['aparicoes'] + 1
		# REMOVER GENE QUE NÃO APARECE
		if(d_genes[gene_name]['aparicoes'] == 0):
			del d_genes[gene_name]

print(len(d_genes.keys()))

num_genes = len(d_genes.keys())

arquivo_stats = open('statistics.txt', 'w')
arquivo_stats.write("Número total de genes na lista de pares: ")
arquivo_stats.write(str(num_genes))
arquivo_stats.write('\n')
arquivo_stats.write("Genes: ")
arquivo_stats.write('\n')

for key, value in d_genes.items():
	arquivo_stats.write('%s:%s\n' % (key, value))








#arquivo_stats.write(json.dumps(d_genes))

"""
dict1 = {'a':1,'b':2,'c':3}
print(len(dict1.keys()))
"""

"""
>>> d = {}
>>> d['dict1'] = {}
>>> d['dict1']['innerkey'] = 'value'
>>> d['dict1']['innerkey2'] = 'value2'
>>> d
{'gm28588': {'conjunto': 'bulk', 'aparicoes': '32'}}
"""

