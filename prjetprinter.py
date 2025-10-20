# variable
option1=" Imprimante Canon MegaTank MAXIFY GX7120"
option2=" Imprimante Epson EcoTank Pro ET-5800"
prix_canon=1139.99
prix_epson=1099.99
prix_imprimente = "Prix de l'imprimante selon l'option choisie"
prix_offre = "Prix de l'offre selon l'offre choisie"
offre1=" Offre 1 comprend 2 bouteilles d'encre noire par imprimante acheter"
offre2=" Offre 2 comprend 1 bouteille d’encre noire, cyan, magenta et jaune"
offre3=" Offre 3 Vous-refusez l'offre"
prix_offre_noir=19.99
prix_offre_couleur=39.98


#compagnie bienvenu
print("_" * 50)
print()
print("Bienvenu chez Staples que souhaitez-vous acheter")
print("_" * 50)
print()


#option d'imprimante
print("option 1 - imprimante Canon MegaTank MAXIFY GX7120 au prix de 1139.99$")
print()
print("option 2 - imprimante Epson EcoTank Pro ET-5800 au prix de 1099.99$")
print()


#input choisir son option
option_choisie = str(input("- Quelle option choisissez-vous (1 ou 2): "))
print()


#affiche option choisi
option= option1 if option_choisie == "1" else option2
print(f"- Vous avez choisi option: {option}")
print("_" * 50)
print()


#quantiter d’imprimante acheter
quantiter=int(input("- Combien imprimante souhaitez-vous acheter: "))
print()
print(f"- Vous avez indiqué vouloir {quantiter} {option} ")
print()
if option_choisie == "1":
    print(f"- Voici combien vont couter vos imprimantes {quantiter*prix_canon:.2f}")
else:
    print(f"- Voici combien vont couter vos imprimantes {quantiter*prix_epson:.2f}")
print("_" * 50)
print()


#offre d'encre
print("_" * 50)
print("- Voici nos offres d'encre à l'achat d'une imprimante")
print()
print(f"{offre1}")
print()
print(f"{offre2}")
print()
print(f"{offre3}")
print()

offre_choisie = str(input("- Quelle offre choisissez-vous (1, 2 ou 3 ): "))
print()
if offre_choisie == "1":
    offre = offre1
    print("Vous avez choisi l'offre 1 qui comprend 2 bouteilles d'encre noire par imprimante acheter")
elif offre_choisie == "2":
    offre = offre2
    print("Vous avez choisi l'offre 2 qui comprend 1 bouteille d'encre noire, cyan, magenta et jaune")
else:
    offre = offre3
    print("Vous avez refusé l'offre")

print("_" * 50)
print()

#Calcul du prix selon l'offre
if option_choisie == "1":
    prix_imprimente = prix_canon
else:
    if option_choisie == "2":
        prix_imprimente = prix_epson
if offre_choisie == "1":
    prix_offre = prix_offre_noir
elif offre_choisie == "2":
    prix_offre = prix_offre_couleur
else:
    if offre_choisie == "3":
        prix_offre = 0
prix_offretot = ((prix_imprimente + prix_offre) * quantiter)

#Calcul 
if quantiter >= 50:
    prixtotal = (prix_offretot - (prix_offretot * 0.05))
else:
    prixtotal = prix_offretot


#Sortie des donnees
print(f" Le sous-total des imprimantes est de: {prix_imprimente * quantiter:.2f} ")
print()
if offre_choisie == "1":
    print(f" Le sous-total des bouteilles d'encre est de: {prix_offre_noir * quantiter:.2f}")
elif offre_choisie == "2":
    print(f" Le sous-total des bouteilles d'encre est de: {prix_offre_couleur * quantiter: .2f}")
else:
    print("Le sous-total des bouteilles d'encre est de: 0.00")
print()

if quantiter >= 50:
    print(f"Nous vous offron un rabais de : {prix_offretot * 0.05:.2f}")
else:
    print("Rabais: 0.00")
print()
print(f" Le sous-total incluant le rabais et les bouteilles d'encre est de: {prixtotal}")
print()
print()