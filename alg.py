"""
Sistema di Raccomandazione per Metodi di Risoluzione di Sistemi Lineari
========================================================================

Basato sui codici forniti e sul README.MD, questo sistema raccomanda
il metodo ottimale in base a tre caratteristiche principali del sistema.

Uso: python metodi_selector.py <simmetrico> <positivo> <diag_dom>
Dove ogni parametro è 0 o 1:
- simmetrico: 0=non simmetrico, 1=simmetrico
- positivo: 0=non definito positivo, 1=definito positivo  
- diag_dom: 0=non diagonalmente dominante, 1=diagonalmente dominante

Esempi:
- python metodi_selector.py 0 0 0  → Matrice generica
- python metodi_selector.py 1 1 0  → Simmetrica definita positiva
- python metodi_selector.py 0 0 1  → Diagonalmente dominante
"""

import sys

def leggi_parametri_terminale():
    """
    Legge i parametri dal terminale.
    Formato: python script.py <simmetrico> <positivo> <diag_dom>
    """
    if len(sys.argv) != 4:
        return None
    
    try:
        params = [int(arg) for arg in sys.argv[1:4]]
        
        # Verifica che siano tutti 0 o 1
        if not all(p in [0, 1] for p in params):
            raise ValueError("Tutti i parametri devono essere 0 o 1")
        
        return params
    
    except ValueError as e:
        print(f"Errore nei parametri: {e}")
        return None

def raccomanda_metodo(simmetrico, positivo, diag_dom):
    """
    Raccomanda i metodi ottimali basati sulle caratteristiche del sistema.
    
    Args:
        simmetrico: 0=non simmetrico, 1=simmetrico
        positivo: 0=non definito positivo, 1=definito positivo  
        diag_dom: 0=non diagonalmente dominante, 1=diagonalmente dominante
    
    Returns:
        dict: Informazioni sui metodi raccomandati
    """
    
    # Mappatura delle caratteristiche
    sim_desc = "Simmetrica" if simmetrico else "Non simmetrica"
    pos_desc = "Definita positiva" if positivo else "Non definita positiva"
    diag_desc = "Diagonalmente dominante" if diag_dom else "Non diagonalmente dominante"
    
    print(f"ANALISI DELLA MATRICE:")
    print(f"\tSimmetria: {sim_desc}")
    print(f"\tPositività: {pos_desc}")
    print(f"\tDominanza diagonale: {diag_desc}")
    print("-" * 60)
    
    # Determina se è simmetrica definita positiva (SPD)
    spd = simmetrico and positivo
    
    # Metodi disponibili dai file forniti
    metodi_iterativi = {
        "conjugate_gradient": "Sistemi lineari iterativi/conjugate_gradient.py",
        "gauss_seidel": "Sistemi lineari iterativi/gauss_seidel.py", 
        "gauss_seidel_sor": "Sistemi lineari iterativi/gauss_seidel_sor.py",
        "jacobi": "Sistemi lineari iterativi/jacobi.py",
        "steepestdescent": "Sistemi lineari iterativi/steepestdescent.py"
    }
    
    metodi_diretti = {
        "eqnorm": "Sovradeterminati/eqnorm.py",
        "qrLS": "Sovradeterminati/qrLS.py", 
        "SVDLS": "Sovradeterminati/SVDLS.py"
    }
    
    metodi_newton = {
        "newton": "Newton e varianti/newton.py",
        "newton_mod": "Newton e varianti/newton_mod.py",
        "newtonsys": "Newton e varianti/newtonsys.py",
        "my_newtonSys_corde": "Newton e varianti/my_newtonSys_corde.py",
        "my_newtonSys_sham": "Newton e varianti/my_newtonSys_sham.py"
    }
    
    metodi_ricerca_radici = {
        "metodo_bisezione": "Ricerca radici o minimizzazione/metodo_bisezione.py",
        "secanti": "Ricerca radici o minimizzazione/secanti.py",
        "falsi": "Ricerca radici o minimizzazione/falsi.py",
        "corde": "Ricerca radici o minimizzazione/corde.py"
    }
    
    # Albero decisionale con ALMENO 2 metodi per caso
    if spd:  # Simmetrica definita positiva (1,1,x)
        if diag_dom:  # SPD + diagonalmente dominante (1,1,1)
            return {
                "metodo_primario": {
                    "nome": "conjugate_gradient.py",
                    "file": metodi_iterativi["conjugate_gradient"],
                    "descrizione": "Gradiente Coniugato - OTTIMALE per SPD",
                    "complessità": "O(n²√κ)",
                    "convergenza": "Garantita e veloce"
                },
                "metodo_secondario": {
                    "nome": "gauss_seidel_sor.py", 
                    "file": metodi_iterativi["gauss_seidel_sor"],
                    "descrizione": "Gauss-Seidel SOR - Doppia garanzia di convergenza",
                    "complessità": "O(n²) per iterazione", 
                    "convergenza": "Garantita (SPD + diag. dom.)"
                },
                "alternative": [
                    f"steepestdescent.py ({metodi_iterativi['steepestdescent']})",
                    f"gauss_seidel.py ({metodi_iterativi['gauss_seidel']})"
                ],
                "note": "🏆 CASO IDEALE: Entrambe le proprietà garantiscono convergenza"
            }
        else:  # SPD ma non diagonalmente dominante (1,1,0)
            return {
                "metodo_primario": {
                    "nome": "conjugate_gradient.py",
                    "file": metodi_iterativi["conjugate_gradient"], 
                    "descrizione": "Gradiente Coniugato - Metodo di elezione per SPD",
                    "complessità": "O(n²√κ)",
                    "convergenza": "Garantita per SPD"
                },
                "metodo_secondario": {
                    "nome": "steepestdescent.py",
                    "file": metodi_iterativi["steepestdescent"],
                    "descrizione": "Steepest Descent - Più semplice, convergenza garantita", 
                    "complessità": "O(n³) (più lento)",
                    "convergenza": "Garantita ma lenta per SPD"
                },
                "alternative": [
                    f"gauss_seidel.py ({metodi_iterativi['gauss_seidel']})",
                    "numpy.linalg.cholesky() per sistemi piccoli"
                ],
                "note": "SPD garantisce convergenza per entrambi i metodi"
            }
    
    elif diag_dom and not spd:  # Diagonalmente dominante ma non SPD
        if simmetrico:  # Simmetrica, diag. dom., non def. pos. (1,0,1)
            return {
                "metodo_primario": {
                    "nome": "gauss_seidel_sor.py",
                    "file": metodi_iterativi["gauss_seidel_sor"],
                    "descrizione": "Gauss-Seidel SOR - Convergenza garantita + accelerazione",
                    "complessità": "O(n²) per iterazione",
                    "convergenza": "Garantita (diag. dominante)"
                },
                "metodo_secondario": {
                    "nome": "gauss_seidel.py", 
                    "file": metodi_iterativi["gauss_seidel"],
                    "descrizione": "Gauss-Seidel classico - Più conservativo",
                    "complessità": "O(n²) per iterazione",
                    "convergenza": "Garantita (diag. dominante)"
                },
                "alternative": [
                    f"jacobi.py ({metodi_iterativi['jacobi']})",
                    f"steepestdescent.py ({metodi_iterativi['steepestdescent']}) - solo se SPD"
                ],
                "note": "Dominanza diagonale garantisce convergenza"
            }
        else:  # Non simmetrica, diag. dom., non def. pos. (0,0,1)
            return {
                "metodo_primario": {
                    "nome": "gauss_seidel_sor.py",
                    "file": metodi_iterativi["gauss_seidel_sor"],
                    "descrizione": "Gauss-Seidel SOR - Migliore per matrici diag. dominanti",
                    "complessità": "O(n²) per iterazione", 
                    "convergenza": "Garantita (diag. dominante)"
                },
                "metodo_secondario": {
                    "nome": "jacobi.py",
                    "file": metodi_iterativi["jacobi"],
                    "descrizione": "Jacobi - Sempre convergente per diag. dominanti",
                    "complessità": "O(n²) per iterazione",
                    "convergenza": "Garantita ma più lenta"
                },
                "alternative": [
                    f"gauss_seidel.py ({metodi_iterativi['gauss_seidel']})",
                    "Metodi diretti per sistemi piccoli"
                ],
                "note": "Dominanza diagonale garantisce convergenza per entrambi"
            }
    
    elif simmetrico and not positivo and not diag_dom:  # Solo simmetrica (1,0,0)
        return {
            "metodo_primario": {
                "nome": "gauss_seidel.py",
                "file": metodi_iterativi["gauss_seidel"],
                "descrizione": "Gauss-Seidel - Metodo conservativo per matrici simmetriche",
                "complessità": "O(n²) per iterazione",
                "convergenza": "Non garantita - monitorare"
            },
            "metodo_secondario": {
                "nome": "jacobi.py", 
                "file": metodi_iterativi["jacobi"],
                "descrizione": "Jacobi - Più stabile, convergenza più lenta",
                "complessità": "O(n²) per iterazione", 
                "convergenza": "Non garantita ma più robusto"
            },
            "alternative": [
                f"gauss_seidel_sor.py ({metodi_iterativi['gauss_seidel_sor']}) - con ω piccolo",
                "Metodi diretti se dimensioni ridotte"
            ],
            "note": "Convergenza non garantita - testare entrambi i metodi"
        }
    
    else:  # Matrice generica (0,0,0) o (0,1,0)
        return {
            "metodo_primario": {
                "nome": "jacobi.py",
                "file": metodi_iterativi["jacobi"],
                "descrizione": "Jacobi - Metodo più conservativo e robusto",
                "complessità": "O(n²) per iterazione",
                "convergenza": "Dipende dalla matrice"
            },
            "metodo_secondario": {
                "nome": "gauss_seidel.py",
                "file": metodi_iterativi["gauss_seidel"], 
                "descrizione": "Gauss-Seidel - Se converge, più veloce di Jacobi",
                "complessità": "O(n²) per iterazione",
                "convergenza": "Più rischioso ma potenzialmente più veloce"
            },
            "alternative": [
                f"gauss_seidel_sor.py ({metodi_iterativi['gauss_seidel_sor']}) - rischio divergenza",
                "numpy.linalg.solve() per sistemi piccoli",
                f"Metodi sovradeterminati: qrLS.py ({metodi_diretti['qrLS']})",
                f"Metodi Newton per sistemi non lineari: newtonsys.py ({metodi_newton['newtonsys']})"
            ],
            "note": "CASO DIFFICILE: Provare entrambi e verificare convergenza"
        }

def stampa_raccomandazione(raccomandazione):
    """Stampa la raccomandazione in formato leggibile"""
    
    print(f"METODI RACCOMANDATI:")
    print()
    print(f"METODO PRIMARIO:")
    print(f"File: {raccomandazione['metodo_primario']['file']}")
    print(f"Nome: {raccomandazione['metodo_primario']['nome']}")
    print(f"Descrizione: {raccomandazione['metodo_primario']['descrizione']}")
    print(f"Complessità: {raccomandazione['metodo_primario']['complessità']}")
    print(f"Convergenza: {raccomandazione['metodo_primario']['convergenza']}")
    
    print()
    print(f"METODO SECONDARIO:")
    print(f"File: {raccomandazione['metodo_secondario']['file']}")
    print(f"Nome: {raccomandazione['metodo_secondario']['nome']}")
    print(f"Descrizione: {raccomandazione['metodo_secondario']['descrizione']}")
    print(f"Complessità: {raccomandazione['metodo_secondario']['complessità']}")
    print(f"Convergenza: {raccomandazione['metodo_secondario']['convergenza']}")
    
    if 'note' in raccomandazione:
        print(f"\nNOTE: {raccomandazione['note']}")
    
    print(f"\nALTERNATIVE AGGIUNTIVE:")
    for alt in raccomandazione['alternative']:
        print(f"\t{alt}")

def main():
    """Funzione principale"""
    print("🔬 SISTEMA DI RACCOMANDAZIONE METODI NUMERICI")
    print("=" * 60)
        
    # Leggi parametri dal terminale
    params = leggi_parametri_terminale()
    if params is None:
        print("Uso corretto: python metodi_selector.py <simmetrico> <positivo> <diag_dom>")
        print("Usa 'python metodi_selector.py --help' per maggiori informazioni")
        return
    
    # Ottieni raccomandazione
    raccomandazione = raccomanda_metodo(*params)
    
    # Stampa risultati
    stampa_raccomandazione(raccomandazione)
    
    print(f"\nPARAMETRI INSERITI: {' '.join(map(str, params))}")
    print("=" * 60)
    print("💡 Usa 'python metodi_selector.py --help' per maggiori informazioni")

if __name__ == "__main__":
    main()