from matplotlib import pyplot as plt
import numpy as np

def my_newton_minimo(gradiente, Hess, x0, tolx, tolf, nmax):
    """
    DA UTILIZZARE NEL CASO IN CUI CALCOLATE DRIVATE PARZIALI PER GRADIENTE ED HESSIANO SENZA UTILIZZO DI SYMPY
    
    Funzione di newton-raphson per calcolare il minimo di una funzione in più variabili

    Parametri
    ----------
    fun : 
        Nome della funzione che calcola il gradiente della funzione non lineare.
    Hess :  
        Nome della funzione che calcola la matrice Hessiana della funzione non lineare.
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
        Vettore contenente la norma del passo ad ogni iterazione.
    """
    matHess = Hess(x0)

    if np.linalg.matrix_rank(matHess) < len(x0):
        print("La matrice Hessiana calcolata nell'iterato precedente non è a rango massimo")
        return None, None, None
    
    grad_fx0= gradiente(x0)    
    s = -np.linalg.solve(matHess, grad_fx0)

    # Aggiornamento della soluzione
    x1 = x0 + s
    grad_fx1 = gradiente(x1)
    Xm = [np.linalg.norm(s, 1)]
    it = 1

    while np.linalg.norm(s,1) > tolx and np.linalg.norm(grad_fx1, 1) > tolf and it < nmax:
        x0 = x1
        it += 1
        matHess = Hess(x0) 
        grad_fx0=grad_fx1
        
        if np.linalg.matrix_rank(matHess) < len(x0):    
            print("La matrice Hessiana calcolata nell'iterato precedente non è a rango massimo")
            return None, None, None
        
    
        s = -np.linalg.solve(matHess, grad_fx0)
        
        # Aggiornamento della soluzione
        x1 = x0 + s

        #Calcolo del gradiente nel nuovo iterato
        grad_fx1  = gradiente(x1)
        print(np.linalg.norm(s, 1))
        Xm.append(np.linalg.norm(s, 1))

        if it == nmax:
            print("Massime itazioni raggiunte")
    return x1, it, Xm


# Funzione gradiente
def gradiente(x):
    return np.array([2*(x[0] - 1), 2*(x[1] - 2)])

# Funzione Hessiana
def Hess(x):
    return np.array([[2, 0],
                     [0, 2]])

# Punto iniziale
x0 = np.array([0.0, 0.0])

# Tolleranze e max iterazioni
tolx = 1e-6
tolf = 1e-6
nmax = 100

# Funzione gradiente
def gradiente(x):
    return np.array([2*(x[0] - 1), 2*(x[1] - 2)])

# Funzione Hessiana
def Hess(x):
    return np.array([[2, 0],
                     [0, 2]])

# Punto iniziale
x0 = np.array([0.0, 0.0])

# Tolleranze e max iterazioni
tolx = 1e-6
tolf = 1e-6
nmax = 100
# Esecuzione del test
sol, iterations, steps = my_newton_minimo(gradiente, Hess, x0, tolx, tolf, nmax)

print("Soluzione trovata:", sol)
print("Numero di iterazioni:", iterations)
print("Norma passo per iterazione:", steps)

plt.figure(figsize=(10, 5))
plt.plot(range(1, len(steps)+1), steps, marker='o', linestyle='-')
plt.axhline(y=tolx, color='red', linestyle='--', label=f'Tolleranza tolx = {tolx}')
plt.title("Convergenza del metodo di Newton")
plt.xlabel("Iterazione")
plt.ylabel("Norma del passo")
plt.yscale('log')  # scala logaritmica per vedere meglio la decrescita
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()