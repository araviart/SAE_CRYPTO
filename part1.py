import random
import sys
import time
from sdes import encrypt, decrypt
from constante import key_test1, key_test2, text1, text2


def texte_to_binaire(texte):
    """Converts a text to binary representation.

    Args:
        texte (str): Text to convert.

    Returns:
        str: Binary representation of the input text.
    """
    binaire = ""
    for lettre in texte:
        binaire += format(ord(lettre), "08b")
    return binaire

def binaire_to_texte(binaire):
    """Converts a binary text to plain text.

    Args:
        binaire (str): Binary text to convert (8 bits per character).

    Returns:
        str: Converted plain text.
    """
    texte = ""
    for i in range(0, len(binaire), 8):
        texte += chr(int(binaire[i:i+8], 2))
    return texte

def decouper_en_blocs(text, n):
    """Splits a string into blocks of n characters.

    Args:
        text (str): String to split.
        n (int): Number of characters per block.

    Returns:
        list: List of character blocks.
    """
    return [text[i:i+n] for i in range(0, len(text), n)]

def crypt_sdes(texte_clair, key):
    """Encrypts a text using the SDES method.

    Args:
        texte_clair (str): Text to encrypt.
        key (int): Encryption key.

    Returns:
        str: Encrypted text.
    """
    texte_b = texte_to_binaire(texte_clair)
    liste_b = decouper_en_blocs(texte_b, 8)
    message_crypted = ""
    for bloc_clair in liste_b:
        message_crypted += format(encrypt(key, int(bloc_clair, 2)), "08b")
    return message_crypted

def crypt_double_sdes(texte_clair, key, key_test2):
    """Encrypts a text using the Double SDES method.

    Args:
        texte_clair (str): Text to encrypt.
        key (int): 1st encryption key.
        key_test2 (int): 2nd encryption key.

    Returns:
        str: Encrypted text.
    """
    crypt1 = crypt_sdes(texte_clair, key)
    crypt2 = crypt_sdes(binaire_to_texte(crypt1), key_test2)
    return crypt2

def decrypt_sdes(texte_crypted, key):
    """Decrypts an encrypted text using the SDES method.

    Args:
        texte_crypted (str): Encrypted text to decrypt.
        key (int): Decryption key.

    Returns:
        str: Decrypted text.
    """
    liste_b = decouper_en_blocs(texte_crypted, 8)
    message_decrypted = ""
    for bloc_crypted in liste_b:
        message_decrypted += format(decrypt(key, int(bloc_crypted, 2)), "08b")
    return binaire_to_texte(message_decrypted)

def decrypt_double_sdes(texte_crypted, key, key_test2):
    """Decrypts an encrypted text using the Double SDES method.

    Args:
        texte_crypted (str): Encrypted text to decrypt.
        key (int): 1st decryption key.
        key_test2 (int): 2nd decryption key.

    Returns:
        str: Decrypted text.
    """
    decrypt1 = decrypt_sdes(texte_crypted, key_test2)
    decrypt2 = decrypt_sdes(texte_to_binaire(decrypt1), key)
    return decrypt2

def brute_force_double_sdes(message_clair, message_chiffre):
    """Brute-force attack on the Double SDES method.

    Args:
        message_clair (str): Original text for verification.
        message_chiffre (str): Encrypted text to decrypt.

    Returns:
        tuple: (success flag, decryption key, computation time)
    """
    debut = time.time()
    for i in range(1024):
        for j in range(1024):
            decry = decrypt_double_sdes(message_chiffre, i, j)
            if decry == message_clair:
                return True, j, time.time() - debut
    return False, None, None

def cassage_astucieux(message_clair, message_chiffre):
    """Smart attack on the Double SDES method.

    Args:
        message_clair (str): Original text for verification.
        message_chiffre (str): Encrypted text to decrypt.

    Returns:
        tuple: (decryption key, computation time)
    """
    dict_partiel = {}
    debut = time.time()

    # Generating keys
    for i in range(1024):
        message = crypt_sdes(message_clair, i)
        dict_partiel[i] = message

    for j in range(1024):
        message = texte_to_binaire(decrypt_sdes(message_chiffre, j))
        if message in dict_partiel.values():
            for key, value in dict_partiel.items():
                if value == message:
                    return key, j, time.time() - debut
    return None, None, time.time() - debut

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        *_, temps = brute_force_double_sdes(text1, crypt_double_sdes(text1, key_test1, key_test2))
        print(" Text 1 temps de cassage brutal :", temps)
        *_, temps = cassage_astucieux(text1, crypt_double_sdes(text1, key_test1, key_test2))
        print("Text 2 temps de cassage astucieux :", temps)
    elif len(sys.argv) > 1 and sys.argv[1] == "aleatoire":
        rep = input("Attention vous avez lancé un test aléatoire, les résultats peuvent être long à obtenir, voulez vous continuer ? (y/n)" + "\n")
        if rep == "y":
            clef_aléatoire1 =  random.randint(2**(10-1),2**10-1)
            clef_aléatoire2 = random.randint(2**(10-1),2**10-1)
            *_, temps = brute_force_double_sdes(text2, crypt_double_sdes(text2, clef_aléatoire1, clef_aléatoire2))
        else:
            sys.exit()
        print(" Text 2 temps de cassage brutal :", temps)
        *_, temps = cassage_astucieux(text2, crypt_double_sdes(text2, clef_aléatoire1, clef_aléatoire2))
        print("Text 2 temps de cassage astucieux :", temps)
    else:
        input = input("Veuillez choisir un mode de test : test ou aleatoire" + "\n")
        if input == "test":
            *_, temps = brute_force_double_sdes(text1, crypt_double_sdes(text1, key_test1, key_test2))
            print(" Text 1 temps de cassage brutal :", temps)
            *_, temps = cassage_astucieux(text1, crypt_double_sdes(text1, key_test1, key_test2))
            print("Text 2 temps de cassage astucieux :", temps)
        elif input == "aleatoire":
            print("Attention vous avez lancé un test aléatoire, les résultats peuvent être long à obtenir")
            clef_aléatoire1 =  random.randint(2**(10-1),2**10-1)
            clef_aléatoire2 = random.randint(2**(10-1),2**10-1)
            *_, temps = brute_force_double_sdes(text2, crypt_double_sdes(text2, clef_aléatoire1, clef_aléatoire2))
            print(" Text 2 temps de cassage brutal :", temps)
            *_, temps = cassage_astucieux(text2, crypt_double_sdes(text2, clef_aléatoire1, clef_aléatoire2))
            print("Text 2 temps de cassage astucieux :", temps)
        else:
            print("Mauvaise entrée")