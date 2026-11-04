from composite import Dossier
from feuille import Fichier

musique = Dossier("Musique")
rock = Dossier("Rock")
classique = Dossier("Classique")

rock.ajouter(Fichier("bohemian_rhapsody.mp3", 8200))
rock.ajouter(Fichier("hotel_california.mp3", 6500))
classique.ajouter(Fichier("beethoven_9.mp3", 45000))

musique.ajouter(rock)
musique.ajouter(classique)
musique.ajouter(Fichier("playlist.m3u", 2))


print(f"Taille totale : {musique.calculer_taille()} Ko")
print(f"Nombre de fichiers : {musique.nb_fichiers()}")
musique.afficher()