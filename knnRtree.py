class  Node:
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
searchKNN(root, Q, r);        