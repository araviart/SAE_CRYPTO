import cv2
import textwrap
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from part1 import texte_to_binaire, crypt_sdes, decrypt_sdes, text1

def extract_key(image_path):
    """
    Extrait une clé à partir de l'image spécifiée.

    Parameters:
    - image_path (str): Le chemin vers l'image à traiter.

    Returns:
    - str: La clé extraite sous forme de chaîne binaire.
    """
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    first_row = image[0]
    key_bits = []

    for pixel_value in first_row[:64]:
        binary_pixel = format(pixel_value[0], '08b') + format(pixel_value[1], '08b') + format(pixel_value[2], '08b')

        key_bits.append(binary_pixel[-1])

    key = ''.join(key_bits)

    return key

def encrypt_aes(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = b""
    for block in split_text_into_blocks(plaintext, 16):
        ciphertext += cipher.encrypt(pad(block.encode(), AES.block_size))

    return ciphertext

def decrypt_aes(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

def split_text_into_blocks(text, block_size):
    blocks = textwrap.wrap(text, block_size)
    blocks = [block.ljust(block_size) for block in blocks]
    return blocks

aes_key = b'16bytesecretkey1'
sdes_key = 511

data = texte_to_binaire(text1)
data_sdes = texte_to_binaire(text1)

# Mesure du temps d'exécution pour AES - Cryptage
start_time = time.time()
aes_ciphertext = encrypt_aes(aes_key, data)
aes_encrypt_time = time.time() - start_time

# Mesure du temps d'exécution pour AES - Décryptage
start_time = time.time()
aes_decrypted_text = decrypt_aes(aes_key, aes_ciphertext)
aes_decrypted_text = aes_decrypted_text.decode("utf-8")
aes_decrypt_time = time.time() - start_time

# Mesure du temps d'exécution pour SDES - Cryptage
start_time = time.time()
sdes_ciphertext = crypt_sdes(data_sdes, sdes_key)
sdes_encrypt_time = time.time() - start_time

# Mesure du temps d'exécution pour SDES - Décryptage
start_time = time.time()
sdes_decrypted_text = decrypt_sdes(sdes_ciphertext, sdes_key)
sdes_decrypt_time = time.time() - start_time

# Affichage des résultats
print("Temps d'exécution pour AES - Cryptage :", aes_encrypt_time)
print("Temps d'exécution pour AES - Décryptage :", aes_decrypt_time)
print("Temps d'exécution pour SDES - Cryptage :", sdes_encrypt_time)
print("Temps d'exécution pour SDES - Décryptage :", sdes_decrypt_time)

