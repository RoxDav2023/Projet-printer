# variable
option1="imprimante Canon MegaTank MAXIFY GX7120"
option2="imprimante Epson EcoTank Pro ET-5800"
prix_canon=1139.99
prix_epson=1099.99
prix_imprimente = "prix de l'imprimente selon l'option choisie"
prix_offre = "prix de l'offre selon l'offre choisie"
option3="option 3 offre 2 bouteille d'encre noir par imprimante acheter"
option4="option 4 offre 1 bouteille dencre noir, cyan, magenta et jaune"
option5="je ne vuex pas d'offre"
prix_offre_noir=19.99
prix_offre_couleur=39.98


#compagnie binevenu
print("_" * 50)
print()
print("Bienvenu sur staples que souhaitez-vous acheter")
print("_" * 50)
print()


#option dimprimante
print("option 1 - imprimante Canon MegaTank MAXIFY GX7120 au prix de 1139.99$")
print()
print("option 2 - imprimante Epson EcoTank Pro ET-5800 au prix de 1099.99$")
print()


#input choisire son option
option_choisie = str(input("- Quel option choisisez-vous(1 ou 2): "))
print()


#affiche option choisi
option= option1 if option_choisie == "1" else option2
print(f"- vous avez choisi option: {option}")
print("_" * 50)
print()


#quantiter dimprimante acheter
quantiter=int(input("- Combien imprimante souhaitez-vous acheter: "))
print()
print(f"- vous avez indiquer vouloir {quantiter} {option} ")
print()
if option_choisie == "1":
    print(f"- voici combien vont couter vos imprimante {quantiter*prix_canon:.2f}")
else:
    print(f"- voici combien vont couter vos imprimante {quantiter*prix_epson:.2f}")
print("_" * 50)
print()


#offre dencre
print("- voici nos offre d'encre a l'achat d'une imprimante")
print()
print("option 3 offre 2 bouteille d'encre noir")
print()
print("option 4 offre 1 bouteille dencre noir, cyan, magenta et jaune")
print()
print("option 5 vous ne voulez pas profiter de l'offre d'encre")
print()

offre_choisie = str(input("- Quel option choisisez-vous(3, 4 ou 5 ): "))
print()
if offre_choisie == "3":
    offre = option3
    print("Vous avez choisi l'offre contenant une bouteille d'encre noir")
elif offre_choisie == "4":
    offre = option4
    print("Vous avez choisi l'offre contenant une bouteille d'ancre noir, cyan, magenta et jaune")
else:
    offre = option5
    print("vous avez refusez l'offre")

print("_" * 50)
print()

#Calcul du prix selon l'offre
if option_choisie == "1":
    prix_imprimente = prix_canon
else:
    if option_choisie == "2":
        prix_imprimente = prix_epson
if offre_choisie == "3":
    prix_offre = prix_offre_noir
elif offre_choisie == "4":
    prix_offre = prix_offre_couleur
else:
    if offre_choisie == "5":
        prix_offre = 0
prix_offretot = ((prix_imprimente + prix_offre) * quantiter)

#Calcul 
if quantiter >= 50:
    prixtotal = (prix_offretot - (prix_offretot * 0.05))
else:
    prixtotal = prix_offretot


#Sortie des donnees
print(f"Sous total des imprimentes: {prix_imprimente * quantiter:.2f} ")
print()
if offre_choisie == "3":
    print(f"Le sous total des cartouches est: {prix_offre_noir * quantiter:.2f}")
elif offre_choisie == "4":
    print(f"Le sous total des cartouches est de: {prix_offre_couleur * quantiter: .2f}")
else:
    print("Le sous total des cartouche est de: 0.00")
print()

if quantiter >= 50:
    print(f"Rabais: {prix_offretot * 0.05:.2f}")
else:
    print("Rabais: 0.00")
print()
print(f"Sous total incluant le rabais et cartouches: {prixtotal}")
print()
print()