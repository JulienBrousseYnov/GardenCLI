from jardin import Jardin
from types_plantes.fleur import Fleur
from types_plantes.legume import Legume
from types_plantes.arbre import Arbre

def main():
    mon_jardin = Jardin()

    rose = Fleur("Rose", 50, 3, 0.5, "Rouge")
    tomate = Legume("Tomate", 60, 4, 0.7, 45)
    chene = Arbre("Chêne", 100, 5, 0.3, 20)

    mon_jardin.ajouter_plante(rose)
    mon_jardin.ajouter_plante(tomate)
    mon_jardin.ajouter_plante(chene)

    # Interaction avec les plantes
    mon_jardin.interagir_avec_plante("Rose", "arroser", 60)
    while True:
        print("\nActions disponibles :")
        print("1. Arroser une plante")
        print("2. Fertiliser une plante")
        print("3. Entretenir une plante")
        print("4. Afficher l'état du jardin")
        print("6. Ajouter une plante")
        print("5. Quitter")

        choix = input("Choisissez une action (1-6) : ")

        if choix == "1":
            plante = input("Entrez le nom de la plante à arroser : ")
            quantite = int(input("Entrez la quantité d'eau : "))
            mon_jardin.interagir_avec_plante(plante, "arroser", quantite)
        elif choix == "2":
            plante = input("Entrez le nom de la plante à fertiliser : ")
            mon_jardin.interagir_avec_plante(plante, "fertiliser")
        elif choix == "3":
            plante = input("Entrez le nom de la plante à entretenir : ")
            mon_jardin.interagir_avec_plante(plante, "entretenir")
        elif choix == "4":
            mon_jardin.afficher_jardin()
        elif choix == "5":
            print("Merci d'avoir joué !")
        elif choix == "6":
            print("Plantes disponibles à ajouter :")
            print("1. Rose (Fleur)")
            print("2. Tomate (Légume)")
            print("3. Chêne (Arbre)")
            print("4. Cerisier (Arbre)")
            type_plante = input("Choisissez une plante à ajouter (1-3) : ")
            if type_plante == "1":
                mon_jardin.ajouter_plante(Fleur("Rose", 50, 3, 0.5, "Rouge"))
                print("Rose ajoutée avec succès.")
            elif type_plante == "2":
                mon_jardin.ajouter_plante(Legume("Tomate", 60, 4, 0.7, 45))
                print("Tomate ajoutée avec succès.")
            elif type_plante == "3":
                mon_jardin.ajouter_plante(Arbre("Chêne", 100, 5, 0.3, 20))
                print("Chêne ajoutée avec succès.")
            else:
                print("Choix invalide, veuillez réessayer.")
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
