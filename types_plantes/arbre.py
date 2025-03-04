from plante import Plante

class Arbre(Plante):
    def __init__(self, nom, besoin_eau, besoin_lumiere, vitesse_croissance, hauteur_max):
        super().__init__(nom, besoin_eau, besoin_lumiere, vitesse_croissance)
        self.hauteur_max = hauteur_max
        self.sante = 100

    def afficher_etat(self):
        print(f"{self.nom} - Santé: {self.sante} - Hauteur maximale: {self.hauteur_max}m")

    def entretenir(self):
        self.sante += 10
        if self.sante > 100:
            self.sante = 250 
        print(f"Entretenir {self.nom} - Santé après entretien: {self.sante}")

    def arroser(self, quantite):
        self.sante += + quantite
        if self.sante > 100:
            self.sante = 250
        print(f"Arroser {self.nom} - Santé après arrosage: {self.sante}")

    def fertiliser(self):
        self.sante += 20
        if self.sante > 100:
            self.sante = 250
        print(f"Fertiliser {self.nom} - Santé après fertilisation: {self.sante}")