import numpy as np
import sympy as sp

def newton_raphson(gradiente, Hess, x0, tolx, tolf, nmax):

    """
    Funzione di newton-raphson per calcolare il minimo di una funzione in più variabili, modificato nel caso in cui si utilizzando sympy 
    per calcolare Gradiente ed Hessiano. Rispetto alla precedente versione cambia esclusivamente il modo di valutare il vettore gradiente e la matrice Hessiana in un punto 
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

        
    matHess = np.array([[Hess[0, 0](x0[0], x0[1]), Hess[0, 1](x0[0], x0[1])],
                        [Hess[1, 0](x0[0], x0[1]), Hess[1, 1](x0[0], x0[1])]])
    

    gradiente_x0=np.array([gradiente[0](x0[0], x0[1]),gradiente[1](x0[0], x0[1])])
    
    if np.linalg.det(matHess) == 0:
        print("La matrice Hessiana calcolata nell'iterato precedente non è a rango massimo")
        return None, None, None
        
    s = -np.linalg.inv(matHess).dot(gradiente_x0)
    
    # Aggiornamento della soluzione
    it = 1
    x1 = x0 + s
    grad_fx1 = np.array([gradiente[0](x1[0],x1[1]),gradiente[1](x1[0],x1[1])])
    Xm = [np.linalg.norm(s, 1)]
    
    while np.linalg.norm(s, 1) > tolx and np.linalg.norm(grad_fx1, 1) > tolf and it < nmax:
        x0 = x1
        it += 1
        matHess = np.array([[Hess[0, 0](x0[0], x0[1]), Hess[0, 1](x0[0], x0[1])],
                            [Hess[1, 0](x0[0], x0[1]), Hess[1, 1](x0[0], x0[1])]])
        
        grad_fx0=grad_fx1
        
        if np.linalg.det(matHess) == 0:
            print("La matrice Hessiana calcolata nell'iterato precedente non è a rango massimo")
            return None, None, None
        
        s = -np.linalg.inv(matHess).dot(grad_fx0)
        
        # Aggiornamento della soluzione
        x1 = x0 + s
        #Aggiorno il gradiente per la prossima iterazione 
        grad_fx1=np.array([gradiente[0](x1[0],x1[1]),gradiente[1](x1[0],x1[1])])
        print(np.linalg.norm(s, 1))
        Xm.append(np.linalg.norm(s, 1))

    return x1, it, Xm


# Variabili simboliche
x, y = sp.symbols('x y')

# Funzione
f = (x - 1)**2 + (y - 2)**2

# Gradiente simbolico
grad_f = [sp.lambdify((x, y), df, 'numpy') for df in [sp.diff(f, x), sp.diff(f, y)]]

# Hessiano simbolico (matrice 2x2)
Hessian_f = sp.Matrix([[sp.diff(f, var1, var2) for var2 in (x, y)] for var1 in (x, y)])
Hess_f = np.array([[sp.lambdify((x, y), Hessian_f[i,j], 'numpy') for j in range(2)] for i in range(2)])

# Punto iniziale
x0 = np.array([0.0, 0.0])

# Tolleranze e max iterazioni
tolx = 1e-6
tolf = 1e-6
nmax = 100


sol, iterations, step_norms = newton_raphson(grad_f, Hess_f, x0, tolx, tolf, nmax)

print("Soluzione trovata:", sol)
print("Numero di iterazioni:", iterations)
print("Norma passi:", step_norms)