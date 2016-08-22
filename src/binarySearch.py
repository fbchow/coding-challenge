
# import libraries 
import os, json, codecs, re, datetime
import networkx as nx
import numpy as np
from dateutil.parser import *


import networkx as nx
import itertools as IT
import matplotlib.pyplot as plt
import collections


# class BinaryTree(object):
#    def __init__(self, data):
#       self.data = data
#       self.right = None
#       self.left = None
#       self.name = None
#    def edgelist(self, counter = IT.count().next):
#        self.name = counter() if self.name is None else self.name
#        for node in (self.left, self.right):       
#            if node:
#                node.name = counter() if node.name is None else node.name
#                yield (self.name, node.name)
#        for node in (self.left, self.right):
#            if node:
#                for n in node.edgelist(counter):
#                    yield n

# tree = [BinaryTree(i) for i in range(5)]        
# tree[0].left = tree[1]
# tree[0].right = tree[2]
# tree[2].left = tree[3]
# tree[2].right = tree[4]

# edgelist = list(tree[0].edgelist())
# print(edgelist)   

# G = nx.Graph(edgelist)
# nx.draw_spectral(G)
# plt.show()


 # source files
path = "/Users/fanny/Github/coding-challenge/venmo_input"
filename = "venmo-trans.txt"
fpath = os.path.join(path, filename)

# initialize empty graph & empty array
data = []
g = nx.Graph()

def edges_breadth(tree):
    history = collections.deque([tree])
    while history:
        parent = history.popleft()
        for c in (parent.left, parent.right):
            if c:
                yield((parent.data, c.data))
                history.append(c)



# read-in file
with open(fpath, encoding='utf-8') as file:
  for i in file:
    schedenfraude = edges_breadth(i)    
    print (schedenfraude)







