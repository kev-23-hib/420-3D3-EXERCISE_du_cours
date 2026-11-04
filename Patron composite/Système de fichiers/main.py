from explorateur import Fichier, Dossier, Explorateur

musique = Dossier("Musique")
rock = Dossier("Rock")
classique = Dossier("Classique")

rock.ajouter_fichier(Fichier("bohemian_rhapsody.mp3", 8200))
rock.ajouter_fichier(Fichier("hotel_california.mp3", 6500))
classique.ajouter_fichier(Fichier("beethoven_9.mp3", 45000))

musique.ajouter_dossier(rock)
musique.ajouter_dossier(classique)
musique.ajouter_fichier(Fichier("playlist.m3u", 2))

explorateur = Explorateur(musique)
print(f"Taille totale : {explorateur.taille_totale()} Ko")
print(f"Nombre de fichiers : {explorateur.nb_fichiers()}")
explorateur.afficher()