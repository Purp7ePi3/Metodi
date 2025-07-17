#ES 1
from scipy.io import loadmat
import numpy as np
from scipy.linalg import cholesky, solve_triangular

# Caricamento dati
dati = loadmat('testII')
A = dati["A"].astype(float)
b = dati["b"].astype(float)
A1 = dati["A1"].astype(float)
b1 = dati["b1"].astype(float)

print("SISTEMA 1: A x = b")
print("="*30)

# Verifica proprieta matrice A
is_sym = np.allclose(A, A.T)
eigenvals = np.linalg.eigvals(A)
is_pos_def = np.all(eigenvals > 0)

print(f"A e simmetrica: {is_sym}")
print(f"A e definita positiva: {is_pos_def}")
print("METODO: Cholesky (A e simmetrica definita positiva)")

# Risoluzione con Cholesky
L = cholesky(A, lower=True)
y = solve_triangular(L, b, lower=True)
x = solve_triangular(L.T, y, lower=False)

print(f"Soluzione x: {x.flatten()}")
print(f"Residuo: {np.linalg.norm(A @ x - b):.2e}")

print("\nSISTEMA 2: A1 x1 = b1")
print("="*30)

print(f"A1 e {A1.shape} (rettangolare)")
print("METODO: Minimi quadrati (sistema sovradeterminato)")

# Risoluzione con minimi quadrati
x1, residuals, rank, s = np.linalg.lstsq(A1, b1, rcond=None)

print(f"Soluzione x1: {x1.flatten()}")
residuo_A1 = np.linalg.norm(A1 @ x1 - b1)
print(f"Residuo: {residuo_A1:.2e}")

print("\nPERTURBAZIONE (0.1% su b1[0])")
print("="*30)

# Perturbazione del termine noto
b1_pert = b1.copy()
b1_pert[0, 0] += 0.001 * b1[0, 0]  # 0.1%

# Risoluzione sistema perturbato
x1_pert, _, _, _ = np.linalg.lstsq(A1, b1_pert, rcond=None)

# Calcolo errori relativi
err_dati = np.linalg.norm(b1_pert - b1) / np.linalg.norm(b1)
err_sol = np.linalg.norm(x1_pert - x1) / np.linalg.norm(x1)

print(f"Errore relativo sui dati: {err_dati:.2e}")
print(f"Errore relativo sulla soluzione: {err_sol:.2e}")

# Numero di condizione
cond_num = np.linalg.cond(A1.T @ A1)
print(f"Numero di condizione k(A1^T A1): {cond_num:.2e}")
print(f"Fattore di amplificazione: {err_sol/err_dati:.1f}")

import numpy as np

# Definizione del sistema A3 x3 = b3
A3 = np.array([[8.0, 0, 1, 1],
               [0, 0.8, 1, 0],
               [1, 1, 2, 0],
               [1, 0, 0.0, 2.0]])

b3 = np.array([10.0, 1.8, 4.0, 3.0])

print("VERIFICA CONVERGENZA GAUSS-SEIDEL")
print("="*40)

def verifica_convergenza_GS(A):
    """
    Verifica convergenza Gauss-Seidel usando criteri teorici
    """
    n = A.shape[0]
    
    # Criterio 1: Dominanza diagonale stretta
    print("CRITERIO 1: Dominanza diagonale stretta")
    dom_diag = True
    for i in range(n):
        somma_non_diag = sum(abs(A[i, j]) for j in range(n) if j != i)
        if abs(A[i, i]) <= somma_non_diag:
            dom_diag = False
    
    if dom_diag:
        print("CONVERGENZA GARANTITA: Matrice diagonalmente dominante")
        return True
    else:
        print("Non diagonalmente dominante")
    
    # Criterio 2: Simmetrica definita positiva
    print("\nCRITERIO 2: Simmetrica definita positiva")
    is_sym = np.allclose(A, A.T)
    print(f"Simmetrica: {is_sym}")
    
    if is_sym:
        eigenvals = np.linalg.eigvals(A)
        is_pos_def = np.all(eigenvals > 0)
        print(f"Definita positiva: {is_pos_def}")
        print(f"Autovalori: {eigenvals}")
        
        if is_pos_def:
            print("CONVERGENZA GARANTITA: Matrice simmetrica definita positiva")
            return True
    
    return False

converge = verifica_convergenza_GS(A3)

print(f"\nIMPLEMENTAZIONE GAUSS-SEIDEL")
print("="*40)

def gauss_seidel(A, b, x0=None, max_iter=100, tol=1e-10):
    n = len(b)
    if x0 is None:
        x = np.zeros(n)
    else:
        x = x0.copy()
    
    print(f"Iterazione 0: x = {x}")
    
    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            somma = 0
            for j in range(n):
                if j != i:
                    somma += A[i, j] * x[j]
            x[i] = (b[i] - somma) / A[i, i]
        
        # Calcolo errore
        errore = np.linalg.norm(x - x_old, ord=np.inf)
        
        if (k + 1) <= 5 or (k + 1) % 10 == 0:
            print(f"Iterazione {k+1}: x = {x}, errore = {errore:.2e}")
        
        # Test di convergenza
        if errore < tol:
            print(f"\nConvergenza raggiunta in {k+1} iterazioni")
            print(f"Errore finale: {errore:.2e}")
            break
    
    return x, k+1

# Risoluzione con Gauss-Seidel
print("Risoluzione del sistema con Gauss-Seidel:")
x_gs, iter_gs = gauss_seidel(A3, b3)

print(f"\nSOLUZIONE FINALE:")
print(f"x3 = {x_gs}")

# Verifica della soluzione
residuo = A3 @ x_gs - b3
print(f"Residuo ||A3*x3 - b3||: {np.linalg.norm(residuo):.2e}")

# Confronto con soluzione esatta
x_exact = np.linalg.solve(A3, b3)
errore_sol = np.linalg.norm(x_gs - x_exact)
print(f"Errore rispetto soluzione esatta: {errore_sol:.2e}")
print(f"Soluzione esatta: {x_exact}")