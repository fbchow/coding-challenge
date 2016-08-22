# Chow,Fanny
# coding-challenge
# python3


# import libraries 
import os, json, codecs, re, datetime
import networkx as nx
import numpy as np
from dateutil.parser import *

# source files
path = "/Users/fanny/Github/coding-challenge/venmo_input"
filename = "venmo-trans.txt"
fpath = os.path.join(path, filename)

# initialize empty graph & empty array
data = []
g = nx.Graph()

# read-in file
with open(fpath, encoding='utf-8') as file:
	for i in file:
		data = (json.loads(i))
		actor = data['actor']
		target = data['target']
		created_time = (data['created_time'])

		g.add_node(actor) 
		g.add_node(target)
		g.add_edge(actor, target, time = created_time)

		# some functionality for the created-time difference

# creates an empty dict because there's nothin to obtain associated with 'Ying-Mo's key
zz = g.node['Ying-Mo']
yy = g.edge['Ying-Mo']['Maryann-Berry']
# print(type(yy))
# print(type(zz))
# print("who is ying-mo connected to: %s" % yy)
# print("who is ying-mo connected to: %s" % zz)

# print a list of all edges read-in	
# iterate through the edges
# i = 0
# for n1, n2, attr in g.edges(data=True):÷

# 	# if (attr == 0):
# 	# 	print ("yeah")
# 	# else:
# 	# 	print (attr)
# 	# 	print (attr - 1)
# 	i = i + 1
# 	print(attr['time'])

pp = g.get_edge_data('Ying-Mo', 'Maryann-Berry')
print (pp)

# new_list = []
# for i in old_list:

ff = [e for e in g.edges_iter()]
print ("list comprehension is %s" % ff)

	# t1 = "2016-04-07T03:34:58Z"
	# t2 = "2016-04-07T03:31:18Z"
	# tt1 = parse(t1)
	# tt2 = parse(t2)
	# diff = tt1 - tt2

	# if (diff > datetime.timedelta(minutes=1)):
 #    	print ("transaction outside the 60 sec window")
	# else:
 #    	print ("transaction within the 60 sec window")

	# print (n1, n2, attr)



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


def median_degree(G): 
	degree_sequence = G.degree().values()
	med_degree = np.median(list(degree_sequence))
	print ("Mean degree is %.3f." % med_degree)
	return med_degree

