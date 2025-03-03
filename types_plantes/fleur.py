from plante import Plante

class Fleur(Plante):
    def __init__(self, nom, besoin_eau, besoin_lumiere, vitesse_croissance, couleur):
        super().__init__(nom, besoin_eau, besoin_lumiere, vitesse_croissance)
        self.couleur = couleur

    def afficher_etat(self):
        print(f"{self.nom} - Couleur: {self.couleur} - Santé: {self.sante}")

    def entretenir(self):
        self.sante += 5
        if self.sante > 100:
            self.sante = 50  # Assurez-vous que la santé ne dépasse pas 100
        print(f"Entretenir {self.nom} - Santé après entretien: {self.sante}")