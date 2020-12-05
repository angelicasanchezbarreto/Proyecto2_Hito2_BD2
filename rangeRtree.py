class  Node:
    children=[] #address
    mbrs = [] #mbsr of children 

def searchRange(node, Q, r):
    listResult = []
    if node.isLeaf():
        for C in node:
            d = ED(C, Q)    
            if d <= r:  #refine
                listResult.append( (d, C) )
    else:
        for i in range(len(node.children)):            
            if MINDIST(Q, node.mbrs[i] ) <= r: #filter
                child = readNode(node.children[i])
                searchRange(child, Q, r)
##

searchRange(root, Q, r)




