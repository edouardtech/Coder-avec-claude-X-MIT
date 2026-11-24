# ==========================================================
#  Leçon 2 — Mes réponses (1er essai) + corrections de Claude
# ==========================================================

# ===== 1. Le compte à rebours, version while 🚀 — ✅ JUSTE =====
compte = 10
while compte > 0 :
    print(compte)
    compte = compte - 1
print("Decollage")
# 👉 Parfait, réussi tout seul ! Détail : la consigne disait « Décollage ! 🚀 ».

# ===== 2. Le mot de passe 🔐 — ❌ =====
# Mot de passe = ""
# if Mot de passe == "polytechnique":
#     print("Mot de passe correct")
# else :
#     print("Faux")
# 👉 Un nom de variable ne peut pas contenir d'espaces : mot_de_passe.
# 👉 Il manque input() pour demander le mot de passe.
# 👉 if ne vérifie qu'UNE fois : pour redemander, il faut while.

# ===== 3. Le réservoir ⛽ — ✅ (réponse vue) =====
carburant = int(input("Carburant au départ ? "))
secondes = 0
while carburant >= 7:
    carburant = carburant - 7
    secondes = secondes + 1
print("La fusée vole", secondes, "secondes")
print("Il reste", carburant, "litres")
# 👉 Question : pourquoi >= 7 et pas > 7 ?

# ===== 4. Le nombre secret 🎮 — ❌ =====
# secret = 37
# while secret != 37:
#     print("recommence")
#         if secret < 15 :
#             print("Plus grand")
#                  elif :
#                       print("plus petit )
# 👉 Il manque la proposition du joueur (input) : c'est elle qu'on compare au secret.
# 👉 secret vaut 37, donc « secret != 37 » est faux : la boucle ne tourne jamais.
# 👉 Décalages incohérents → IndentationError. if / else doivent être alignés.
# 👉 elif a besoin d'une condition (ici, else suffit). Guillemet non fermé après « plus petit ».

# ===== 5. Syracuse 🔥 — pas encore fait =====
