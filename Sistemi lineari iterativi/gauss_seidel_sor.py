import numpy as np

def gauss_seidel_sor(A,b,x0,toll,it_max,omega):
    errore=1000
    d = np.diag(A)

    D = np.diag(d)
    Dinv = np.diag(1/d)
    E = np.tril(A, -1)
    F = np.tril(A, 1)

    Momega=D+omega*E
    Nomega=(1-omega)*D-omega*F
    T = np.linalg.inv(Momega) @ Nomega
    autovalori=np.linalg.eigvals(T)
    raggiospettrale=np.max(np.abs(autovalori))
    print("raggio spettrale Gauss-Seidel SOR ", raggiospettrale)
    
    it=0
    xold=x0.copy()
    xnew=x0.copy()
    er_vet=[]

    while errore > toll and it < it_max:
        
        temp = b - A @ xold
        xtilde = xold + omega * Dinv @ temp
        xnew = xtilde.copy()
        errore=np.linalg.norm(xnew-xold)/np.linalg.norm(xnew)
        er_vet.append(errore)
        xold=xnew.copy()
        it=it+1

    return xnew,it,er_vet


A = np.array([[4, 1, 2],
              [1, 3, -1],
              [2, -1, 5]], dtype=float)

b = np.array([4, 5, 1], dtype=float)
x0 = np.zeros_like(b)
toll = 1e-6
it_max = 100

sol, iterazioni, errori = gauss_seidel_sor(A, b, x0, toll, it_max,1.2)
print("Soluzione:", sol)
print("Iterazioni:", iterazioni)
