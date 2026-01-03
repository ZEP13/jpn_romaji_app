from app.repository import voc as voc_repo


def find_jpn_voc() -> str:
    while True:
        input_fr = input("Entrez le mot francais à rechercher: ").strip()
        if input_fr.lower() == 'exit':
            return "Recherche terminée."

        existing_jpn = voc_repo.find_trad_fr_jpn(input_fr)

        if existing_jpn:
            lines = [f"{fr} → {jpn}" for fr, jpn in existing_jpn]
            return f"Traductions japonaises pour '{input_fr}':\n" + "\n".join(lines)
        else:
            return f"Aucune traduction japonnaise trouvée pour '{input_fr}'."
