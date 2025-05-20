import numpy as np
import math
import matplotlib.pyplot as plt

def newton(fname,fpname,x0,tolx,tolf,nmax):
    """
    Implementa il metodo di Newton per il calcolo degli zeri di un'equazione non lineare.

    Parametri:
    fname: La funzione di cui si vuole calcolare lo zero.
    fpname: La derivata prima della funzione di  cui si vuole calcolare lo zero.
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
    if abs(dfx0) < 1e-15: 
        print("Derivata prima nulla in x0")
        return None, None,None
    
    d = fx0 / dfx0 
    x1 = x0 - d
    fx1=fname(x1)
    xk.append(x1)
    it=1
    
    while abs(x1 - x0) > tolx and abs(fx1) > tolf and it < nmax:
        x0= x1
        fx0= fx1
        dfx0 = fpname(x0)
        if abs(dfx0) < 1e-15:
            print("Derivata prima nulla in x0")
            return None, None,None
        
        d = fx0 / dfx0
        
        x1= x0 - d
        fx1=fname(x1)
        it=it+1
        
        xk.append(x1)
        
    if it==nmax:
        print('raggiunto massimo numero di iterazioni \n')
        
    
    return x1,it,xk

f = lambda x: x**3 - x - 2
fp = lambda x: 3*x**2 - 1  # derivata di f

x0 = 1
tolx = 1e-6
tolf = 1e-6
nmax = 100

root, n_iter, steps = newton(f, fp, x0, tolx, tolf, nmax)
print(f"Radice approssimata: {root}, in {n_iter} iterazioni.")
# ===== GRAFICO FACOLTATIVO =========== #
plt.figure(figsize=(10, 5))
plt.plot(range(1, len(steps)+1), steps, marker='o', linestyle='-')
plt.axhline(y=root, color='red', linestyle='--', label=f'Radice ≈ {root:.7f}')
plt.title("Convergenza del metodo di newton")
plt.xlabel("Iterazione")
plt.ylabel("Approssimazione $x_k$")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()