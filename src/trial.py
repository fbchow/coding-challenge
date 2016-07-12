# with open(fpath, encoding='utf-8') as file:
# 	for i in file:
# 		data = (json.loads(i))

# 		actor = data['actor']
# 		target = data['target']
# 		time = (data['created_time'])


import os
import json
import codecs
import re

import networkx as nx
import datetime


path = "/Users/fanny/Github/coding-challenge/venmo_input"
filename = "venmo-trans.txt"
fpath = os.path.join(path, filename)

g = nx.read_edgelist(fpath)