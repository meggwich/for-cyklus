# Projekt: Generovanie reťazca pomocou hovna, palíc a for-cyklov

## Popis

Tento projekt prijíma štyri vstupné parametre: šírku, výšku, slovo a oddeľovače. Na základe týchto parametrov sa vytvorí reťazec, ktorý sa následne spracováva rôznymi spôsobmi.

## Vstupné údaje

- `width`: Šírka reťazca (celé číslo)
- `height`: Výška reťazca (celé číslo)
- `word`: Slovo na spracovanie (reťazec s dĺžkou 6 znakov)
- `delimiters`: Oddeľovače na použitie (reťazec s dĺžkou 2 znaky)

## Popis práce kódu

Tento kód prijíma štyri vstupné parametre: šírku, výšku, slovo a oddeľovače. Na základe týchto parametrov generuje reťazec, ktorý sa následne spracováva rôznymi spôsobmi. Hlavné kroky práce kódu:

1. **Inicializácia premenných**: Vytvoria sa premenné na ukladanie medzivýsledkov a výsledkov.
2. **Spracovanie slova**: Vstupné slovo sa spracováva v niekoľkých krokoch, čím sa vytvárajú rôzne kombinácie znakov.
3. **Spracovanie oddeľovačov**: Vstupné oddeľovače sa tiež spracovávajú na vytvorenie rôznych kombinácií.
4. **Generovanie reťazca**: Hlavný cyklus generuje reťazec na základe spracovaných slov a oddeľovačov, pričom používa rôzne matematické operácie na vytvorenie unikátnych kombinácií.
5. **Špeciálne prípady**: Kód spracováva špeciálne prípady pre šírku a výšku, aby zabezpečil správne generovanie reťazca pre všetky možné hodnoty vstupných parametrov.

## Príklad vykonania kódu

Vstupné údaje:
```
width = 20
height = 14
word = 'matfyz'
delimiters = '()'
```

Výstupné údaje:
```
m(a)t(f)y(z)m(a)t(f)y(z)m(a)t(f)y(z)m(a
t)f(y)z(m)a(t)f(y)z(m)a(t)f(y)z(m)a(t)f
y(z)m(a)t(f)y(z)m(a)t(f)y(z)m(a)t(f)y(z
m)a(t)f(y)z(m)a(t)f(y)z(m)a(t)f(y)z(m)a
t(f)y(z)m(a)t(f)y(z)m(a)t(f)y(z)m(a)t(f
y)z(m)a(t)f(y)z(m)a(t)f(y)z(m)a(t)f(y)z
m(a)t(f)y(z)m(a)t(f)y(z)m(a)t(f)y(z)m(a
t)f(y)z(m)a(t)f(y)z(m)a(t)f(y)z(m)a(t)f
y(z)m(a)t(f)y(z)m(a)t(f)y(z)m(a)t(f)y(z
m)a(t)f(y)z(m)a(t)f(y)z(m)a(t)f(y)z(m)a
t(f)y(z)m(a)t(f)y(z)m(a)t(f)y(z)m(a)t(f
y)z(m)a(t)f(y)z(m)a(t)f(y)z(m)a(t)f(y)z
m(a)t(f)y(z)m(a)t(f)y(z)m(a)t(f)y(z)m(a
t)f(y)z(m)a(t)f(y)z(m)a(t)f(y)z(m)a(t)f
```

Tento príklad demonštruje, ako sa vstupné parametre transformujú do zložitého reťazca pomocou pomocou hovna, palíc a for-cyklov.

