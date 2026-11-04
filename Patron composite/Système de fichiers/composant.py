from abc import ABC, abstractmethod



class Composant(ABC):
    def __init__(self, nom: str) -> None:
        self.nom = nom

    @abstractmethod
    def calculer_taille(self) -> int:
        pass



    @abstractmethod
    def nb_fichiers(self) -> int:
        pass

    @abstractmethod
    def afficher(self, prefix: str = "") -> None:
        pass