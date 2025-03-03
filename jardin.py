class Jardin:
    def __init__(self):
        self.plantes = []

    def ajouter_plante(self, plante):
        self.plantes.append(plante)

    def afficher_jardin(self):
        if not self.plantes:
            print("Il n'y a pas de plantes dans le jardin.")
        for plante in self.plantes:
            plante.afficher_etat()

    def interagir_avec_plante(self, nom, action, quantite=None):
        for plante in self.plantes:
            if plante.nom.lower() == nom.lower():
                if action == "arroser":
                    plante.arroser(quantite)
                elif action == "fertiliser":
                    plante.fertiliser()
                elif action == "entretenir":
                    plante.entretenir()
                break
        else:
            print("Plante non trouvée.")