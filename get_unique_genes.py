# CRIA A LISTA DE GENES UNICOS QUE APARECEM PELO MENOS UMA VEZ NA LISTA DE PARES

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
	print("agora eh o gene: " + gene_name)
	#
	if 'olfr' not in gene_name:
		#
		d_genes[gene_name] = {}
		d_genes[gene_name]['aparicoes'] = 0
		#d_genes[gene_name]['bulk_set'] = 'sim'
		# PEGA CADA GENE BULK E OLHA SE APARECE NA LISTA DE PARES
		for par in pares:
			if(gene_name in par):
				print("o gene " + gene_name + " está no par " + par)
				d_genes[gene_name]['aparicoes'] = d_genes[gene_name]['aparicoes'] + 1
		# REMOVER GENE QUE NÃO APARECE
		if(d_genes[gene_name]['aparicoes'] == 0):
			del d_genes[gene_name]

print(len(d_genes.keys()))

# SC
print("SC")
for gene in genes_sc:
	gene_name = gene.split()[0]
	print("agora eh o gene: " + gene_name)
	#
	if 'olfr' not in gene_name:
		#
		if(gene_name in d_genes):
			#d_genes[gene_name]['sc_set'] = 'sim'
			print('gene ja ta na lista, entao nao faz nada')
		else:
			d_genes[gene_name] = {}
			d_genes[gene_name]['aparicoes'] = 0
			#d_genes[gene_name]['sc_set'] = 'sim'
			# PEGA CADA GENE SC E OLHA SE APARECE NA LISTA DE PARES
			for par in pares:
				#
				if(gene_name in par):
					print("o gene " + gene_name + " está no par " + par)
					d_genes[gene_name]['aparicoes'] = d_genes[gene_name]['aparicoes'] + 1
			# REMOVER GENE QUE NÃO APARECE
			if(d_genes[gene_name]['aparicoes'] == 0):
				del d_genes[gene_name]

print(len(d_genes.keys()))

#
arquivo_genes = open('unique_genes.txt', 'w')
#
for key in d_genes:
	arquivo_genes.write(str(key) + '\n')