import numpy as np

def gauss_seidel(A,b,x0,toll,it_max):
    errore = 1000
    d = np.diag(A)

    D = np.diag(d)
    E = np.tril(A, -1)
    F = np.tril(A, 1)

    M = D + E
    N = -F

    T = np.linalg.inv(M) @ N
    autovalori=np.linalg.eigvals(T)
    raggiospettrale = np.max(np.abs(autovalori))
    print("raggio spettrale Gauss-Seidel ",raggiospettrale)

    it=0
    er_vet=[]

    while errore > toll and it < it_max:
        temp = b - F @ x0
        x =  np.linalg.solve(M, temp)
        errore=np.linalg.norm(x-x0)/np.linalg.norm(x)
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

sol, iterazioni, errori = gauss_seidel(A, b, x0, toll, it_max)
print("Soluzione:", sol)
print("Iterazioni:", iterazioni)
