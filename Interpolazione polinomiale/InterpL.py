import numpy as np
import matplotlib.pyplot as plt
from plagr import plagr

def InterpL(x, y, xx):
    n = x.size
    m = xx.size
    L = np.zeros((m, n))
    for j in range(n):
        p = plagr(x, j)
        L[:, j] = np.polyval(p, xx)
    return L @ y

# Nodi e valori campionati (ad esempio funzione sin(x) su pochi punti)
x = np.array([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
y = np.sin(x)

# Punti per valutare il polinomio interpolante
xx = np.linspace(0, np.pi, 200)
yy = InterpL(x, y, xx)

# Plot
plt.plot(xx, yy, label='Polinomio interpolante')
plt.scatter(x, y, color='red', label='Nodi')
plt.plot(xx, np.sin(xx), linestyle='dashed', label='sin(x) reale')
plt.legend()
plt.grid(True)
plt.title("Interpolazione polinomiale con formula di Lagrange")
plt.show()
