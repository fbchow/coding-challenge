


# from pprint import pprint

# file = "/venmo_input/venmo-trans.txt"
# x = json.load(file)
# print x

	
# file1 = open('filepath', 'r')
# data = file1.readlines()

# for line in data :
#    values = json.loads(line)

# '''Now you can access all the objects using values.get('key') '''

import os
import json
import codecs
import re

import datetime

import networkx as nx
# import numpy

# ASK GRACE HOW DO I FIX THIS LATER TO GET IT TO BE USABLE ON ANOTHER PERSON'S MACHINE?
# BECAUSE I HAD TO SPECFIFY MY OWN LOCAL PATH TO READ THE FILE THAT WAS IN A DIFFERENT FOLDER`
path = "/Users/fanny/Github/coding-challenge/venmo_input"
filename = "venmo-trans.txt"
fpath = os.path.join(path, filename)

# data = []


# with codecs.open(fpath,'rU','utf-8') as f:
# with open(fpath, "r") as f:
#     # for line in f:
#     #    data.append(json.loads(line)[0])

#     file_content = f.read()

#     data = json.load(f)

#     print (data)

# json1_file = open('json1')
# json1_str = json1_file.read()
# json1_data = json.loads(json1_str)[0]


    # dat = data['target']
    # print(dat)
    
# json1_file = open('json1')
#      json1_str = json1_file.read()
#      json1_data = json.loads.(json1_str)




#      json1_data = json.loads(json1_str)[0]

# Now you can access the data stored in datapoints just as you were expecting:

# datapoints = json1_data['datapoints']




#     # x = data['created_time']
#     x = type(data)
#     y = data[1]
#     print (x)
#     print (y)


# with open(fpath, encoding='utf-8') as data_file:
#     data = json.load(data_file.read())
#     print (data)



## CLASSIC WAY OF READING WITHOUT JSON LIBRARY -- JUST READS AS ONE BIG ASS STRING NOT A DICTIONARY...
# with open(fpath, encoding='utf-8') as f:
	# file_content = f.read()
	# print(file_content[10])
	# f.replace("\r\n", "\\n")
	# # data = [json.loads(str(f)) for item in f.strip().split('\n')]
	# data = json.load(f)
	# print (data)
	
#CODE WORKS HERE	
with open(fpath, encoding='utf-8') as file:
	for i in file:
		data = (json.loads(i))

		actor = data['actor']
		target = data['target']
		time = (data['created_time'])

		# print ("what is")
		# print (type(data))
		# print (type(i))
		# print (i)
		print (actor)
		# print (target)
		# print (time)


# #constructing the graph
G = nx.Graph()		#initialize the graph
# G.add_node("spam")	#add a node
G.add_nodes_from([actor])
# G.add_edge(1,2)		#add an edge
# G.add_node("m")	#add a node
# G.add_edge(1,1)
# 		#add an edge
print(list(G.nodes())) #print the nodes & edges

# PRINT ANALYTICS
print("here's some shit")
avg = avg()

# STACK OVERFLOW 
# def read_json_file(fpath):
#     with open(fpath) as f:
#         js_graph = json.load(f)
#     return json_graph.node_link_graph(js_graph)

# shits = read_json_file(fpath)
# print (shits)





	# print (file_content)







# json_data = open("file root")
# data = json.load(json_data)


	# json1_data = json.loads(file_content)
	# print(json1_data)


	# file_content = json.load(f)
# print (file_content)
# 	file_content = json.load(json_data)
# 	parsed_json = json.loads(file_content)
# 	x = print(parsed_json["created_time"])
# 	print (x)


# json1_file = open('json1')
# json1_str = json1_file.read()
# json1_data = json.loads(json1_str)[0]
	# datapoints = numpy.array(json1_data['datapoints'])
# avg = datapoints[0:5,0].mean()


# x = json.load(file_content)
# print (x)


# f = open(filename, 'r')
# f.read()


#calculates the median degree of a venmo transaction graph


#sources
# http://stackoverflow.com/questions/19483351/converting-json-string-to-dictionary-not-list-python