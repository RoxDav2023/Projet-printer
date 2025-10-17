# variable
option1="option 1 imprimante Canon MegaTank MAXIFY GX7120 au prix de 1139.99$"
option2="option 2 imprimante Epson EcoTank Pro ET-5800 au prix de 1099.99$"

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
print(f"vous avez choisi option: {option}")