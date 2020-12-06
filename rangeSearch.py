
dist = lambda X,Y : sum((X-Y)**2)**0.5

def rangeSearch(Query,radio,data):
    result = []
    for obj in data["encodings"]:
        d = dist(Query,obj[1])
        if d <= radio:
            result.append( (d,obj[0]) )
    return result


