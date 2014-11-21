# -*- coding: utf-8 -*-
import networkx as nx
import os

class GPS(object):
	grafo 	= None
	origem 	= None
	destino = None

	def ler_mapa(self, arquivo_mapa):
		self.grafo = nx.convert.convert_to_undirected(nx.read_gml(arquivo_mapa))

	def setar_origem(self, origem):
		self.origem = int(origem)

	def setar_destino(self, destino):
		self.destino = int(destino)

	def processar(self):
		rotas = nx.all_simple_paths(self.grafo, self.origem, self.destino, cutoff=None)
		print '================================ GPS ================================'
		print u'\nCalculando rota de [%s]%s até [%s]%s:' % (str(self.origem), nx.get_node_attributes(self.grafo,'label')[self.origem], str(self.destino), nx.get_node_attributes(self.grafo,'label')[self.destino])
		conta_rota = 1
		for rota in rotas:
			print '\nRota número %s:' % (str(conta_rota))
			conta_rota += 1
			caminho = ''
			cidade_anterior = False
			for cidade in rota:
				if caminho:
					caminho += ' -- '
					if cidade_anterior:
						try:
							caminho += nx.get_edge_attributes(self.grafo,'label')[cidade_anterior, cidade]
						except:
							caminho += nx.get_edge_attributes(self.grafo,'label')[cidade, cidade_anterior]
					caminho += ' --> '
				caminho += nx.get_node_attributes(self.grafo,'label')[cidade]
				cidade_anterior = cidade
			print caminho