from abc import ABC, abstractmethod
from composant import Composant


class composite(ABC, Composant):
    def __init__(self, nom: str) -> None:
        super().__init__(nom)
        self.enfants : list[Composant] = []

    def ajouter(self, composant: Composant) -> None:
        self.enfants.append(composant)

    def calculer_taille(self) -> int:
        taille_totale = 0
        for enfant in self.enfants:
            taille_totale += enfant.calculer_taille()
        return taille_totale

    def nb_fichiers(self) -> int:
        total_fichiers = 0
        for enfant in self.enfants:
            total_fichiers += enfant.nb_fichiers()
        return total_fichiers

    def afficher(self) -> None:
        print(f"[{self.nom}]")
        for enfant in self.enfants:
            enfant.afficher()