import numpy as np
import math
import matplotlib.pyplot as plt

def corde(fname,m,x0,tolx,tolf,nmax):
    """
    Implementa il metodo delle corde per il calcolo degli zeri di un'equazione non lineare.

    Parametri:
    fname: La funzione da cui si vuole calcolare lo zero.
    m: coefficiente angolare della retta che rimane fisso per tutte le iterazioni
    tolx: La tolleranza di errore tra due iterati successivi
    tolf: tolleranza sul valore della funzione
    nmax: numero massimo di iterazione

    Restituisce:
    Lo zero approssimato della funzione, il numero di iterazioni e la lista degli iterati intermedi.
    """
    xk = []
    fx0 = fname(x0)
    d = fx0 / m
    x1 = x0 - d
    fx1 = fname(x1)
    xk.append(x1)
    it=1
    
    while abs( x1 - x0 ) > tolx and abs(fx1) > tolf and it < nmax:
        x0 = x1
        fx0 = fx1
        d = fx0 - m
        x1 = x0 - d
        fx1 = fname(x1)
        it=it+1
        xk.append(x1)
        
    if it==nmax:
        print('raggiunto massimo numero di iterazioni \n')
        
    
    return x1,it,xk

f = lambda x: math.exp(x) - 2
m = 1.5
x0 = 0
tolx = 1e-6
tolf = 1e-6
nmax = 100
root, n_iter, steps = corde(f, m, x0, tolx, tolf, nmax)
print("Zero approssimato:", root)
print("Iterazioni:", n_iter)
# ===== GRAFICO FACOLTATIVO =========== #
plt.figure(figsize=(10, 5))
plt.plot(range(1, len(steps)+1), steps, marker='o', linestyle='-')
plt.axhline(y=root, color='red', linestyle='--', label=f'Radice ≈ {root:.7f}')
plt.title("Convergenza del metodo delle corde")
plt.xlabel("Iterazione")
plt.ylabel("Approssimazione $x_k$")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()