def file_to_str(file_name, encoding="utf-8"):
    """Retourne le contenu d'un fichier sous forme de string"""
    with open(file_name, "r", encoding=encoding) as file:
        return file.read()

    
def str_to_file(string, file_name):
    """Ecrit le contenu d'un string dans un fichier"""
    with open(file_name, "w") as file:
        file.write(string)

file_name = "C:/Users/Eren1/Desktop/crypto/arsene_lupin_extrait.txt"
file_name2 = "C:/Users/Eren1/Desktop/crypto/lettres_persanes.txt"

text1 = file_to_str(file_name)
text2 = file_to_str(file_name2)

key_test1 = 0
key_test2 = 63