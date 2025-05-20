import numpy as np

def jacobi(A,b,x0,toll,it_max):
    errore = 1000
    d = np.diag(A)
    n = A.shape[0]
    invM = np.diag(1/d)
    E = np.tril(A, -1)
    F = np.tril(A, 1)
    N = E + F
    T = -invM @ N
    autovalori = np.linalg.eigvals(T)
    raggiospettrale = max(abs(autovalori))
    print("raggio spettrale jacobi", raggiospettrale)

    it=0
    er_vet=[]

    while errore > toll and it < it_max:
        x = invM @ (b - N @ x0)
        errore = np.linalg.norm(x-x0)/np.linalg.norm(x)
        er_vet.append(errore)
        x0=x.copy()
        it=it+1
    return x,it,er_vet


A = np.array([[4, 1, 2],
              [1, 3, -1],
              [2, -1, 5]], dtype=float)

b = np.array([4, 5, 1], dtype=float)
x0 = np.zeros_like(b)
toll = 1e-6
it_max = 100

sol, iterazioni, errori = jacobi(A, b, x0, toll, it_max)
print("Soluzione:", sol)
print("Iterazioni:", iterazioni)
