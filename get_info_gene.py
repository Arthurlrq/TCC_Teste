#
import json

#
arquivo_pares = open('mmukegg_new_new_unique_rand_labelx.txt')
pares = arquivo_pares.readlines()

#
arquivo_bulk = open('bulk_gene_list.txt')
genes_bulk = arquivo_bulk.readlines()

#
arquivo_sc = open('sc_gene_list.txt')
genes_sc = arquivo_sc.readlines()

#
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

#
num_genes = len(d_genes.keys())

#
arquivo_info = open('info_gene.txt', 'w')
arquivo_info.write("Número total de genes na lista de pares: ")
arquivo_info.write(str(num_genes))
arquivo_info.write('\n----------------------------------------------------------------------\n')
arquivo_info.write("Genes: ")
arquivo_info.write('\n')
#
for key, value in d_genes.items():
	arquivo_info.write('%s:%s\n' % (key, value))
	arquivo_info.write('----------------------------------------------------------------------\n')


#
arquivo_genes = open('unique_genes.txt', 'w')
#
for key in d_genes.items():
	arquivo_genes.write('%s\n' % (key))