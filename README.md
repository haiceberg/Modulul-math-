# Modulul 'math' - prezentare generala prin exemple

# Operatii de baza:

Acest modul oferă funcții pentru realizarea unor operații matematice de bază, cum ar fi:

 * Calcularea ariei unui cerc
 * Calcularea factorialului unui număr

Modulul include și documentația necesară pentru a explica modul de utilizare al funcțiilor și cum să le apelați.

# Funcționalități:
 ### 1. Calcularea ariei unui cerc
* Funcția calcul_arie(raza) calculează aria unui cerc având ca parametru raza cercului. 
* Formula utilizată este: Aria = pi * raza^2.
* Dacă raza este negativă, va fi ridicată o excepție **ValueError**.

 __Exemplu de utilizare:__
Dacă se apelează funcția cu valoarea 2 pentru raza, rezultatul va fi 12.566370614359172.

  ### 2. Calcularea factorialului unui număr
* Funcția calcul_factorial(num) calculează factorialul unui număr întreg.
* Factorialul unui număr n este produsul tuturor numerelor întregi pozitive mai mici sau egale cu n.
* Dacă numărul este negativ, va fi ridicată o excepție **ValueError**.

__Exemplu de utilizare:__
Dacă se apelează funcția cu valoarea 5 pentru număr, rezultatul va fi 120.

# Detalii tehnice:
__Constante__
p - reprezintă valoarea constantei pi folosită în calculul ariei cercului.

# __Funcții__:
## 1) calcul_arie(raza)

### Descriere: Calculează aria unui cerc având ca parametru raza.
* __Argumente:__
raza (float): Raza cercului.

* __Returnează:__
Aria cercului (float).

* __Excepții:__
Ridică o excepție ValueError dacă raza este negativă.
## 2) calcul_factorial(num)

### Descriere: Calculează factorialul unui număr întreg.
* __Argumente:__
num (int): Numărul al cărui factorial este calculat.

* __Returnează:__
Factorialul numărului (int).

* __Excepții:__
Ridică o excepție ValueError dacă numărul este negativ.

# Demonstrarea utilizării:
* În cadrul scriptului principal, se afișează documentația completă a modulului și a funcțiilor sale, iar exemplele de utilizare sunt prezentate în următoarele linii:

* Dacă raza cercului este 3, programul va calcula aria cercului și o va afișa. De asemenea, dacă se calculează factorialul numărului 5, rezultatul va fi 120.

* Ieșirea va fi similară cu:
  *  Aria cercului cu raza 3 este 28.274333882308138
  *  Factorialul numărului 5 este 120

# Instalare:
Pentru a utiliza acest modul, trebuie doar să importați fișierul Python în proiectul dumneavoastră. Nu sunt necesare instalări suplimentare de pachete externe.
