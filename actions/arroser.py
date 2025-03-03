def arroser(plante, quantite_eau):
    if quantite_eau >= plante.besoin_eau:
        plante.sante += 10
        plante.taille += plante.vitesse_croissance
        print(f"{plante.nom} a été bien arrosée et a grandi.")
    else:
        plante.sante -= 5
        print(f"{plante.nom} n'a pas reçu assez d'eau et sa santé a diminué.")