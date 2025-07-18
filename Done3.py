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

#ES 2
import numpy as np
import matplotlib.pyplot as plt

# Equazioni II grado: x^2 + (4^(2k) - 2^(-2k))x - 4^(2k)*2^(-2k) = 0
# Soluzioni esatte: x1 = -4^(2k), x2 = 2^(-2k)

k_values = np.arange(4, 13)

def risolvi_equazione(k):
    """Formula risolutiva classica"""
    a = 1
    b = 4.0**(2*k) - 2.0**(-2*k)
    c = -4.0**(2*k) * 2.0**(-2*k)
    
    disc = b**2 - 4*a*c
    sqrt_disc = np.sqrt(disc)
    
    x1_calc = (-b + sqrt_disc) / (2*a)
    x2_calc = (-b - sqrt_disc) / (2*a)
    
    x1_exact = -4.0**(2*k)
    x2_exact = 2.0**(-2*k)
    
    return x1_calc, x2_calc, x1_exact, x2_exact

# Calcolo errori relativi
errori_x1, errori_x2 = [], []

print("k\tErr_x1\t\tErr_x2")
for k in k_values:
    x1_calc, x2_calc, x1_exact, x2_exact = risolvi_equazione(k)
    
    err_x1 = abs(x1_calc - x1_exact) / abs(x1_exact)
    err_x2 = abs(x2_calc - x2_exact) / abs(x2_exact)
    
    errori_x1.append(err_x1)
    errori_x2.append(err_x2)
    
    print(f"{k}\t{err_x1:.2e}\t{err_x2:.2e}")

# Grafico degli errori
plt.figure(figsize=(10, 6))
plt.semilogy(k_values, errori_x1, 'ro-', label='x1 = -4^(2k)', linewidth=2)
plt.semilogy(k_values, errori_x2, 'bo-', label='x2 = 2^(-2k)', linewidth=2)
plt.xlabel('k')
plt.ylabel('Errore relativo')
plt.title('Stabilita numerica delle formule classiche')
plt.grid(True)
plt.legend()
plt.show()

print("\nANALISI STABILITA:")
print("x1: INSTABILE - errore cresce esponenzialmente")
print("x2: STABILE - errore rimane piccolo")
print("\nMotivo: Cancellazione numerica in x1 = (-b + sqrt(b^2-4ac))/2a")
print("Quando b >> sqrt(4ac), si ha sqrt(b^2-4ac) circa uguale a b")
print("quindi x1 circa uguale a 0/2a (cancellazione!)")

# Formula stabile alternativa
def formula_stabile(k):
    """Evita cancellazione numerica"""
    a = 1
    b = 4.0**(2*k) - 2.0**(-2*k)
    c = -4.0**(2*k) * 2.0**(-2*k)
    
    disc = b**2 - 4*a*c
    sqrt_disc = np.sqrt(disc)
    
    # Usa x1*x2 = c/a per evitare cancellazione
    if b > 0:
        x1 = -2*c / (b + sqrt_disc)  # Formula stabile per x1
        x2 = (-b - sqrt_disc) / (2*a)
    else:
        x1 = (-b + sqrt_disc) / (2*a)
        x2 = -2*c / (b - sqrt_disc)
    
    return x1, x2

errori_x1_stabile = []
print("\nALGORITMO STABILE:")
print("k\tErr_classico\tErr_stabile")
for k in k_values:
    x1_stabile, x2_stabile = formula_stabile(k)
    _, _, x1_exact, x2_exact = risolvi_equazione(k)
    
    err_stabile = abs(x1_stabile - x1_exact) / abs(x1_exact)
    errori_x1_stabile.append(err_stabile)
    
    print(f"{k}\t{errori_x1[k-4]:.2e}\t\t{err_stabile:.2e}")

# Confronto stabilita
plt.figure(figsize=(8, 5))
plt.semilogy(k_values, errori_x1, 'r--', label='x1 classico (instabile)', linewidth=2)
plt.semilogy(k_values, errori_x1_stabile, 'g-', label='x1 stabile', linewidth=2)
plt.xlabel('k')
plt.ylabel('Errore relativo')
plt.title('Confronto stabilita: Formula classica vs. stabile')
plt.legend()
plt.grid(True)
plt.show()

print(f"\nRISULTATO: Formula stabile mantiene errore controllato")
print("CONDIZIONAMENTO DI f: R -> R")
print("="*40)
print()
print("Dato un problema f(x), con perturbazione delta_x:")
print("f(x + delta_x) - f(x) circa uguale a f'(x) * delta_x")
print()
print("CONDIZIONAMENTO ASSOLUTO:")
print("k_abs(f,x) = lim(delta_x->0) |delta_f|/|delta_x| = |f'(x)|")
print()
print("CONDIZIONAMENTO RELATIVO:")
print("k_rel(f,x) = lim(delta_x->0) (|delta_f|/|f(x)|)/(|delta_x|/|x|)")
print("           = |f'(x)| * |x| / |f(x)|")
print("           = |x * f'(x) / f(x)|")
print()

# Esempio pratico
def esempio_condizionamento():
    print("ESEMPIO: f(x) = x^2")
    print("f'(x) = 2x")
    print("k_abs = |f'(x)| = |2x| = 2|x|")
    print("k_rel = |x*f'(x)/f(x)| = |x*2x/x^2| = 2")
    print()
    print("Interpretazione:")
    print("- Il condizionamento assoluto cresce linearmente con |x|")
    print("- Il condizionamento relativo e costante = 2")

esempio_condizionamento()

#3,2,2,3,3 teoria