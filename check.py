from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

dati = loadmat('testI')
A = dati["A"].astype(float)
b = dati["b"].astype(float).flatten()
def diagDom(A):
    A = np.array(A)
    n = A.shape[0]
    if A.shape[0] != A.shape[1]:
        return False
    for i in range(n):
        diag_elem = abs(A[i, i])
        off_diag_sum = sum(abs(A[i, j]) for j in range(n) if j != i)
        if diag_elem < off_diag_sum:
            return False    
    return True

def check_mat(A):
    isSym = np.allclose(A, A.T)
    isPos = isSym and np.all(np.linalg.eigvals(A) > 0)
    diagDom_res = diagDom(A)
    return isSym, isPos, diagDom_res

print(check_mat(A))