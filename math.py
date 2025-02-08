"""
Acest modul prezintă
operații matematice de bază și utilitare.
"""

# Import modulul necesar
import math

# Constante
p = math.pi  #Constanta pentru valoarea lui PI

# Functii definite
def calcul_arie(raza):
    """
    Calculează aria unui cerc data fiind raza sa.

    Args:
        raza (float): Raza cercului.

    Ce returneaza:
        float: Aria cercului.

    Exceptii:
        ValueError: Daca raza este negativa.

    Examplu:
        >>> calcul_arie(2)
        12.566370614359172
    """
    if raza < 0:
        raise ValueError("Raza nu poate sa fie negativa")
    return p * raza ** 2


def calcul_factorial(num):
    """
    Calculeaza factorialul unui numar dat.

    Args:
        num (int): Numarul al carui factorial este calculat.

    Ce returneaza:
        int: Factorialul numarului dat.

    Exceptii:
        ValueError: Daca numarul este negativ.

    Examplu:
        >>> calcul_factorial(5)
        120
    """
    if num < 0:
        raise ValueError("Numarul nu poate sa fie negativ")
    return math.factorial(num)


# Demonstrarea utilizarii modulului
if __name__ == "__main__":
    print("Documentatia modulului:")
    print(__doc__)  # Afiseaza docstring-ul modulului

    # Afiseaza docstring-ul functiei
    print("\nDocumentatia functiei 'calcul_arie' :")
    print(calcul_arie.__doc__)
    
    print("\nDocumentatia functiei 'calcul_factorial' :")
    print(calcul_factorial.__doc__)

    # Exemplu de utilizare
    raza = 3
    print(f"\nAria cercului cu raza {raza} este {calcul_arie(raza)}")

    num = 5
    print(f"Factorialul numarului {num} este {calcul_factorial(num)}")

input()
