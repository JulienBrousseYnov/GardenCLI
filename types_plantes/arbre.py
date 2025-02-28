from plante import Plante

class Arbre(Plante):
    def __init__(self, nom, besoin_eau, besoin_lumiere, vitesse_croissance, hauteur_max):
        super().__init__(nom, besoin_eau, besoin_lumiere, vitesse_croissance)
        self.hauteur_max = hauteur_max

    def afficher_etat(self):
        super().afficher_etat()
        print(f"Hauteur maximale: {self.hauteur_max} mètres")