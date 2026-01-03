from app.services.actions import add_voc as add_voc_action
from app.services.actions import find_fr_voc as find_fr_voc_action
from app.services.actions import find_jpn_voc as find_jpn_voc_action
from app.services.actions import get_random_voc as get_random_voc_action


def main() -> None:
    print(" -------------------------------------------------------- ")
    print("\n   Options:\n")
    print(" -------------------------------------------------------- ")
    print("   1. Ajouter du vocabulaire")
    print("   2. Rechercher une traduction de japonais à français")
    print("   3. Rechercher une traduction de francais a japonais")
    print("   4. Evaluer connaissance sur vocabulaires aléatoires")
    print(" -------------------------------------------------------- ")
    print("\n   ESC. Quitter")
    while True:
        choice = input("\nChoisissez une option : ").strip()

        if choice == '1':
            result = add_voc_action.add_vocabulary()
            print(result)
        elif choice == '2':
            result = find_fr_voc_action.find_fr_voc()
            print(result)
        elif choice == '3':
            result = find_jpn_voc_action.find_jpn_voc()
            print(result)
        elif choice == '4':
            result = get_random_voc_action.get_random_voc()
            print(result)
        elif choice == "esc":
            break
        else:
            print("Option invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
