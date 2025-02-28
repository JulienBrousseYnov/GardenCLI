class Plante:
    def __init__(self, nom, besoin_eau, besoin_lumiere, vitesse_croissance):
        self.nom = nom
        self.besoin_eau = besoin_eau
        self.besoin_lumiere = besoin_lumiere
        self.vitesse_croissance = vitesse_croissance
        self.sante = 100  # Santé initiale
        self.taille = 1   # Taille initiale

    def afficher_etat(self):
        print(f"{self.nom} - Santé: {self.sante}, Taille: {self.taille}")