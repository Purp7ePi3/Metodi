import numpy as np

def plagr(xnodi,j):
   """
   Restituisce i coefficienti del j-esimo pol di
   Lagrange associato ai punti del vettore xnodi
   """
   n=xnodi.size
   
   if j==0:
      xzeri=xnodi[1:n]
   else:
      xzeri = np.append(xnodi[:j], xnodi[j+1:n])
   
   num = np.poly(xzeri) # costruisce il polinomio dai suoi zeri
   den = np.prod(xnodi[j] - xzeri)
   
   p=num/den
   
   return p
