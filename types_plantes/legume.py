from plante import Plante

class Legume(Plante):
    def __init__(self, nom, besoin_eau, besoin_lumiere, vitesse_croissance, temps_croissance):
        super().__init__(nom, besoin_eau, besoin_lumiere, vitesse_croissance)
        self.temps_croissance = temps_croissance

    def afficher_etat(self):
        print(f"{self.nom} - Santé: {self.sante} - Temps de croissance: {self.temps_croissance} jours")

    def entretenir(self):
        # Augmenter la santé du légume de 10 à chaque entretien
        self.sante += 10
        if self.sante > 100:
            self.sante = 100  # S'assurer que la santé ne dépasse pas 100
        print(f"Entretenir {self.nom} - Santé après entretien: {self.sante}")