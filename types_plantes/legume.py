from plante import Plante

class Legume(Plante):
    def __init__(self, nom, besoin_eau, besoin_lumiere, vitesse_croissance, temps_croissance):
        super().__init__(nom, besoin_eau, besoin_lumiere, vitesse_croissance)
        self.temps_croissance = temps_croissance
        self.sante = 10

    def afficher_etat(self):
        print(f"{self.nom} - Santé: {self.sante} - Temps de croissance: {self.temps_croissance} jours")

    def entretenir(self):
        # Augmenter la santé du légume de 10 à chaque entretien
        self.sante += 10
        if self.sante > 100:
            self.sante = 100  # S'assurer que la santé ne dépasse pas 100
        print(f"Entretenir {self.nom} - Santé après entretien: {self.sante}")

    def arroser(self, quantite):
    # Augmenter la santé de la fleur de 5 pour chaque unité d'eau
        self.sante += + quantite
        if self.sante > 50:
            self.sante = 50  # S'assurer que la santé ne dépasse pas 100
        print(f"Arroser {self.nom} - Santé après arrosage: {self.sante}")

    def fertiliser(self):
        # Augmenter la santé du légume de 20 à chaque fertilisation
        self.sante += 20
        if self.sante > 50:
            self.sante = 50
        print(f"Fertiliser {self.nom} - Santé après fertilisation: {self.sante}")