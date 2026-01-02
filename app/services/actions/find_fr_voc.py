from app.repository import voc as voc_repo


def find_fr_voc() -> str:
    input_jpn = input("Entrez le mot japonais à rechercher: ").strip()

    existing_fr = voc_repo.find_trad_jpn_fr(input_jpn)

    if existing_fr:
        lines = [f"{fr} → {jpn}" for fr, jpn in existing_fr]
        return f"Traductions japonaises pour '{input_jpn}':\n" + "\n".join(lines)
    else:
        return f"Aucune traduction française trouvée pour '{input_jpn}'."
