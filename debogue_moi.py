import datetime

def ajouter_apres_dernier(calendrier: dict, nom: str, duree: str) -> str:
    """
    Fonction pour ajouter un rendez-vous au premier moment disponible dans le caledrier
    :param calendrier: Calendrier de rendez-vous professionels
    :param nom: nom du patient
    :param duree: durée du nouveau rendez-vous
    :return: une confirmation avec l'heure du nouveau rendez-vous
    """
    dernier_rv = calendrier[-1]

    h = datetime.datetime.strptime(dernier_rv[0], "%h:%m")
    d = datetime.timedelta(minutes=dernier_rv[1])

    nouveau_debut = h + d + datetime.timedelta(minutes=15)

    heure_str = nouveau_debut.strftime("%h:%m")
    duree_str = duree.strftime("%m")

    calendrier[nom] = (heure_str, duree_str)

    return f"Rendez-vous confirmé à {heure_str}."

if __name__ == "__main__":
    rendez_vous = {
        "Amélie" : ("08:15","60"),
        "Hakim" : ("09:30","90"),
        "Bouchra" : ("11:15","60"),
        "Jacob" : ("13:45","30")
    }

    nom = input("Entrez le nom du patient : ")
    duree = input("Entrez la durée du rendez-vous, en minutes : ")
    print(ajouter_apres_dernier(rendez_vous, nom, duree))

