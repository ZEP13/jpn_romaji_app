from app.repository import voc as voc_repo


def get_random_voc() -> str:
    try:
        number_input = input(
            "Combien de vocabulaires aléatoires souhaitez-vous obtenir? ").strip()
        if not number_input.isdigit() or int(number_input) <= 0:
            return "Veuillez entrer un nombre entier positif valide."
        number = int(number_input)

        random_vocs = voc_repo.get_number_of_rand_voc(number)
        if not random_vocs:
            return "Aucun vocabulaire trouvé."

        lang_choice = input(
            "Choisissez la langue pour l'évaluation (fr/jpn): ").strip().lower()
        if lang_choice not in ['fr', 'jpn']:
            return "Choix de langue invalide. Veuillez choisir 'fr' ou 'jpn'."

        for fr, jpn in random_vocs:
            if lang_choice == 'jpn':
                print(fr)
                reponse = input("Traduction en japonais: ").strip()
                if reponse == jpn:
                    print("Correct!")
                else:
                    print(f"Incorrect. La bonne réponse est: {jpn}")
            else:
                print(jpn)
                reponse = input("Traduction en français: ").strip()
                if reponse == fr:
                    print("Correct!")
                else:
                    print(f"Incorrect. La bonne réponse est: {fr}")

        return "Évaluation terminée."

    except Exception as e:
        return f"Une erreur s'est produite lors de la récupération des vocabulaires aléatoires: {e}"
