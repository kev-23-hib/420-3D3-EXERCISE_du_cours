from composant import Composant

class Feuille(Composant):
    pass

class PieceSimple(Feuille):
    def __init__(self, nom, prix):
        super().__init__(nom)
        self.prix = prix

    def nb_pieces(self) -> int:
        return 1

    def prix_total(self) -> float:
        return self.prix

    def afficher(self, prefix: str = "") -> None:
        print(f"{prefix}{self.nom} ({self.prix} $)")
    




