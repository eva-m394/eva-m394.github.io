###########
###TESTS###
###########

from PROJET_complet import vigenere,cesar,morse_encodage,morse_decodage


###Vigenère###

if vigenere("encoder","Hello World !","clef")=="Jppqq Attwh !":
    print("Test encodage Vigenère OK")
else:
    print("Test encodage Vigenère pas OK")

if vigenere("décoder","Jppqq Attwh !","clef")=="Hello World !":
    print("Test décodage Vigenère OK")
else:
    print("Test décodage Vigenère pas OK :", vigenere("décoder","Jppqq Attwh !","clef"))


###César###
if cesar("encoder","Hello World !",147,"droite")=="Yvccf Nficu !":
    print("Test encodage César OK")
else:
    print("Test encodage César pas OK", cesar("encoder","Hello World !",147,"droite"))

if cesar("décoder","Yvccf Nficu !",147,"droite")=="Hello World !":
    print("Test décodage César OK")
else:
    print("Test décodage César pas OK :", cesar("décoder","Yvccf Nficu !",147,"droite"))

    
###Morse###
caracteres_morse= { "A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.", "0":"-----", ".":".-.-.-", "?":"..--..", "-":"-....-", "'":".----.", " ":" ", ",":"--..--"} 
if morse_encodage("Hello World")==".... . .-.. .-.. ---  .-- --- .-. .-.. -.. ":
    print("Test encodage Morse OK")
else:
    print("Test encodage Morse pas OK :", morse_encodage("Hello World"))

if morse_decodage(".... . .-.. .-.. ---  .-- --- .-. .-.. -.. ")=="HELLO WORLD ":
    print("Test décodage Morse OK")
else:
    print("Test décodage Morse pas OK :", morse_decodage(".... . .-.. .-.. ---  .-- --- .-. .-.. -.. "))
    
