""" class  Node:
    children=[] #address
    mbrs = [] #mbsr of children 

def searchKNN(node, Q, k):
    if node.isLeaf():
        for C in node:
            d = ED(C, Q)    
            if len(listResult) < k:
                listResult.push( (d, C) )
            else:
                r = listResult.top()[0] #distance
                if d <= r:
                    listResult.push( (d, C) )
                    listResult.pop()
    else:        
        for i in range(len(node.children)):  
            r = listResult.top()[0] #distance          
            if MINDIST(Q, node.mbrs[i] ) <= r: #filter
                child = readNode(node.children[i])
                searchKNN(child, Q, r)

listResult = MaxHeap()
listResult.push( (INF, -1) )
searchKNN(root, Q, r);   """      

import pickle
from rtree import index

def knnRtree(Query,k,data):
    p = index.Property()
    p.dimension = 256
    p.buffering_capacity = 23
    p.dat_extension = 'data'
    p.idx_extension = 'index'
    idx = index.Index('rtree_index')
    id = 0
    result = []
    for i in data["encodings"]:
        lista = list(i)
        idx.insert(id,tuple(lista))
        id+=1
    for i in Query:
        query_list = list(i)
        query_tuple = tuple(query_list)
        result.append(idx.nearest(coordinates=query_tuple,num_results=k))
    return result