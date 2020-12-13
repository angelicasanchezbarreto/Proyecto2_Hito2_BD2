from rtree import index
from maxHeap import MaxHeap

dist = lambda X,Y : sum((X-Y)**2)**0.5

def knnSequential(Query,k,data):
    heap_max = MaxHeap()
    for obj in data:
        d = dist(Query,obj[1])
        heap_max.push( (-d,obj[0]) )
        if heap_max.size() > k:
            heap_max.pop()
    return heap_max.get_k_elem(k)


def knnRtree(Query,k,data):
    p = index.Property()
    idx = index.Index()
    result = []
    #print(list(data[0][1]))
    for i in range(len(data)-1):
        idx.insert(i,list(data[i][1])*2)
    
    """ for i in data["encodings"]:
        idx.insert(id,i[1]*2)
        id+=1 """
        
    #for i in Query:
    
    #print(idx.nearest(coordinates=list(Query)*2,num_results=k))
    
    result = list(idx.nearest(coordinates=list(Query)*2,num_results=k))
    return result