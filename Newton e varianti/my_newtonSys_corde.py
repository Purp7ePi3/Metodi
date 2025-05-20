import numpy as np
import matplotlib.pyplot as plt
def my_newtonSys_corde(fun, jac, x0, tolx, tolf, nmax):

    """
    Funzione per la risoluzione del sistema f(x)=0
    mediante il metodo di Newton, con variante delle corde, in cui lo Jacobiano non viene calcolato
    ad ogni iterazione, ma rimane fisso, calcolato nell'iterato iniziale x0.
    
    Parametri
    ----------
    fun : funzione vettoriale contenente ciascuna equazione non lineare del sistema.
    jac : funzione che calcola la matrice Jacobiana della funzione vettoriale.
    x0 : array
        Vettore contenente l'approssimazione iniziale della soluzione.
    tolx : float
        Parametro di tolleranza per l'errore tra due soluzioni successive.
    tolf : float
        Parametro di tolleranza sul valore della funzione.
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

    x0 = np.array(x0, dtype = float)
    fx0 = fun(x0)
    matjac = jac(x0)   

    if np.linalg.matrix_rank(matjac) < len(x0):
        print("La matrice dello Jacobiano calcolata nell'iterato precedente non è a rango massimo")
        return None, None,None
    
    try: 
        s = np.linalg.solve(matjac, -fx0)
    except np.linalg.LinAlgError:
        return None, None, None
    
    # Aggiornamento della soluzione
    x1 = x0 + s
    fx1 = fun(x1)
    Xm = [np.linalg.norm(s, 1)/np.linalg.norm(x1,1)]
    it = 1    

    while np.linalg.norm(s, 1) > tolx and np.linalg.norm(fx1, 1) > tolf and it < nmax:
        x0 = x1 
        fx0 = fx1
        
        try: 
            s = np.linalg.solve(matjac, -fx1)
        except np.linalg.LinAlgError:
            return None, None, None
     
        # Aggiornamento della soluzione
        x1 =  x0 + s
        fx1 = fun(x1)
        Xm.append(np.linalg.norm(s, 1)/np.linalg.norm(x1,1))
        if it == nmax:
            print("Raggiunto il numero massimo di iterazioni.")

    return x1, it, Xm

# Sistema: x^2 + y^2 - 1 = 0 ; x - y = 0
def f(v):
    x, y = v
    return np.array([x**2 + y**2 - 1, x - y])

def J(v):
    x, y = v
    return np.array([[2*x, 2*y], [1, -1]])

x0 = [0.5, 0.5]
sol, it, Xm = my_newtonSys_corde(f, J, x0, tolx=1e-10, tolf=1e-10, nmax=100)
print("Soluzione:", sol)
print("Iterazioni:", it)
print("Errori relativi:", Xm)

plt.figure(figsize=(10, 5))
plt.plot(range(1, len(Xm) + 1), Xm, marker="o", linestyle="-", label="Errore relativo")
plt.title(f"Convergenza dell'errore relativo\nSoluzione approssimata: {np.round(sol, 5)}")
plt.xlabel("Iterazione")
plt.ylabel("Errore relativo (norma L1)")
plt.grid(True)
plt.legend()
plt.show()
