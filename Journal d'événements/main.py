# main.py

from journal import Journal

# Module de conversion
def convertir_fichier(nom: str) -> None:
    journal = Journal()
    journal.enregistrer(f"Début de la conversion : {nom}")
    # ... conversion ...
    journal.enregistrer(f"Conversion réussie : {nom}")

# Module de validation
def valider_fichier(nom: str) -> bool:
    journal = Journal()
    journal.enregistrer(f"Validation de {nom}")
    return True

# Programme principal
convertir_fichier("rapport.csv")
valider_fichier("rapport.csv")

# On veut consulter tout le journal ici
journal = Journal()
print(f"Nombre de messages enregistrés : {journal.nb_messages()}")
journal.afficher()