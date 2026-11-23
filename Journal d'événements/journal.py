

class Journal:
    _instance = None  # mémorise l'instance unique

    def __new__(cls):

        if cls._instance is None:
            # Première fois : on crée vraiment l'objet
            cls._instance = super().__new__(cls)
            # On initialise ici, pas dans __init__
            cls._instance._initialiser()
        return cls._instance 
    
    def  _initialiser(self):
        self._messages = []

        





    def __init__(self):
        self._messages = []
    
    def enregistrer(self, message: str) -> None:
        self._messages.append(message)

    def afficher(self) -> None:
        for msg in self._messages:
            print(msg)

    def nb_messages(self) -> int:
        return len(self._messages)