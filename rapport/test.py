def get_convertisseur(format_source: str, format_cible: str):
    if format_source == "csv" and format_cible == "json":
        return CsvVersJson()
    elif format_source == "json" and format_cible == "csv":
        return JsonVersCsv()
    elif format_source == "csv" and format_cible == "xml":
        return CsvVersXml()
    # ... etc.
    else:
        raise ValueError(f"Conversion non supportée : {format_source} → {format_cible}")






    class FabriqueConvertisseur:
    _convertisseurs: dict[tuple[str, str], type[Convertisseur]] = {
        ("csv", "json"): CsvVersJson,
        ("json", "csv"): JsonVersCsv,
        ("csv", "xml"):  CsvVersXml,
        ("xml", "csv"):  XmlVersCsv,
        ("json", "xml"): JsonVersXml,
        ("xml", "json"): XmlVersJson,
        ("md",  "html"): MarkdownVersHtml,
    }

    @classmethod
    def creer(cls, format_source: str, format_cible: str) -> Convertisseur:
        cle = (format_source, format_cible)
        classe = cls._convertisseurs.get(cle)
        if classe is None:
            raise ValueError(f"Conversion non supportée : {format_source} → {format_cible}")
        return classe()
    