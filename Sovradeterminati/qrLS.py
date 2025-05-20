import numpy as np
import scipy.linalg as spLin
from ..Funzioni_ausiliarie import SolveTriangular

def qrLS(A,b):
    #Risolve un sistema sovradeterminato con il metodo QR-LS
    n=A.shape[1]  # numero di colonne di A
    Q,R=spLin.qr(A)
    h = Q.T @ b
    x,flag=SolveTriangular.Usolve(R[:n, :],h[:n])
    residuo=np.linalg.norm(h[n:])**2
    return x,residuo

A = np.array([[1, 1], [1, 2], [1, 3]])
b = np.array([6, 0, 0])

x, residuo = qrLS(A, b)
print(f"Soluzione approssimata: {x}")
print("Residuo:", residuo)
