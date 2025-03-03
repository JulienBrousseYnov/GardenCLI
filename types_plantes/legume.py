from plante import Plante

class Legume(Plante):
    def __init__(self, nom, besoin_eau, besoin_lumiere, vitesse_croissance, temps_croissance):
        super().__init__(nom, besoin_eau, besoin_lumiere, vitesse_croissance)
        self.temps_croissance = temps_croissance
        self.sante = 10

    def afficher_etat(self):
        print(f"{self.nom} - Santé: {self.sante} - Temps de croissance: {self.temps_croissance} jours")

    def entretenir(self):
        self.sante += 10
        if self.sante > 50:
            self.sante = 50
        print(f"Entretenir {self.nom} - Santé après entretien: {self.sante}")

    def arroser(self, quantite):
        self.sante += + quantite
        if self.sante > 50:
            self.sante = 50
        print(f"Arroser {self.nom} - Santé après arrosage: {self.sante}")

    def fertiliser(self):
        self.sante += 20
        if self.sante > 50:
            self.sante = 50
        print(f"Fertiliser {self.nom} - Santé après fertilisation: {self.sante}")