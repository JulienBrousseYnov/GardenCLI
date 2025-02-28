from plante import Plante

class Legume(Plante):
    def __init__(self, nom, besoin_eau, besoin_lumiere, vitesse_croissance, temps_recolte):
        super().__init__(nom, besoin_eau, besoin_lumiere, vitesse_croissance)
        self.temps_recolte = temps_recolte

    def afficher_etat(self):
        super().afficher_etat()
        print(f"Temps jusqu'à récolte: {self.temps_recolte} jours")