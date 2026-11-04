from composant import Composant

class Composite(Composant):
    def __init__(self, nom):
        super().__init__(nom)
        self.enfant : list[Composant] = []


    def ajouter(self, composant: Composant) -> None:
        self.enfant.append(composant)

    def nb_pieces(self) -> int:
        return sum(e.nb_pieces() for e in self.enfant) // len(self.enfant) 


    def prix_total(self) -> float:
        return sum(e.prix_total() for e in self.enfant) / len(self.enfant)

    
    def afficher(self, prefix: str = "") -> None:
        print(f"{prefix}[{self.nom}]")
        for enfant in self.enfant:
            enfant.afficher(prefix + "   ")


class SousSysteme(Composite):
    pass

         
    



