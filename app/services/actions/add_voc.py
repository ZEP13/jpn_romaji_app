from app.repository import voc as voc_repo


def add_vocabulary() -> str:
    while True:
        input_jpn = input("Entrez le mot japonais: ").strip()
        input_fr = input("Entrez la traduction française: ").strip()

        existing_jpn = voc_repo.find_trad_fr_jpn(input_fr)
        existing_fr = voc_repo.find_trad_jpn_fr(input_jpn)

        if existing_jpn:
            jpn_words = [jpn for _, jpn in existing_jpn]

            still_want = input(
                f"Le mot français '{
                    input_fr}' existe déjà avec la traduction japonaise "
                f"'{', '.join(jpn_words)
                    }'. Voulez-vous quand même l'ajouter? (o/n): "
            ).strip().lower()

            if still_want != 'o':
                return "Ajout de vocabulaire annulé."

        if existing_fr:
            fr_words = [fr for fr, _ in existing_fr]

            still_want = input(
                f"Le mot japonais '{
                    input_jpn}' existe déjà avec la traduction française "
                f"'{', '.join(fr_words)
                    }'. Voulez-vous quand même l'ajouter? (o/n): "
            ).strip().lower()

            if still_want != 'o':
                return "Ajout de vocabulaire annulé."

        voc_repo.add_vocabulary(input_jpn, input_fr)
        print("Nouveau vocabulaire ajouté avec succès.")
        if input("Voulez-vous ajouter un autre mot? (o/n): ").strip().lower() != 'o':
            return "Fin de l'ajout de vocabulaire."
