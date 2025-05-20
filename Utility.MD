## Metodi Iterativi per Sistemi Lineari

- Jacobi.py: Implementa il metodo iterativo di Jacobi per risolvere sistemi lineari con matrici diagonali dominanti.
- Gauss_Seidel.py: Metodo iterativo simile a Jacobi, con aggiornamento sequenziale più efficiente.
- Gauss_Seidel_SOR.py: Variante del metodo di Gauss-Seidel con sovra-rilassamento per accelerare la convergenza.
- SteepestDescent.py: Metodo del gradiente discendente per sistemi lineari, semplice ma con convergenza lenta.
- Conjugate_Gradient.py: Metodo del gradiente coniugato, più efficiente e adatto a matrici simmetriche positive definite.

---

## Metodi per Sistemi Non Lineari e Ottimizzazione

- Newton.py, Newtonsys.py: Metodi di Newton per equazioni non lineari e sistemi di equazioni.
- My_NewtonSys_corde.py: Metodo di Newton con Jacobiano fisso (variante delle corde).
- My_NewtonSys_sham.py: Variante modificata di Newton con aggiornamenti approssimati.
- My_Newton_minimo.py, My_Newton_minimo_MOD.py: Metodi di Newton applicati a problemi di minimizzazione.

---

## Interpolazione Polinomiale

- plagr.py: Calcola i polinomi base di Lagrange dati un insieme di nodi.
- InterpL.py: Calcola il polinomio interpolante usando la formula di Lagrange in punti dati.

---

## Risoluzione di Sistemi Sovradeterminati (Least Squares)

- eqnorm.py: Metodo delle equazioni normali per minimi quadrati, meno stabile ma semplice.
- qrLS.py: Risoluzione tramite fattorizzazione QR, più stabile e usato frequentemente.
- SVDLS.py: Risoluzione tramite decomposizione ai valori singolari, numericamente molto stabile.

---

## Metodi di Ricerca Radici e Approssimazioni

- bisezione.py: Metodo della bisezione per trovare radici di funzioni continue in un intervallo, semplice e garantito.
- corde.py: Metodo delle corde per trovare radici di equazioni non lineari.
- falsi.py: Metodo dei falsi punti per la ricerca di radici.
- secanti.py: Metodo delle secanti, simile a Newton ma senza calcolare la derivata.
- stima.py: Funzioni di stima o approssimazione (da dettagliare).

---

## Funzioni Ausiliarie

- SolveTriangular.py: Funzioni per risolvere sistemi triangolari superiori o inferiori, utilizzate come sottoprogrammi.

---
