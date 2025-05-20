import numpy as np

def eqnorm(A,b):
#Risolve un sistema sovradeterminato con il metodo delle equazioni normali
    G = A.T @ A # Matrice simmetrica (Gramiana)
    f = A.T @ b # Termine noto
    
    # Fattorizzazione di Cholesky: G = L L^T (valida perché G è simmetrica definita positiva)
    L = np.linalg.cholesky(G) 
    U = L.T
        
    # Risolviamo L z = f (sistema triangolare inferiore)
    z = np.linalg.solve(L, f)

    # Risolviamo U x = z (sistema triangolare superiore)
    x = np.linalg.solve(U, z)
    
    return x

A = np.array([[4, 1], [1, 3]])
b = np.array([1, 2])

x = eqnorm(A, b)
print("Soluzione approssimata:", x)
