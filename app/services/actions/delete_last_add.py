from app.repository import voc as voc_repo


def delete_last_add() -> str:
    last_entry = voc_repo.get_last_added()
    if not last_entry:
        return "\nAucune entrée trouvée à supprimer."

    jpn, fr = last_entry
    confirm = input(
        f"\nLa dernière entrée ajoutée est '{jpn}' → '{fr}'. "
        "Voulez-vous la supprimer? (o/n): "
    ).strip().lower()

    if confirm == 'o':
        voc_repo.delete_vocabulary(jpn, fr)
        return "\nDernière entrée supprimée avec succès."
    else:
        return "\nSuppression annulée."
