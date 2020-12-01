class  Node:
    children=[] #address
    mbrs = [] #mbsr of children 

def searchRange(node, Q, r):
    if node.isLeaf():
        for C in node:
            d = ED(C, Q)    
            if d <= r:  #refine
                listResult.add( (d, C) )
    else:
        for i in range(len(node.children)):            
            if MINDIST(Q, node.mbrs[i] ) <= r: #filter
                child = readNode(node.children[i])
                searchRange(child, Q, r)
##
listResult = []
searchRange(root, Q, r, listResult);        