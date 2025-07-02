from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

# Load data
dati = loadmat('testII')
A = dati['A'].astype('float')
A1 = dati['A1'].astype('float')
b = dati['b'].astype('float')
b1 = dati['b1'].astype('float')

# Conjugate Gradient
def cg(A, b, x0, tol=1e-6, max_it=2000):
    x = x0.flatten()
    b = b.flatten()
    r = A @ x - b
    p = -r
    nb = np.linalg.norm(b)
    err = [np.linalg.norm(r) / nb]
    
    for it in range(max_it):
        if err[-1] < tol:
            break
        Ap = A @ p
        alpha = -(r @ p) / (p @ Ap)
        x += alpha * p
        r_old = r.copy()
        r += alpha * Ap
        beta = (r @ r) / (r_old @ r_old)
        p = -r + beta * p
        err.append(np.linalg.norm(r) / nb)
    
    return x.reshape(-1,1), err, it+1

# Steepest Descent
def sd(A, b, x0, tol=1e-6, max_it=2000):
    x = x0.flatten()
    b = b.flatten()
    r = A @ x - b
    nb = np.linalg.norm(b)
    err = [np.linalg.norm(r) / nb]
    
    for it in range(max_it):
        if err[-1] < tol:
            break
        p = -r
        Ap = A @ p
        alpha = -(r @ p) / (p @ Ap)
        x += alpha * p
        r += alpha * Ap
        err.append(np.linalg.norm(r) / nb)
    
    return x.reshape(-1,1), err, it+1

# Check matrix properties
def check(A):
    sym = np.allclose(A, A.T)
    pos = sym and np.all(np.linalg.eigvals(A) > 0)
    return sym, pos

# Solve both systems
for A_curr, b_curr, name in [(A, b, "A"), (A1, b1, "A1")]:
    sym, pos = check(A_curr)
    print(f"Matrix {name}: symmetric={sym}, positive={pos}")
    
    if sym and pos:
        x0 = np.zeros((A_curr.shape[0], 1))
        sol_cg, err_cg, it_cg = cg(A_curr, b_curr, x0)
        sol_sd, err_sd, it_sd = sd(A_curr, b_curr, x0)
        
        print(f"CG: {it_cg} iterations")
        print(f"SD: {it_sd} iterations")
        print(f"Speedup: {it_sd/it_cg:.1f}x")

        # Plot
        plt.figure(figsize=(10,6))
        plt.semilogy(err_cg, label='CG')
        plt.semilogy(err_sd, label='SD')
        plt.xlabel('Iterations')
        plt.ylabel('Error')
        plt.legend()
        plt.grid()
        plt.title(f'Matrix {name}')
        plt.show()