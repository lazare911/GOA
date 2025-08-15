def number(bus_stops):
    l=[]
    for i in bus_stops:
        l.append(i[0]-i[1])
    return sum(l)