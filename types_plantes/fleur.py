from plante import Plante

class Fleur(Plante):
    def __init__(self, nom, besoin_eau, besoin_lumiere, vitesse_croissance, couleur):
        super().__init__(nom, besoin_eau, besoin_lumiere, vitesse_croissance)
        self.couleur = couleur

    def afficher_etat(self):
        super().afficher_etat()
        print(f"Couleur: {self.couleur}")
