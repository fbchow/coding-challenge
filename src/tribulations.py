# Chow,Fanny
# coding-challenge
# python3


# import libraries 
import os
import json
import codecs
import re
import networkx as nx
import numpy as np
import datetime

#source files
path = "/Users/fanny/Github/coding-challenge/venmo_input"
filename = "venmo-trans.txt"
fpath = os.path.join(path, filename)

# initialize empty graph & empty array
data = []
g = nx.Graph()

with open(fpath, encoding='utf-8') as file:
	for i in file:
		data = (json.loads(i))
		actor = data['actor']
		target = data['target']
		created_time = (data['created_time'])

		# print (data)
		# print (type(data))

		# print (target)
		# print (actor)
		# print (type(target))

		# g.add_node(actor, target)
		g.add_node(actor) 
		g.add_node(target)
		g.add_edge(actor, target, time = created_time)


		# some functionality for it the created-time difference
		# if (created-time[] - created-time[]) > 60:



# iterate through the nodes
# for node in g.nodes():

# print a list of all edges read-in	
# iterate through the edges
for n1, n2, attr in g.edges(data=True):
	print (n1, n2, attr)

# # sample func
# # calculate the avg degree of each node's neighbors
# def avg_neigh_degree(g):
# 	dat = {}
# 	for n in g.nodes():
# 		if g.degree(n):
# 			dat[n] = float(sum(g.degree(i) for i in g[n]))/ g.degree(n)
# 	return dat

# print(avg_neigh_degree(g))
# print(type(avg_neigh_degree(g)))

# simple func
# calculate the median degree of each node's neighbors



def median_degree(G): 
	degree_sequence = G.degree().values()
	med_degree = np.median(list(degree_sequence))
	print ("Mean degree is %.3f." % med_degree)
	return med_degree

# def avg_neigh_degree(g):
# 	dat = {}
# 	for n in g.nodes():
# 		if g.degree(n):
# 			dat[n] = float(median_degree(n))
# 	return dat


# q = avg_neigh_degree(g)
# print(q)
# print(type(avg_neigh_degree(g)))



# x = load_json(path)
# print (x)
# #print(x['created_time'])
# print(type(x))

# garbage iteration 7/11/16
	# x = file.read()
	# print (x)
	# print(type(file.read()))
	# for i in x:
	# 	y = json.loads(x)
	# 	print (y)