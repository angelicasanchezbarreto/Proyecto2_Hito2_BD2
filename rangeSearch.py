
dist = lambda X,Y : sum((X-Y)**2)**0.5

def rangeSearch(Query,radio,data):
    result = []
    for obj in data:
        d = dist(Query,data[obj])
        if d <= radio:
            result.append( (d,obj) )
    return result


