#chr(ascii)=> latin
#ord("latin")=> ascii

def cesar(quoi,texte,decalage,direction): ##définition de la fontion
    ##définition des variables
    txt_final=""
    txt_ascii=[]
    type_caractere=[] ##pour pouvoir distinguer le type de caractère (lettre majuscule ou minuscule, chiffre, symbole)
    if direction=="gauche" : ##inversion du décalage si on veut décoder ou s'il se fait vers la gauche
        decalage*=-1
    if quoi=="décoder" :
        decalage*=-1
    for i in texte: ##transformation du texte à crypter en un tableau des ascii correspondant à chaque caractère
        txt_ascii.append(ord(i))
    for i in range(len(txt_ascii)): ##encodage de chaque caractère selon son type
        if 97<=txt_ascii[i]<=122: ##minuscules
            txt_ascii[i]=((txt_ascii[i]+decalage)-97)%26 ##-97 pour retrouver une lettre minuscule ##%26 pour retrouver une lettre de l'alphabet
            type_caractere.append("m") ##on enregistre que c'est une minuscule
        elif 65<=txt_ascii[i]<=90: ##majuscules
            txt_ascii[i]=((txt_ascii[i]+decalage)-65)%26 ##-65 idem majuscule ##idem
            type_caractere.append("M") ##idem majuscule
        elif 48<=txt_ascii[i]<=57: ##chiffres
            txt_ascii[i]=(txt_ascii[i]+decalage)%10 ##%10 pour retrouver un chiffre
            type_caractere.append("c") ##idem chiffre
        else: ##symboles
            type_caractere.append("s") ##idem symbole
    for i in range(len(txt_ascii)): ##transformation de l'ascii crypté en texte
        if type_caractere[i]=="m": ##minuscules
            txt_final+=chr(txt_ascii[i]+97) ##+97 pour retrouver une minuscule
        elif type_caractere[i]=="M": ##majuscules
            txt_final+=chr(txt_ascii[i]+65) ##+65 idem majuscule
        elif type_caractere[i]=="c":
            txt_final+=chr(txt_ascii[i]+48)
        elif type_caractere[i]=="s": ##chiffres ou symboles
            txt_final+=chr(txt_ascii[i])
    return(txt_final)
        

z=input("Que voulez-vous faire? (encoder/décoder): ")        
a=input("Entrez le texte: ")
b=int(input("Entrez la valeur du décalage: "))
c=input("Entrez la direction (droite/gauche): ")
x=decalage(z,a,b,c)
print(x)
