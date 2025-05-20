import numpy as np
import math
import matplotlib.pyplot as plt

def sign(n):
   if n > 0: return 1
   elif n < 0: return -1
   else: return 0
   
def falsi(fname, a, b, maxit, tolx,tolf):
    fa=fname(a)
    fb=fname(b)
    
    if fa * fb >= 0 :
        print("Non è possibile applicare il metodo di falsa posizione \n")
        return None, None,None

    it = 0
    v_xk = []
    # fallback = a
    fxk = 10 
    
    for it in range(maxit): #while it < maxit:
        xk = a - fa * (b-a) / (fb-fa) # (a * fb - b * fa) / (fb - fa) 
        v_xk.append(xk)
        #it += 1
        fxk=fname(xk)
        if fxk==0: # or (abs(b-a) < tolx and abs(fxk) < tolf)
            return xk, it, v_xk

        # Aggiorna gli estremi dell'intervallo
        if sign(fa)*sign(fxk)>0:   
            a = xk
            fa = fxk
        elif sign(fxk)*sign(fb)>0:    
            b = xk
            fb = fxk
    # fallback = xk
    print('Raggiunto massimo numero di iterazioni\n')

    return xk, it, v_xk


f = lambda x: x**3 - x - 2
root, n_iter, steps = falsi(f, 1, 2, 100, 1e-7, 1e-10)
print(f"Radice approssimata: {root}, in {n_iter} iterazioni.")
# ===== GRAFICO FACOLTATIVO =========== #
plt.figure(figsize=(10, 5))
plt.plot(range(1, len(steps)+1), steps, marker='o', linestyle='-')
plt.axhline(y=root, color='red', linestyle='--', label=f'Radice ≈ {root:.7f}')
plt.title("Convergenza del metodo dei falsi")
plt.xlabel("Iterazione")
plt.ylabel("Approssimazione xₖ")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()