from app.repository import voc as voc_repo
from colorama import Fore, Style


def find_jpn_voc() -> str:
    while True:
        input_fr = input("\nEntrez le mot francais à rechercher: ").strip()
        if input_fr.lower() == 'exit':
            return "\n Fin recherche"

        existing_jpn = voc_repo.find_trad_fr_jpn(input_fr)

        if existing_jpn:
            lines = [f"{fr} → {jpn}" for fr, jpn in existing_jpn]
            print(f"\nTraductions japonaises pour '{
                  input_fr}':\n" + "\n".join(lines))
        else:
            print(Fore.RED + f"\nAucune traduction japonnaise trouvée pour '{input_fr}'.")
            print(Style.RESET_ALL)
