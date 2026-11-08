# ==========================================================
#  Leçon 1 — Mes réponses (1er essai) + corrections de Claude
# ==========================================================

# ===== 1. Le compte à rebours de la fusée 🚀 — ✅ JUSTE =====
for i in range (11,1,-1):
    print(i-1)
print("decollage")
# 👉 Ça marche ! Plus simple : range(10, 0, -1) puis print(i), sans le « - 1 ».
# 👉 Détail : la consigne demandait « Décollage ! 🚀 ».

# ===== 2. La table de multiplication — ❌ presque =====
nombre = int(input("nombre :"))
for i in range (1,11):
    print(nombre , "x" , i"=", nombre *i)
# 👉 SyntaxError : il manque une virgule entre i et "=".

# ===== 3. Le carburant de la fusée ⛽ — ✅ (réponse vue) =====
duree = int(input("Durée du vol ? "))
total = 0
for i in range(1, duree + 1):
    total = total + i
print("Carburant consommé :", total, "litres")
# 👉 À refaire sans regarder. Question : pourquoi « duree + 1 » ?

# ===== 4. Compter les voyelles 🔤 — ❌ pas fini =====
mot = input("Ton mot ? :")
nombre = 0
for lettre in (mot):
print("Il y a {nombre} voyelles")
# 👉 La boucle est vide → IndentationError. Il manque le test et le « + 1 ».
# 👉 Il manque le f devant les guillemets pour afficher la valeur de {nombre}.

# ===== 5. La pyramide de la fusée 🔥 — ❌ pas fini =====
n = float(input("nombre : "))
for i in range (1, n+1):
    print("*"
# 👉 float → range() veut un nombre entier : utilise int().
# 👉 Parenthèse fermante manquante après "*".
# 👉 Il manque les espaces et le bon nombre d'étoiles à chaque étage.
