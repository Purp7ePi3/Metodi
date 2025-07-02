from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

dati = loadmat('testI')
A = dati["A"].astype(float)
b = dati["b"].astype(float).flatten()

def check(A):
    is_sym = np.allclose(A, A.T)
    is_pos = is_sym and np.all(np.linalg.eigvals(A) > 0)
    return is_sym, is_pos

print(check(A))


def jacobi(A, b, x0, tol=1e-10, max_it=2000):
    d = np.diag(A)  
    n = A.shape[0]
    invM = np.diag(1/d)
    L = np.tril(A, -1)       
    U = np.triu(A, 1)      
    N = L + U
    T = -invM @ N
    autovalori = np.linalg.eigvals(T)
    raggio = max(abs(autovalori))
    print("Raggio spettrale jacobi:", raggio)
    
    er_vet = []
    for i in range(max_it):
        x = invM @ (b - N @ x0)
        error = np.linalg.norm(x - x0) / np.linalg.norm(x)
        er_vet.append(error)
        
        if error < tol:
            return x, i+1, er_vet
        x0 = x.copy()
    
    return x, max_it, er_vet


def gauss_seidel(A, b, x0, tol=1e-10, max_it=2000):
    n = A.shape[0]
    D = np.diag(np.diag(A))
    E = np.tril(A, -1)
    F = np.triu(A, 1)

    M = D + E
    N = -F

    T = np.linalg.inv(M) @ N
    autovalori=np.linalg.eigvals(T)
    raggiospettrale = np.max(np.abs(autovalori))
    print("raggio spettrale Gauss-Seidel ",raggiospettrale)
    er_vet = []
    
    for i in range(max_it):
        temp = b - F @ x0
        x = np.linalg.solve(M, temp)
        error = np.linalg.norm(x - x0) / np.linalg.norm(x)
        er_vet.append(error)
        if error < tol:
            return x, i+1, er_vet
        x0 = x.copy()

    return x, max_it, er_vet


n = A.shape[0]
x0_curr = np.zeros(n)
sol, iterazioni, errori = jacobi(A, b, x0_curr)
sol1, iterazioni1, errori1 = gauss_seidel(A, b, x0_curr)

plt.figure(figsize=(12,6))
plt.semilogy(errori, label='Jacobi', markersize=3)
plt.semilogy(errori1, label='Gauss-Seidel', markersize=3)
plt.xlabel('Iterazioni')
plt.ylabel('Errore relativo')
plt.title('Confronto convergenza: Jacobi vs Gauss-Seidel')
plt.legend()
plt.grid(True)
plt.show()