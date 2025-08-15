def validate_hello(greetings):
    g = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for i in g:
        if i in greetings.lower():
            return True
    return False