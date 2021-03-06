from rtree import index
from maxHeap import MaxHeap
import os.path as path
from os import remove

dist = lambda X,Y : sum((X-Y)**2)**0.5

def knnSequential(Query,k,data):
    heap_max = MaxHeap()
    for obj in data:
        d = dist(Query,data[obj])
        heap_max.push( (-d,obj) )
        if heap_max.size() > k:
            heap_max.pop()
    return heap_max.get_k_elem(k)

def knnRtree(Query,k,data):
    if path.exists('rtree.dat'):
        remove('rtree.dat')
    if path.exists('rtree.idx'):
        remove('rtree.idx')
    p = index.Property()
    p.dimension = 256
    idx = index.Index('rtree',properties=p)
    result = []
    id=0
    names = {}
    for obj in data:
        coordinates = data[obj]
        idx.insert(id,tuple(coordinates*2))
        names[id] = obj
        id+=1
    
    nearest = list(idx.nearest(coordinates=tuple(list(Query)*2),num_results=k))
    for i in nearest:
        result.append((i,names[i]))
    return result