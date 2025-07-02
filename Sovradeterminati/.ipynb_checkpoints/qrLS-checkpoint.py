def qrLS(A, b):
    """
    Risolve un sistema sovradeterminato con il metodo QR-LS
    """
    n = A.shape[1]  # numero di colonne di A
    Q, R = spLin.qr(A)
    h = Q.T @ b
    
    # Reshape h[:n] per renderlo compatibile con Usolve
    h_reshaped = h[:n].reshape(-1, 1)
    x, flag = Usolve(R[:n, :], h_reshaped)
    
    if flag == 1:
        print("Errore nella risoluzione del sistema triangolare")
        return None, None
    
    residuo = np.linalg.norm(h[n:])**2
    return x.flatten(), residuo  # Restituisce x come array 1D

# Esempio di utilizzo
if __name__ == "__main__":
    A = np.array([[1, 1], [1, 2], [1, 3]], dtype=float)
    b = np.array([6, 0, 0], dtype=float)

    x, residuo = qrLS(A, b)
    if x is not None:
        print(f"Soluzione approssimata: {x}")
        print("Residuo:", residuo)
        
        # Verifica della soluzione
        print("Verifica Ax - b:", A @ x - b)
        print("Norma del residuo:", np.linalg.norm(A @ x - b))