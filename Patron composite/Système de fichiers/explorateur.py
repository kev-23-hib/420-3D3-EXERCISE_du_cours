class Fichier:
    def __init__(self, nom: str, taille: int):
        self.nom = nom
        self.taille = taille  # en Ko


class Dossier:
    def __init__(self, nom: str):
        self.nom = nom
        self.fichiers: list[Fichier] = []
        self.sous_dossiers: list["Dossier"] = []

    def ajouter_fichier(self, fichier: Fichier) -> None:
        self.fichiers.append(fichier)

    def ajouter_dossier(self, dossier: "Dossier") -> None:
        self.sous_dossiers.append(dossier)


class Explorateur:
    def __init__(self, racine: Dossier):
        self.racine = racine

    def taille_totale(self) -> int:
        total = 0
        for fichier in self.racine.fichiers:
            total += fichier.taille
        for sous_dossier in self.racine.sous_dossiers:
            for fichier in sous_dossier.fichiers:
                total += fichier.taille
            for sous_sous_dossier in sous_dossier.sous_dossiers:
                for fichier in sous_sous_dossier.fichiers:
                    total += fichier.taille
        return total

    def nb_fichiers(self) -> int:
        count = len(self.racine.fichiers)
        for sous_dossier in self.racine.sous_dossiers:
            count += len(sous_dossier.fichiers)
            for sous_sous_dossier in sous_dossier.sous_dossiers:
                count += len(sous_sous_dossier.fichiers)
        return count

    def afficher(self) -> None:
        print(f"[{self.racine.nom}]")
        for fichier in self.racine.fichiers:
            print(f"  {fichier.nom} ({fichier.taille} Ko)")
        for sous_dossier in self.racine.sous_dossiers:
            print(f"  [{sous_dossier.nom}]")
            for fichier in sous_dossier.fichiers:
                print(f"    {fichier.nom} ({fichier.taille} Ko)")
            for sous_sous_dossier in sous_dossier.sous_dossiers:
                print(f"    [{sous_sous_dossier.nom}]")
                for fichier in sous_sous_dossier.fichiers:
                    print(f"      {fichier.nom} ({fichier.taille} Ko)")