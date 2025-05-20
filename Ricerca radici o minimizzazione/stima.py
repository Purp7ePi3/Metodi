import numpy as np

def stima_ordine(xk,iterazioni):

     k=iterazioni-4
     p=np.log(abs(xk[k+2]-xk[k+3])/abs(xk[k+1]-xk[k+2]))/np.log(abs(xk[k+1]-xk[k+2])/abs(xk[k]-xk[k+1]))     
     ordine=p

     return ordine
