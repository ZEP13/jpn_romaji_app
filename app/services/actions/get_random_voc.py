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

        for id, fr, jpn, good_answers, all_answers in random_vocs:

            stats_word = (
                (good_answers / all_answers) * 100
                if all_answers > 0 else 0
            )

            if lang_choice == 'jpn':
                print(f"{fr}  (réussite: {stats_word:.1f}%)")
                reponse = input("Traduction en japonais: ").strip()
                if reponse == jpn:
                    print("Correct!")
                    voc_repo.update_voc_stats(id, 1, 1)
                else:
                    print(f"Incorrect. La bonne réponse est: {jpn}")
                    voc_repo.update_voc_stats(id, 0, 1)
            else:
                print(f"{jpn}  (réussite: {stats_word:.1f}%)")
                reponse = input("Traduction en français: ").strip()
                if reponse == fr:
                    print("Correct!")
                    voc_repo.update_voc_stats(id, 1, 1)
                else:
                    print(f"Incorrect. La bonne réponse est: {fr}")
                    voc_repo.update_voc_stats(id, 0, 1)
        return "Évaluation terminée."

    except Exception as e:
        return f"Une erreur s'est produite lors de la récupération des vocabulaires aléatoires: {e}"
