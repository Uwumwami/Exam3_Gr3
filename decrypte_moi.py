def dechiffrer_message(messages):
    """
    Cette fonction permet de déchiffrer les messages cryptés.
    :param messages: Les messages à déchiffrer
    :return: resultat
    """
    indice=0
    decalage = 3
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    chiffre = "1,2,3,4,5,6,7,8,9"
    resultat = ""

    # code de dechiffre inspiré de mes notes que j'ai pris quand je pratiquais.
    while indice>=3:
        mot_crypter = messages["cryptes"][indice]
        for caractere in mot_crypter:
            if caractere.isupper():
                lettre = caractere.lower()
                position = alphabet.index(lettre)
                nouvelle_position = (position - decalage) % 26
                resultat += alphabet[nouvelle_position]
            elif caractere.islower():
                position = alphabet.index(caractere)
                nouvelle_position = (position - decalage) % 26
                resultat += alphabet[nouvelle_position]
            elif caractere.isdigit():
                position = chiffre.index(caractere)
                nouvelle_position = (position - decalage) % 9
                resultat += chiffre[nouvelle_position]
            else:
                resultat += caractere
        indice += 1
    return resultat


def accuser_reception(messages_dechiffre,messages_gr):
    """
    Cette fonction permet d'avertit DebugWoman des messages qui ont été modifiés.
    :return:
    """
    print("Accusé-réception : ")
    if messages_gr["messages"][0] == messages_dechiffre or messages_gr["messages"][1] == messages_dechiffre or messages_gr["messages"][2] == messages_dechiffre :
        print("Aucun message intercepter.")

    elif messages_gr["messages"][0] != messages_dechiffre:
        print("Attention, le 1e message a été intercepté.")
        print("Nous accusons réception des messages 2 et 3")
    elif messages_gr["messages"][1] != messages_dechiffre:
        print("Attention, le 2ième message a été intercepté.")
        print("Nous accusons réception des message 1 et 3")
    else:
        print("Attention le 3ième message a été intercepté.")
        print("Nous accusons réception des messages 1 et 2")


if __name__ == "__main__":
    messages_gr3 = {
        "pseudo" : "DebugWoman",
        "messages" : ["Rendez vous au point 8 à midi", "Plan B activer en cas de problème", "Le code maître est 2345"],
        "cryptes" : ["Uhqghc yrxv dx srlqw 1 à plgl", "Sodq E dfwlyhu hq fdv gh sureoèph", "Oh frgh pdîwuh hvw 4567"]
    }
    message_dechiffre = dechiffrer_message(messages_gr3)
    accuser_reception(message_dechiffre,messages_gr3)
