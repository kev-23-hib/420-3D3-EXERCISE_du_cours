from composant import Composant

class feuille(Composant):
    pass



class Fichier(feuille):
    def __init__(self, nom: str, taille: int) -> None:
        super().__init__(nom)

        self.taille = taille  # en Ko

    def calculer_taille(self) -> int:
        return self.taille

    def nb_fichiers(self) -> int:
        return 1

    def afficher(self, prefix: str = "") -> None:
        print(f"{prefix}{self.nom} ({self.taille} Ko)")