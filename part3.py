from scapy.all import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from constante import clef_256

seuil_longueur = 16
def bits_to_bytes(bit_string):
    return int(bit_string, 2).to_bytes(len(bit_string) // 8, byteorder='big')
key = bits_to_bytes(clef_256)

def decrypt_aes(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, IV=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

def filter_packets(packet):
    if Raw in packet:
        iv = packet[Raw].load[:16]
        ciphertext = packet[Raw].load[16:]
        try :
            decrypted_data = decrypt_aes(ciphertext, key, iv)
        except ValueError:
            decrypted_data = "Erreur"
        if decrypted_data != "Erreur":
            print(decrypted_data.decode("utf-8"))
capture = rdpcap(r"C:\Users\Eren1\Desktop\crypto\trace_sae.cap")
for packet in capture:
    filter_packets(packet)