from rtree import index
from maxHeap import MaxHeap

dist = lambda X,Y : sum((X-Y)**2)**0.5

def knnSequential(Query,k,data):
    heap_max = MaxHeap()
    for obj in data["encodings"]:
        d = dist(Query,obj[1])
        heap_max.push( (-d,obj[0]) ) #O( log(k) )
        if heap_max.size() > k:
            heap_max.pop() #O( log(k) ) //saca los objectos con distancia más grande
    return heap_max.get_k_elem(k)


def knnRtree(Query,k,data):
    p = index.Property()
    p.dimension = 256
    p.buffering_capacity = 23
    p.dat_extension = 'data'
    p.idx_extension = 'index'
    idx = index.Index('rtree',properties=p)
    #idx.interleaved = True
    id = 0
    result = []
    for i in data["encodings"]:
        coordinates = tuple(i)
        idx.insert(id,coordinates)
        id+=1
    for i in Query:
        result.append(idx.nearest(coordinates=i,num_results=k))
    return result