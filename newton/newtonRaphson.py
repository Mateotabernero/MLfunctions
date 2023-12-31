def newtonRaphson(f, fder, x0, maxIter = 1000, tol = 10**(-2)): 
    x = x0 
    n = 0
    lastError = tol +1 
    while(lastError > tol and n < maxIter):
        ### Hay que introducir mensajes de error si fder(x0) no está definido 
        x -= f(x)/fder(x0)

        lastError = abs(f(x))

        n += 1 

    return x

