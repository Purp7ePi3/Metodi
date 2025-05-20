
def newton_mod(fname,fpname,m,x0,tolx,tolf,nmax):
    """
    Implementa il metodo di Newton modificato da utilizzato per il calcolo degli zeri di un'equazione non lineare
    nel caso di zeri multipli.

    Parametri:
    fname: La funzione di cui si vuole calcolare lo zero.
    fpname: La derivata prima della funzione di cui si vuole calcolare lo zero.
    m: molteplicità della radice
    x0: iterato iniziale
    tolx: La tolleranza di errore tra due iterati successivi
    tolf: tolleranza sul valore della funzione
    nmax: numero massimo di iterazione

    Restituisce:
    Lo zero approssimato della funzione, il numero di iterazioni e la lista degli iterati intermedi.
    """ 

    xk = []
    fx0 = fname(x0)
    dfx0 = fpname(x0)

    if  abs(dfx0) < 1e-14:
        print("Derivata prima nulla in x0")
        return None, None,None

    d = m * fx0 / dfx0
    x1 = x0 - d
    fx1 =  fname(x1)
    xk.append(x1)
    it = 1

    while abs(d) > tolx and abs(fx1) > tolf and it < nmax:
        x0 = fx1
        fx0 = fname(fx1)
        dfx0 = fpname(fx1)
        
        #Se la derivata prima e' pià piccola della precisione di macchina stop
        if abs(dfx0) < 1e-14: 
            print(" derivata prima nulla in x0")
            return None, None,None
        
        d = m * fx0 / dfx0
        x1 = x0 - d 
        fx1=fname(x1)
        it=it+1
        xk.append(x1)
        
    if it==nmax:
        print('raggiunto massimo numero di iterazioni \n')
        
    
    return x1,it,xk


# Esempio con una funzione con radice multipla
def f(x):
    return (x - 2)**3  # radice x=2, molteplicità 3

def df(x):
    return 3*(x - 2)**2

root, iterations, iterates = newton_mod(f, df, m=3, x0=3.0, tolx=1e-10, tolf=1e-10, nmax=100)
print("Radice approssimata:", root)
print("Iterazioni:", iterations)
print("Iterati:", iterates)
