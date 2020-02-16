###VIGENERE###
#chr() ascii to latin
#ord() latin to ascii

#def tableau_chaine_caracteres(t[], caracteres):
#    for c in caracteres:
#        t.append(c)
#    return(t)



def chiffrage_vigenere(quoi,txt,clef): ##définition de la fonction
    ##définition des variables
    clef_ascii=[]
    txt_ascii=[]
    txt_final=""
    maj_min_sym=[] ##pour différencier les majuscules, minuscules et symboles/chiffres
    t=1 ##devient -1 si on cherche à décoder le texte
    j=0 ##compteur
    if (quoi!="décoder" and quoi!="encoder") or clef=="": ##vérification qu'il n'y a pas d'erreur
        return "Erreur. Veuillez recommencer."
    if quoi=="décoder": ##inversion pour faire le décodage
        t=-1
    clef=clef.lower()
    for i in clef: ##transformation de la clef en un tableau des caractères ascii correspondants
        clef_ascii.append(t*(ord(i)-97)) ##-97 pour que a=0, b=1, etc
    while len(clef_ascii)<len(txt): ##assemblage de la clef pour avoir assez de caractères
        clef_ascii+=clef_ascii
    clef_ascii=clef_ascii[:len(txt)]
    for i in txt: ##transformation du texte à crypter en ascii
        if 97<=ord(i)<=122: ##minuscules
            txt_ascii.append(ord(i)-97) ##-97 idem
            maj_min_sym.append("m")
        elif 65<=ord(i)<=90: ##majuscules
            txt_ascii.append(ord(i)-65) ##-65 pour que A=0, B=1, etc
            maj_min_sym.append("M")
        else: ##symboles/chiffres
            txt_ascii.append(ord(i)) ##on garde le même
            maj_min_sym.append("")
    for i in txt_ascii: ##encodage de chaque caractère selon son type
        if maj_min_sym[j]=="m": ##minuscules
            x=(i+clef_ascii[j])%26 ##(texte[i]+clef[i])%26 pour encoder, (texte[i]-clef[i])%26 pour décoder
            txt_final+=chr(x+97)
        elif maj_min_sym[j]=="M": ##majuscules
            x=(i+clef_ascii[j])%26
            txt_final+=chr(x+65)
        else: ##symboles/chiffres
            txt_final+=chr(i)
        j+=1 ##compteur
    return (txt_final)


z=input("Que voulez-vous faire? (encoder/décoder): ")
a=input("Entrez le texte: ")
c=input("Entrez la clef (sous forme de texte): ")
print(chiffrage_vigenere(z,a,c))
