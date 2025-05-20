import numpy as np
import matplotlib.pyplot as plt

def my_newtonSys(fun, jac, x0, tolx, tolf, nmax):
    """
    Funzione per la risoluzione del sistema F(x)=0
    mediante il metodo di Newton.

    Parametri
    ----------
    fun : funzione vettoriale contenente ciascuna equazione non lineare del sistema.
    jac : funzione che calcola la matrice Jacobiana della funzione vettoriale.
    x0 : array
        Vettore contenente l'approssimazione iniziale della soluzione.
    tolx : float
        Parametro di tolleranza per l'errore assoluto.
    tolf : float
        Parametro di tolleranza per l'errore relativo.
    nmax : int
        Numero massimo di iterazioni.

    Restituisce
    -------
    x : array
        Vettore soluzione del sistema (o equazione) non lineare.
    it : int
        Numero di iterazioni fatte per ottenere l'approssimazione desiderata.
    Xm : array
        Vettore contenente la norma dell'errore relativo tra due iterati successivi.
    """
    x0 = np.array(x0, dtype=float)
    fx0 = fun(x0)
    matjac = jac(x0)

    if np.linalg.matrix_rank(matjac) < len(x0) :
        print("La matrice dello Jacobiano calcolata nell'iterato precedente non è a rango massimo")
        return None, None,None

    s = np.linalg.solve(matjac, -fx0)
    it = 1
    x1 = x0 + s
    fx1 = fun(x1)

    Xm = [np.linalg.norm(s, 1)/np.linalg.norm(x1,1)]

    while np.linalg.norm(s,1)/np.linalg.norm(x1,1) > tolx and np.linalg.norm(fx1, 2) > tolf and it < nmax:
        x0 = x1
        it += 1
        matjac = jac(x0)
        if np.linalg.matrix_rank(matjac) < len(x0):
                print("La matrice dello Jacobiano calcolata nell'iterato precedente non è a rango massimo")
                return None, None,None

        fx0 = fun(x0)
        s = np.linalg.solve(matjac, -fx0)
        x1 = x0 + s
        fx1 = fun(x1)
        Xm.append(np.linalg.norm(s, 1)/np.linalg.norm(x1,1))

    return x1, it, Xm



def fun(x):
    return np.array([
        x[0]**2 + x[1]**2 - 4,
        x[0] * np.exp(x[1]) - 1
    ])

# Jacobiana del sistema
def jac(x):
    return np.array([
        [2 * x[0], 2 * x[1]],
        [np.exp(x[1]), x[0] * np.exp(x[1])]
    ])

# Importa e usa la funzione my_newtonSys che ti ho dato prima
# Parametri iniziali
x0 = [1.0, 0.0]
tolx = 1e-8
tolf = 1e-8
nmax = 100

# Chiamata alla funzione di Newton
x_sol, it, Xm = my_newtonSys(fun, jac, x0, tolx, tolf, nmax)

# Stampa dei risultati
print(f"Soluzione approssimata: {x_sol}")
print(f"Numero di iterazioni: {it}")

# Grafico della convergenza
plt.figure(figsize=(8, 5))
plt.plot(Xm, marker='o')
plt.yscale('log')
plt.xlabel('Iterazione')
plt.ylabel('Errore relativo (log scala)')
plt.title('Convergenza del metodo di Newton per sistemi')
plt.grid(True)
plt.show()