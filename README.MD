# Guida Completa ai Sistemi Lineari: Identificazione e Soluzioni Pratiche

## 1. Dimensioni del Sistema Lineare

### Sistemi Sovradeterminati (m > n)
- **Cosa significa**: Ci sono più equazioni (m) che incognite (n)
- **Come identificarlo**: Semplicemente contando le dimensioni della matrice A (m×n)
- **Conseguenze**: Non esiste generalmente una soluzione esatta, quindi si cercano soluzioni ai minimi quadrati
- **Esempio**: Un sistema con 10 equazioni e 3 incognite (matrice 10×3)
- **Metodi disponibili**:
  - `eqnorm.py`: Equazioni normali (per matrici ben condizionate)
  - `qrLS.py`: Fattorizzazione QR (più stabile numericamente)
  - `SVDLS.py`: Decomposizione ai valori singolari (massima stabilità numerica)

### Sistemi Quadrati (m = n)
- **Cosa significa**: Il numero di equazioni è uguale al numero di incognite
- **Come identificarlo**: La matrice A è quadrata (m×n con m=n)
- **Conseguenze**: Potrebbe esistere una soluzione unica, infinite soluzioni o nessuna soluzione
- **Esempio**: Un sistema con 5 equazioni e 5 incognite (matrice 5×5)
- **Metodi disponibili**:
  - Metodi diretti: `qrLS.py` (può essere adattato)
  - Metodi iterativi: `jacobi.py`, `gauss_seidel.py`, `gauss_seidel_sor.py`, `conjugate_gradient.py`, `steepestdescent.py`

## 2. Condizionamento della Matrice

### Matrice Ben Condizionata
- **Cosa significa**: Piccole variazioni nei dati di input causano piccole variazioni nella soluzione
- **Come identificarlo**: 
  - Calcolando il numero di condizionamento con `numpy.linalg.cond(A)`
  - Regola pratica: `cond(A) < 100` spesso indica un buon condizionamento
- **Conseguenze**: I metodi numerici sono stabili e accurati
- **Metodi appropriati e alternative**:
  - Per sistemi sovradeterminati:
    - **Ottimale**: Equazioni normali (`eqnorm.py`)
    - **Alternative**: `qrLS.py` (valida ma più costosa)
  - Per sistemi quadrati:
    - **Ottimale**: Fattorizzazione di Gauss (non direttamente implementata)
    - **Alternative**: `qrLS.py`, anche sistemi non lineari con `corde.py` impostando F(x)=Ax-b

### Matrice Mediamente Mal Condizionata
- **Cosa significa**: Sensibilità moderata alle perturbazioni
- **Come identificarlo**: `100 < cond(A) < 10⁶` (approssimativamente)
- **Conseguenze**: Alcuni metodi diretti potrebbero perdere precisione
- **Metodi appropriati e alternative**:
  - Per sistemi sovradeterminati:
    - **Ottimale**: Fattorizzazione QR (`qrLS.py`)
    - **Alternative**: `SVDLS.py` (più stabile ma più costosa)
    - **Da evitare**: `eqnorm.py` (il condizionamento peggiora al quadrato)
  - Per sistemi quadrati:
    - **Ottimale**: Fattorizzazione QR (non direttamente implementata)
    - **Alternative**: `qrLS.py` adattato, `conjugate_gradient.py` se è anche simmetrica

### Matrice Altamente Mal Condizionata
- **Cosa significa**: Estrema sensibilità alle perturbazioni
- **Come identificarlo**: 
  - `cond(A) > 10⁶` o la matrice è vicina alla singolarità
  - Errori di overflow quando si calcola `cond(A)`
  - Altri metodi producono soluzioni con valori NaN o estremamente grandi
- **Conseguenze**: La maggior parte dei metodi numerici può fallire o produrre risultati inaffidabili
- **Metodi appropriati e alternative**:
  - Per sistemi sovradeterminati:
    - **Ottimale**: SVD (`SVDLS.py`)
    - **Alternative**: Nessuna delle opzioni disponibili è adeguata
    - **Da evitare**: `eqnorm.py`, `qrLS.py` potrebbe dare risultati inaccurati
  - Per sistemi quadrati:
    - **Ottimale**: SVD (adattare `SVDLS.py`)
    - **Alternative**: In alcuni casi, metodi iterativi ben precondizionati potrebbero funzionare

## 3. Rango della Matrice

### Matrice a Rango Massimo
- **Cosa significa**: Per matrice m×n: rango(A) = min(m,n)
- **Come identificarlo**: Utilizzando NumPy: `numpy.linalg.matrix_rank(A)`
- **Conseguenze**: 
  - Per sistemi sovradeterminati: esiste una soluzione unica ai minimi quadrati
  - Per sistemi quadrati: esiste una soluzione unica
- **Metodi appropriati**: Tutti i metodi standard funzionano bene

### Matrice Non a Rango Massimo
- **Cosa significa**: Il rango è inferiore al minimo tra m e n
- **Come identificarlo**: `numpy.linalg.matrix_rank(A) < min(m,n)`
- **Conseguenze**: 
  - Per sistemi sovradeterminati: esistono infinite soluzioni ai minimi quadrati
  - Per sistemi quadrati: il sistema è singolare (infinità di soluzioni o nessuna)
- **Metodi appropriati e alternative**:
  - **Ottimale**: SVD (`SVDLS.py`) - fornisce la soluzione di norma minima
  - **Alternative**: Nessuna delle altre opzioni disponibili è adeguata
  - **Da evitare**: Tutti gli altri metodi che non gestiscono matrici singolari

## 4. Proprietà Strutturali della Matrice

### Matrice Simmetrica e Definita Positiva
- **Cosa significa**: 
  - A = A^T (simmetrica)
  - x^T·A·x > 0 per ogni x ≠ 0 (definita positiva)
- **Come identificarlo**: 
  - Simmetria: verificare che `A.T` sia uguale ad `A`
  - Definita positiva: tutti gli autovalori sono positivi (`numpy.all(numpy.linalg.eigvals(A) > 0)`)
  - Test alternativo: tutti i determinanti dei minori principali sono positivi
- **Conseguenze**: Garantisce convergenza di molti metodi iterativi
- **Metodi appropriati e alternative**:
  - **Ottimale**: 
    - Per matrici piccole: Fattorizzazione di Cholesky (disponibile con `numpy.linalg.cholesky(A)`)
    - Per matrici grandi e sparse: Gradiente coniugato (`conjugate_gradient.py`)
  - **Alternative**: 
    - `gauss_seidel.py` (convergenza garantita per matrici SPD)
    - `gauss_seidel_sor.py` (più veloce con parametro ottimale)
    - `steepestdescent.py` (più semplice ma convergenza più lenta)

### Matrice Diagonale Strettamente Dominante
- **Cosa significa**: Il valore assoluto di ogni elemento diagonale è maggiore della somma dei valori assoluti degli altri elementi nella stessa riga
- **Come identificarlo**: Per ogni riga i: |a_ii| > Σ|a_ij| (j≠i)
- **Test in codice**:
  ```python
  def is_diagonally_dominant(A):
      n = A.shape[0]
      for i in range(n):
          if abs(A[i,i]) <= sum(abs(A[i,j]) for j in range(n) if j != i):
              return False
      return True
  ```
- **Conseguenze**: Garantisce convergenza di metodi iterativi come Jacobi e Gauss-Seidel
- **Metodi appropriati e alternative**:
  - **Ottimale** (in ordine di efficienza crescente): 
    - `jacobi.py` (il più semplice)
    - `gauss_seidel.py` (converge più velocemente di Jacobi)
    - `gauss_seidel_sor.py` (il più efficiente con un buon parametro di rilassamento)
  - **Alternative**:
    - `conjugate_gradient.py` (se la matrice è anche simmetrica)
    - `steepestdescent.py` (se la matrice è anche simmetrica)

## 5. Densità della Matrice

### Matrice Densa
- **Cosa significa**: La maggior parte degli elementi è diversa da zero
- **Come identificarlo**: Più del 10-20% degli elementi sono non nulli
- **Test in codice**: `np.count_nonzero(A)/(A.shape[0]*A.shape[1]) > 0.1`
- **Conseguenze**: Richiede più memoria e operazioni
- **Metodi appropriati**:
  - **Ottimali**: Metodi diretti (adattare `qrLS.py` o usare NumPy)
  - **Alternative**: Per matrici di piccole dimensioni, anche i metodi iterativi possono funzionare

### Matrice Sparsa
- **Cosa significa**: La maggior parte degli elementi è zero
- **Come identificarlo**: Meno del 10% degli elementi sono non nulli
- **Test in codice**: `np.count_nonzero(A)/(A.shape[0]*A.shape[1]) < 0.1`
- **Conseguenze**: Si possono risparmiare memoria e operazioni usando formati di memorizzazione speciali
- **Metodi appropriati e alternative**:
  - **Ottimali**: Metodi iterativi (`jacobi.py`, `gauss_seidel.py`, `gauss_seidel_sor.py`, `conjugate_gradient.py`)
  - **Alternative**: Nessuna buona alternativa tra i metodi diretti per matrici molto grandi
  - **Da evitare**: Metodi diretti per sistemi molto grandi

## 6. Dimensione del Sistema

### Piccole Dimensioni
- **Cosa significa**: La matrice A ha dimensioni limitate
- **Come identificarlo**: Tipicamente n < 1000 (ma dipende dalla memoria disponibile)
- **Conseguenze**: I metodi diretti sono generalmente efficienti
- **Metodi appropriati e alternative**:
  - **Ottimali**: Adattare `qrLS.py` o usare funzioni di NumPy
  - **Alternative**: Tutti i metodi iterativi possono funzionare ma sono meno efficienti

### Grandi Dimensioni
- **Cosa significa**: La matrice A ha dimensioni elevate
- **Come identificarlo**: Tipicamente n > 1000
- **Conseguenze**: I metodi diretti possono essere troppo costosi in termini di memoria e tempo
- **Metodi appropriati e alternative**:
  - **Ottimali**: Metodi iterativi (`jacobi.py`, `gauss_seidel.py`, `gauss_seidel_sor.py`, `conjugate_gradient.py`)
  - **Alternative**: Nessuna buona alternativa tra i metodi diretti
  - **Da evitare**: Metodi diretti che richiedono la memorizzazione esplicita della matrice completa

## 7. Albero Decisionale con Alternative Pratiche

```
Il sistema è sovradeterminato (m > n)?
├── Sì:
│   ├── È ben condizionato (cond(A) < 100)?
│   │   ├── Sì: Usa eqnorm.py
│   │   │   └── Alternative: qrLS.py (più stabile ma più costoso)
│   │   └── No: È altamente mal condizionato (cond(A) > 10^6) o rango non massimo?
│   │       ├── Sì: Usa SVDLS.py
│   │       │   └── Alternative: Nessuna valida
│   │       └── No: Usa qrLS.py
│   │           └── Alternative: SVDLS.py (più stabile ma più costoso)
└── No (m = n):
    ├── È di piccole dimensioni e densa?
    │   ├── Sì: È simmetrica e definita positiva?
    │   │   ├── Sì: Usa numpy.linalg.cholesky
    │   │   │   └── Alternative: conjugate_gradient.py, gauss_seidel.py
    │   │   └── No: È ben condizionata?
    │   │       ├── Sì: Usa numpy.linalg.solve o adatta qrLS.py
    │   │       │   └── Alternative: corde.py (impostando F(x)=Ax-b)
    │   │       └── No: Adatta qrLS.py o SVDLS.py
    │   │           └── Alternative: conjugate_gradient.py (se simmetrica)
    └── No (grande e sparsa):
        ├── È diagonale strettamente dominante?
        │   ├── Sì: Usa gauss_seidel_sor.py
        │   │   └── Alternative: gauss_seidel.py, jacobi.py
        └── È simmetrica e definita positiva?
            ├── Sì: Usa conjugate_gradient.py
            │   └── Alternative: gauss_seidel_sor.py, steepestdescent.py
            └── No: Prova gauss_seidel_sor.py 
                └── Alternative: jacobi.py, steepestdescent.py (con cautela)
```

## 8. Tabella Riassuntiva dei Metodi Disponibili con Alternative

| Scenario | Caratteristiche | Metodo Ottimale | Alternative Pratiche | Da Evitare |
|----------|----------------|-----------------|---------------------|------------|
| Sovradeterminato ben condizionato | m>n, cond(A)<100 | `eqnorm.py` | `qrLS.py` | - |
| Sovradeterminato mediamente mal condizionato | m>n, 100<cond(A)<10^6 | `qrLS.py` | `SVDLS.py` | `eqnorm.py` |
| Sovradeterminato altamente mal condizionato | m>n, cond(A)>10^6 | `SVDLS.py` | Nessuna valida | Tutti gli altri |
| Sovradeterminato non a rango massimo | m>n, rank(A)<n | `SVDLS.py` | Nessuna valida | Tutti gli altri |
| Quadrato piccolo e denso, ben condizionato | m=n<1000, denso, cond(A)<100 | Adatta `qrLS.py` | `corde.py` | - |
| Quadrato piccolo e denso, mal condizionato | m=n<1000, denso, cond(A)>100 | Adatta `qrLS.py` | `SVDLS.py` | `eqnorm.py` |
| Quadrato piccolo e denso, SPD | m=n<1000, denso, A=A^T, def. pos. | `numpy.linalg.cholesky` | `conjugate_gradient.py`, `gauss_seidel.py` | - |
| Quadrato grande e sparso, diagonale dominante | m=n>1000, sparso, diag. dom. | `gauss_seidel_sor.py` | `gauss_seidel.py`, `jacobi.py` | Metodi diretti |
| Quadrato grande e sparso, SPD | m=n>1000, sparso, A=A^T, def. pos. | `conjugate_gradient.py` | `gauss_seidel_sor.py`, `steepestdescent.py` | Metodi diretti |
| Quadrato grande e sparso, generico | m=n>1000, sparso | `gauss_seidel_sor.py` (tentativo) | `jacobi.py` (tentativo) | Metodi diretti |