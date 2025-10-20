"""
Programmeurs: Roxane David et Sebastien Doucet

But: Cree un systeme de facturation d'imprimante

Date:2025-10-20

"""


#constante
OPTION1 = " imprimante Canon MegaTank MAXIFY GX7124"
OPTION2 = " imprimante Epson EcoTank Pro ET-5800"
PRIX_CANON = 1139.99
PRIX_EPSON = 1099.99
OFFRE1 = " Offre 1 comprend 2 bouteilles d'encre noire"
OFFRE2 = " Offre 2 comprend 1 bouteille d'encre noire, cyan, magenta et jaune"
OFFRE3 = " Offre 3 Vous-refusez l'offre"
PRIX_OFFRE_NOIR = 19.99
PRIX_OFFRE_COULEUR = 39.98


#variable
prix_offretot = float
prixtotal = float
quantiter = int
option = int
prix_imprimente = "Prix de l'imprimante selon l'option choisie"
prix_offre = "Prix de l'offre selon l'offre choisie"
option_choisie = int
offre = str


#compagnie bienvenu
print("_" * 124)
print()
print("Bienvenu chez Staples que souhaitez-vous acheter?")
print("_" * 124)
print()


#option d'imprimante
print("option 1 - imprimante Canon MegaTank MAXIFY GX7124 au prix de 1139.99$")
print()
print("option 2 - imprimante Epson EcoTank Pro ET-5800 au prix de 1099.99$")
print()


#input choisir son option
option_choisie = input("- Quelle option choisissez-vous? (1 ou 2): ")
print()


#affiche option choisi
option= OPTION1 if option_choisie == "1" else OPTION2
print(f"- Vous avez choisi l'option:{option}")
print("_" * 124)
print()


#quantiter d’imprimante acheter
quantiter=int(input("- Combien d'imprimante souhaitez-vous acheter?: "))
print()
print(f"- Vous avez indiqué vouloir {quantiter}{option} ")
print()
if option_choisie == "1":
    print(f"- Voici combien vont vous coutez vos imprimantes: {quantiter*PRIX_CANON:.2f}$")
else:
    print(f"- Voici combien vont vous coutez vos imprimantes: {quantiter*PRIX_EPSON:.2f}$")
print("_" * 124)
print()


#offre d'encre
print("- Voici nos offres d'encre à l'achat d'une imprimante")
print()
print(f"{OFFRE1}")
print()
print(f"{OFFRE2}")
print()
print(f"{OFFRE3}")
print()


#input choix de l'offre
offre_choisie = input("- Quelle offre choisissez-vous? (1, 2 ou 3 ): ")
print()
if offre_choisie == "1":
    offre = OFFRE1
    print("- Vous avez choisi l'offre 1 qui comprend 2 bouteilles d'encre noire par imprimante acheter")
elif offre_choisie == "2":
    offre = OFFRE2
    print("- Vous avez choisi l'offre 2 qui comprend 1 bouteille d'encre noire, cyan, magenta et jaune par imprimante acheter")
else:
    offre = OFFRE3
    print("- Vous avez refusé l'offre")

print("_" * 124)
print()

#Calcul du prix selon l'offre
if option_choisie == "1":
    prix_imprimente = PRIX_CANON
else:
    if option_choisie == "2":
        prix_imprimente = PRIX_EPSON
if offre_choisie == "1":
    prix_offre = PRIX_OFFRE_NOIR
elif offre_choisie == "2":
    prix_offre = PRIX_OFFRE_COULEUR
else:
    if offre_choisie == "3":
        prix_offre = 0
prix_offretot = ((prix_imprimente + prix_offre) * quantiter)

#Calcul 
if quantiter >= 124:
    prixtotal = (prix_offretot - (prix_offretot * 0.05))
else:
    prixtotal = prix_offretot


#Sortie des donnees
print(f"Le sous-total des imprimantes est de: {prix_imprimente * quantiter:.2f}$ ")
print()
if offre_choisie == "1":
    print(f"Le sous-total des bouteilles d'encre est de: {PRIX_OFFRE_NOIR * quantiter:.2f}$")
elif offre_choisie == "2":
    print(f"Le sous-total des bouteilles d'encre est de: {PRIX_OFFRE_COULEUR * quantiter: .2f}$")
else:
    print("Le sous-total des bouteilles d'encre est de: 0.00")
print()

if quantiter >= 124:
    print(f"- Nous vous offron un rabais de: {prix_offretot * 0.05:.2f}$")
else:
    print("Rabais: 0.00")
print()
print(f"Le sous-total incluant le rabais et les bouteilles d'encre est de: {prixtotal:.2f}$")
print()
print()