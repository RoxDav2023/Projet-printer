# variable
option1="imprimante Canon MegaTank MAXIFY GX7120"
option2="imprimante Epson EcoTank Pro ET-5800"
prix_canon=1139.99
prix_epson=1099.99
option3="option 3 offre 2 bouteille d'encre noir par imprimante acheter"
option4="option 4 offre 1 bouteille dencre noir, cyan, magenta et jaune"
option5="je ne vuex pas d'offre"
prix_offre_noir=19.99
prix_offre_couleur=39.98
#compagnie binevenu
print("_" * 50)
print("Bienvenu sur staples que souhaite vous acheter")
print("_" * 50)

#option dimprimante
print("option 1 imprimante Canon MegaTank MAXIFY GX7120 au prix de 1139.99$")
print("option 2 imprimante Epson EcoTank Pro ET-5800 au prix de 1099.99$")

#input choisire son option
option_choisie = str(input("- Quel option choisisez-vous(1 ou 2): "))

#affiche option choisi
option= option1 if option_choisie == "1" else option2
print(f"- vous avez choisi option: {option}")
print("_" * 50)

#quantiter dimprimante acheter
quantiter=int(input("- Combien imprimante souhaitez-vous acheter: "))
print(f"- vous avez indiquer vouloir {quantiter} {option} ")
if option_choisie == "1":
    print(f"- voici combien vont couter vos imprimante {quantiter*prix_canon}")
else:
    print(f"- voici combien vont couter vos imprimante {quantiter*prix_epson}")
print("_" * 50)
    
#offre dencre
