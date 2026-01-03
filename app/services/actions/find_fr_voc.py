from app.repository import voc as voc_repo


def find_fr_voc() -> str:
    while True:
        input_jpn = input("\nEntrez le mot japonais à rechercher: ").strip()

        if input_jpn.lower() == 'exit':
            print("Recherche terminée.")

        existing_fr = voc_repo.find_trad_jpn_fr(input_jpn)

        if existing_fr:
            lines = [f"{fr} → {jpn}" for jpn, fr in existing_fr]
            print(f"\nTradructions japonaises pour '{
                  input_jpn}':\n" + "\n".join(lines))
        else:
            print(f"\nAucune traduction française trouvée pour '{input_jpn}'.")
