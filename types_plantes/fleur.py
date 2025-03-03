from plante import Plante

class Fleur(Plante):
    def __init__(self, nom, besoin_eau, besoin_lumiere, vitesse_croissance, couleur):
        super().__init__(nom, besoin_eau, besoin_lumiere, vitesse_croissance)
        self.couleur = couleur
        self.sante = 20


    def afficher_etat(self):
        print(f"{self.nom} - Couleur: {self.couleur} - Santé: {self.sante}")

    def entretenir(self):
        self.sante += 10
        if self.sante > 100:
            self.sante = 100
        print(f"Entretenir {self.nom} - Santé après entretien: {self.sante}")

    def arroser(self, quantite):
        self.sante += + quantite
        if self.sante > 100:
            self.sante = 100
        print(f"Arroser {self.nom} - Santé après arrosage: {self.sante}")

    def fertiliser(self):
        self.sante += 10
        if self.sante > 100:
            self.sante = 100