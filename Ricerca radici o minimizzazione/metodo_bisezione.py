import numpy as np
import math
import matplotlib.pyplot as plt

def sign(n):
   if n > 0: return 1
   elif n < 0: return -1
   else: return 0

def metodo_bisezione(fname, a, b, tolx, tolf):
   """
    Implementa il metodo di bisezione per il calcolo degli zeri di un'equazione non lineare.

    Parametri:
    f: La funzione da cui si vuole calcolare lo zero.
    a: L'estremo sinistro dell'intervallo di ricerca.
    b: L'estremo destro dell'intervallo di ricerca.
    tol: La tolleranza di errore.

    Restituisce:
    Lo zero approssimato della funzione, il numero di iterazioni e la lista di valori intermedi.
    """
   fa=fname(a)
   fb=fname(b)
   if  fb*fa >= 0:
      print("Non è possibile applicare il metodo di bisezione \n")
      return None, None,None

   it = 0
   v_xk = []

   maxit = math.ceil(math.log((b - a) / tolx) / math.log(2))-1

   
   while it < maxit: 
    xk =  (a+b) / 2
    v_xk.append(xk)
    it += 1
    fxk=fname(xk)
    if fxk==0:
        return xk, it, v_xk

    if abs(fxk) < tolx or (b-a) / 2 < tolx:
        return xk, it, v_xk
    
    if sign(fa)*sign(fxk) < 0:   
        b = xk
        fb = fxk
    else:
        a = xk
        fa = fxk


   return xk, it, v_xk


f = lambda x: x**3 - x - 2
root, n_iter, steps = metodo_bisezione(f, 1, 2, 1e-7, 1e-10)
print(f"Radice approssimata: {root}, in {n_iter} iterazioni.")
# ===== GRAFICO FACOLTATIVO =========== #
plt.figure(figsize=(10, 5))
plt.plot(range(1, len(steps)+1), steps, marker='o', linestyle='-')
plt.axhline(y=root, color='red', linestyle='--', label=f'Radice ≈ {root:.7f}')
plt.title("Convergenza del metodo di bisezione")
plt.xlabel("Iterazione")
plt.ylabel("Approssimazione xₖ")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()