from app.repository import voc as voc_repo


def find_jpn_voc() -> str:
    while True:
        input_fr = input("\nEntrez le mot francais à rechercher: ").strip()
        if input_fr.lower() == 'exit':
            print("Recherche terminée.")

        existing_jpn = voc_repo.find_trad_fr_jpn(input_fr)

        if existing_jpn:
            lines = [f"{fr} → {jpn}" for fr, jpn in existing_jpn]
            print(f"\nTraductions japonaises pour '{
                  input_fr}':\n" + "\n".join(lines))
        else:
            print(f"\nAucune traduction japonnaise trouvée pour '{input_fr}'.")
