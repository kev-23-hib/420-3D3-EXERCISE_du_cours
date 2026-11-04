from feuille import PieceSimple
from composite import SousSysteme

moteur = SousSysteme("Moteur")
moteur.ajouter(PieceSimple("Bloc moteur", 1200.00))
moteur.ajouter(PieceSimple("Pistons (x4)", 320.00))
moteur.ajouter(PieceSimple("Joint de culasse", 85.00))

freins = SousSysteme("Système de freinage")
freins.ajouter(PieceSimple("Disques avant (x2)", 180.00))
freins.ajouter(PieceSimple("Plaquettes avant (x4)", 60.00))
freins.ajouter(PieceSimple("Maître-cylindre", 95.00))


moteur.ajouter(moteur)
freins.ajouter(freins)

print(f"Prix total : {freins.prix_total():.2f} $")
print(f"Nombre de pièces : {freins.nb_pieces()}")
freins.afficher()