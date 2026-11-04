from abc import ABC, abstractmethod

class Composant(ABC):
    def __init__(self, nom: str) -> None:
        self.nom = nom


    @abstractmethod
    def nb_pieces(self) -> int:
        pass


    @abstractmethod
    def prix_total(self) -> float:
        pass


    @abstractmethod
    def afficher(self, prefix: str = "") -> None:
        pass