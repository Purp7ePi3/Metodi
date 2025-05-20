import numpy as np
import math
import matplotlib.pyplot as plt

def secanti(fname,xm1,x0,tolx,tolf,nmax):
    """
    Implementa il metodo delle secanti per il calcolo degli zeri di un'equazione non lineare.

    Parametri:
    fname: La funzione di cui si vuole calcolare lo zero.
    xm1, x0: primi due iterati
    tolx: La tolleranza di errore tra due iterati successivi
    tolf: tolleranza sul valore della funzione
    nmax: numero massimo di iterazione

    Restituisce:
    Lo zero approssimato della funzione, il numero di iterazioni e la lista degli iterati intermedi.
    """
    xk=[]
    fxm1= fname(xm1)
    fx0= fname(x0)
    if fx0 == fxm1:
        return None, None, None
    d = (x0 - xm1) / (fx0 - fxm1) * fx0
    x1= x0 - d
    xk.append(x1)
    fx1=fname(x1)
    it=1

    while it<nmax and abs(fx1)>=tolf and abs(d)>=tolx*abs(x1):
        xm1=x0
        x0=x1
        fxm1=fx0
        fx0=fx1 
        if fx0 == fxm1:
            print("Divisione per zero evitata: f(x0) = f(xm1).")
            break
        d = (x0 - xm1) / (fx0 - fxm1) * fx0
        x1 = x0 - d
        fx1=fname(x1)
        xk.append(x1)
        it=it+1
        
    
    if it==nmax:
        print('Secanti: raggiunto massimo numero di iterazioni \n')
    
    return x1,it,xk

def f(x):
    return math.cos(x) - x

xm1 = 0.5      
x0 = 1.0        
tolx = 1e-10    
tolf = 1e-10    
nmax = 100      

zero, iterazioni, iterati = secanti(f, xm1, x0, tolx, tolf, nmax)

print(f"Zero approssimato: {zero}")
print(f"Numero di iterazioni: {iterazioni}")

# --- GRAFICO --- #
x_vals = np.linspace(0, 1, 400)
y_vals = [f(x) for x in x_vals]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="f(x) = cos(x) - x", color="blue")
plt.axhline(0, color='gray', linestyle='--')
# Evidenzia gli iterati
y_iter = [f(x) for x in iterati]
plt.plot(iterati, y_iter, 'ro', label="Iterati (secanti)")
plt.plot(zero, f(zero), 'go', label="Zero approssimato")
plt.title("Metodo delle Secanti: f(x) = cos(x) - x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()