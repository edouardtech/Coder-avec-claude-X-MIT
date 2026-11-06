# Leçon 1 — La boucle `for` 🔁

## 1. À quoi ça sert ?

Imagine que tu veux afficher « Bonjour » 5 fois. Sans boucle, tu écrirais :

```python
print("Bonjour")
print("Bonjour")
print("Bonjour")
print("Bonjour")
print("Bonjour")
```

C'est long… et si tu voulais le faire 1000 fois ? 😱
La boucle `for` sert à **répéter des instructions** sans tout recopier :

```python
for i in range(5):
    print("Bonjour")
```

## 2. Comment ça marche ?

```python
for i in range(5):
    print(i)
```

Affiche :
```
0
1
2
3
4
```

- `i` est une **variable** qui change à chaque tour (on l'appelle le *compteur*).
- `range(5)` donne les nombres **de 0 à 4** (5 nombres, mais on **commence à 0** et **5 n'est pas inclus** !).
- Les `:` à la fin de la ligne `for` sont **obligatoires**.
- Tout ce qui est **décalé (indenté) de 4 espaces** est répété.

⚠️ Attention à l'indentation :

```python
for i in range(3):
    print("dans la boucle")   # répété 3 fois
print("après la boucle")      # affiché 1 seule fois
```

## 3. Les 3 façons d'utiliser `range`

| Écriture | Nombres obtenus | Explication |
|---|---|---|
| `range(5)` | 0, 1, 2, 3, 4 | de 0 jusqu'à 5 **exclu** |
| `range(2, 6)` | 2, 3, 4, 5 | de 2 jusqu'à 6 **exclu** |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 | de 0 à 10 exclu, **de 2 en 2** |
| `range(10, 0, -1)` | 10, 9, …, 1 | à l'envers, de 10 à 1 |

💡 Astuce : `range(début, fin, pas)` → la **fin n'est jamais incluse**.

## 4. Exemples concrets

### Exemple A — La table de 3
```python
for i in range(1, 11):
    print("3 x", i, "=", 3 * i)
```

### Exemple B — Faire une somme (l'accumulateur)
On veut calculer 1 + 2 + 3 + … + 10 :
```python
total = 0                  # on part de 0
for i in range(1, 11):
    total = total + i      # on ajoute i au total à chaque tour
print("La somme vaut", total)   # 55
```
C'est une technique **super importante** : une variable créée **avant** la boucle, qu'on modifie **dans** la boucle, et qu'on affiche **après**.

### Exemple C — Parcourir un mot
`for` marche aussi sur les lettres d'un mot :
```python
for lettre in "FUSEE":
    print(lettre)
```
Affiche F, U, S, E, E (une lettre par ligne).

### Exemple D — Avec `input` et `if`
```python
n = int(input("Jusqu'à combien ? "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, "est pair")
```
Rappel : `i % 2` donne le **reste** de la division par 2 (0 si pair).

## 5. Les erreurs classiques 🐛

1. Oublier les `:` → `SyntaxError`
2. Oublier d'indenter → `IndentationError`
3. Croire que `range(10)` va jusqu'à 10 (non, il s'arrête à 9 !)
4. Mettre `total = 0` **dans** la boucle → il est remis à zéro à chaque tour

---

➡️ Maintenant, à toi de jouer : ouvre [`exercices.py`](exercices.py) !
