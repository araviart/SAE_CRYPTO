import cv2

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
