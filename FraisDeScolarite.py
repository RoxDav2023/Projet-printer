COUTREGULIER = 220 

COUTREDUIT = 200

FRAISTECH = 1500

TAUXTAX = 0.15

type_Etud = str 

nom_cours = int : nombre de cours auquel letudient ses inscrit 

frais_scol = float 

montant_tax = float

frais_tot = float

cout_pcours = float

taux_tax = float

type_Etud = str(input("Entrez le type d'etudient, R - retraite ou A - autre: "))

nom_cours = int(input("Veuillez entre le nombre de cours suivis: "))

if type_Etud = "R":
    cout_pcours = 200
    taux_tax = 0.0

else : 
    cout_pcours = 220

    taux_tax = 0.15

frais_scol = (nom_cours * cout_pcours)

montant_tax = (frais_scol * taux_tax)

frais_tot = (montant_tax + frais_scol + FRAISTECH)