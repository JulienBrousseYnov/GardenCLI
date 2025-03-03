def fertiliser(plante):
    plante.sante += 15
    plante.taille += plante.vitesse_croissance * 2
    print(f"{plante.nom} a été fertilisée et a grandi rapidement.")