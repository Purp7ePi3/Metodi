import numpy as np

def Usolve(U, b):
    """
    Risoluzione con procedura backward di Ux=b con U triangolare superiore  
    Input: U matrice triangolare superiore
           b termine noto
    Output: x: soluzione del sistema lineare
            flag=  0, se sono soddisfatti i test di applicabilità
                   1, se non sono soddisfatti
    """ 
    # Test dimensione
    m, n = U.shape
    flag = 0
    if n != m:
        print('errore: matrice non quadrata')
        flag = 1
        x = []
        return x, flag
    
    # Test singolarità
    if not np.all(np.diag(U) != 0):
        print('el. diag. nullo - matrice triangolare superiore')
        x = []
        flag = 1
        return x, flag
    
    # Preallocazione vettore soluzione
    x = np.zeros((n, 1))
    
    for i in range(n-1, -1, -1):
        s = np.dot(U[i, i+1:n], x[i+1:n])  # scalare = vettore riga * vettore colonna
        x[i] = (b[i] - s) / U[i, i]
    
    return x, flag

def Lsolve(L, b):
    """  
    Risoluzione con procedura forward di Lx=b con L triangolare inferiore  
    Input: L matrice triangolare inferiore
           b termine noto
    Output: x: soluzione del sistema lineare
            flag=  0, se sono soddisfatti i test di applicabilità
                   1, se non sono soddisfatti
    """
    # Test dimensione
    m, n = L.shape
    flag = 0
    if n != m:
        print('errore: matrice non quadrata')
        flag = 1
        x = []
        return x, flag
    
    # Test singolarità
    if not np.all(np.diag(L) != 0):
        print('el. diag. nullo - matrice triangolare inferiore')
        x = []
        flag = 1
        return x, flag
    
    # Preallocazione vettore soluzione
    x = np.zeros((n, 1))
    
    for i in range(n):
        s = np.dot(L[i, :i], x[:i])  # scalare = vettore riga * vettore colonna
        x[i] = (b[i] - s) / L[i, i]
    
    return x, flag