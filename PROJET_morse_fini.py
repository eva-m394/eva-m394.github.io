##création du dictionnaire
caracteres_morse= { "A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.", "0":"-----", ".":".-.-.-", "?":"..--..", "-":"-....-", "'":".----.", " ":" ", ",":"--..--"} 

def morse_encodage(txt): ##définition de la fonction
    txt=txt.upper() ##pour s'accorder avec le dictionnaire
    txt=[*txt] ##création d'une liste qui sépare tous les caractères de txt
    txt_final=""
    x=0 ##compteur
    for i in range(len(txt)): ##vérification des caractères
        if txt[i] not in caracteres_morse.keys(): ##si les caractères sont traduisibles
            return "Erreur. Le caractère '",txt[i],"' ne peut pas être traduit en morse."
        elif all(c in ".- " for c in txt): ##si le texte est déjà traduit (ne contient que "-","."," ")
            return "Erreur. Le texte que vous avez entré est déjà en morse."
    for i in range(len(txt)): ##extrait le morse correspondant au caractère
        if txt[i]!=" ":
            txt_final+=caracteres_morse[txt[x]]+" " ##on ajoute " " à la fin pour séparer les caratères
        else :
            txt[i]=" " ##on remplace un espace par " "
            txt_final+=" " ##on obtient "  " pour séparer deux mots
        x+=1
    return txt_final


def morse_decodage(txt):  ##définition de la fontion
    txt+=" " ##pour signifier la fin
    cara_morse="" 
    txt_final=""
    x=0 ##compteur
    for i in range(len(txt)): ##vérification des caractères
        if txt[i] not in caracteres_morse.values():
            return("Erreur. Le caractère '",txt[i],"' n'existe pas en morse.")
    for i in range(len(txt)): ##on extrait le caractère correspondant au morse
        if txt[i]!=" ":
            cara_morse+=txt[i] 
            x=0 ##pour compter les espaces (" ")
        else: 
            x+=1
            if x==2: ##nouveau mot ("  ")
                txt_final+=" "
            else: ##recherche inversée dans le dictionnaire
                j=list(caracteres_morse.values()) ##on extrait toutes les valeurs du dictionnaire
                j=j.index(cara_morse) ##trouver la position de cara_morse[i] dans les valeurs dictionnaire
                txt_final+=list(caracteres_morse.keys())[j] ##on extrait la clef correspondant à la valeur (j)
                cara_morse="" ##on réinitialise la variable
    return txt_final

quoi=input("Que voulez-vous faire ? (encoder/décoder): ")
txt=input("Entrez le texte: ")
if quoi=="encoder":
    print(morse_encodage(txt))
elif quoi=="décoder":
    print(morse_decodage(txt))
