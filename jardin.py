from plante import Plante
from types_plantes.fleur import Fleur
from types_plantes.legume import Legume
from types_plantes.arbre import Arbre
from actions.arroser import arroser
from actions.fertiliser import fertiliser
from actions.entretenir import entretenir

class Jardin:
    def __init__(self):
        self.plantes = []

    def ajouter_plante(self, plante):
        self.plantes.append(plante)

    def afficher_jardin(self):
        for plante in self.plantes:
            plante.afficher_etat()

    def interagir_avec_plante(self, nom_plante, action, *args):
        for plante in self.plantes:
            if plante.nom == nom_plante:
                if action == "arroser":
                    arroser(plante, args[0])
                elif action == "fertiliser":
                    fertiliser(plante)
                elif action == "entretenir":
                    entretenir(plante)
                else:
                    print("Action inconnue.")
                break
        else:
            print("Plante non trouvée.")