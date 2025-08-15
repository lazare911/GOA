def check_alive(health):
    if health<=0:  
        return False
    else:
        return True
print(check_alive(10))
print(check_alive(0))
print(check_alive(-10))
