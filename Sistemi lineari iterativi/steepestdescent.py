from matplotlib import pyplot as plt
import numpy as np

def steepestdescent(A,b,x0,itmax,tol):
    n,m=A.shape
    if n!=m:
        print("Matrice non quadrata")
        return [],[]
    
    x = x0
    r = A @ x - b
    p = -r
    it = 0
    nb = np.linalg.norm(b)
    errore = np.linalg.norm(r)/nb
    
    vec_sol = [x.copy()]    
    vet_r=[errore]
    
    # utilizzare il metodo del gradiente per trovare la soluzione
    while  errore > tol and it < itmax :
        it=it+1
        Ap= A @ p
        alpha = - (r @ p) / (p @ Ap)
                
        x =  x + alpha * p
        vec_sol.append(x.copy())
        
        r = r + alpha * Ap
        errore = np.linalg.norm(r) / nb
        vet_r.append(errore)
        p = -r
        
     
    return x,vet_r,vec_sol,it


A = np.array([[4, 1], [1, 3]])
b = np.array([1, 2])
x0 = np.zeros_like(b)

x, errors, solutions, it = steepestdescent(A, b, x0, itmax=100, tol=1e-10)
print("Soluzione:", x)
print("Iterazioni:", it)

plt.plot(range(len(errors)), errors, marker='o')
#plt.axhline(y=1e-10, color='red', linestyle='--', label=f'Tolleranza: {1e-10}')
plt.xlabel("Iterazione")
#plt.yscale("log")
plt.ylabel("Errore relativo (norma L2)")
plt.title("Convergenza del metodo del gradiente")
plt.grid(True)
plt.show()