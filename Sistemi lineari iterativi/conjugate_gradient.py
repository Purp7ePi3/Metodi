import numpy as np

def conjugate_gradient(A,b,x0,itmax,tol):
    n,m = A.shape
    if n!=m:
        print("Matrice non quadrata")
        return [],[]
    
   # inizializzare le variabili necessarie
    x = x0.copy()
    r = A @ x - b
    p = -r
    it = 0
    nb=np.linalg.norm(b)
    errore=np.linalg.norm(r)/nb

    vec_sol = [x.copy()]
    vet_r = [errore.copy()]
# utilizzare il metodo del gradiente coniugato per calcolare la soluzione
    while errore >= tol and it< itmax:
        it=it+1
        Ap= A @ p
        alpha = - (r @ p) / (p @ Ap)
        x = x + alpha * p
        vec_sol.append(x.copy())

        r_old = r
        r=r+alpha*Ap
        rtr_old = r_old @ r_old
        rtr_new = r @ r
        gamma = rtr_new / rtr_old

        errore=np.linalg.norm(r)/nb
        vet_r.append(errore)
        p =  -r + gamma * p
   
    
    return x, vet_r, vec_sol, it

A = np.array([[4, 1], [1, 3]])
b = np.array([1, 2])
x0 = np.zeros_like(b)

x, errors, solutions, it = conjugate_gradient(A, b, x0, itmax=100, tol=1e-10)

print("Soluzione:", x)
print("Iterazioni:", it)
