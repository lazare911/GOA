def find_next_square(sq):
    x=int(sq**0.5)
    if x*x==sq:
        return (x+1)*(x+1)
    elif x*x!=sq:       
        return -1    
    
        
        