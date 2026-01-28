from app.repository import voc as voc_repo
from colorama import Style, Fore


def find_fr_voc() -> str:
    while True:
        input_jpn = input("\nEntrez le mot japonais à rechercher: ").strip()

        if input_jpn.lower() == 'exit':
            return "\n Fin recherche"

        existing_fr = voc_repo.find_trad_jpn_fr(input_jpn)

        if existing_fr:
            lines = [f"{fr} → {jpn}" for jpn, fr in existing_fr]
            print(f"\nTradructions japonaises pour '{
                  input_jpn}':\n" + "\n".join(lines))
        else:
            print(Fore.RED + f"\nAucune traduction française trouvée pour '{input_jpn}'.")
            print(Style.RESET_ALL)
