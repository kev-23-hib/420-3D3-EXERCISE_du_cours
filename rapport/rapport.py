from abc import ABC, abstractmethod
class rapport(ABC):

    @abstractmethod
    def genere(self):
        pass

class RapportTXT(rapport):

    def genere(self, donnes):
        return f"Rapport\n-------\n" + "\n".join(f"{k}: {v}" for k, v in donnees.items())


class RapportHTML(rapport):

    def genere(self, donnes):
        lignes = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in donnees.items())
        return f"<table>{lignes}</table>"


class RapportCSV(rapport):

    def genere(self, donnes):
        return "\n".join(f"{k},{v}" for k, v in donnees.items())"



class fabrique:
    _Rapport : dict[str, type[rapport]] = {
        "txt" : RapportTXT,
        "html" : RapportHTML,
        "csv" : RapportCSV
    }




donnees_txt = {"nom": "Alice", "age": 30}
rapport_txt = fabrique("txt", donnees_txt)
print(rapport_txt)

donnees_html = {"nom": "Alice", "age": 30}
rapport_html = fabrique("html", donnees_html)
print(rapport_html)

donnees_csv = {"nom": "Alice", "age": 30}
rapport_csv = fabrique("csv", donnees_csv)
print(rapport_csv)