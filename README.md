# Rapport de Projet SAE Crypto

**Membres du Projet :**
- **Noms :** Pigoreau, Raviart
- **Prénoms :** Nathan, Alexandre
- **Groupes :** 23, 22
- **Lien du projet :** [gitHub](https://github.com/araviart/SAE_CRYPTO)

---

### Contenu du Rapport :

1. **Introduction**
   - Présentation du contexte et des objectifs du projet.

2. **Partie 1: Premières tentatives**
   - Réponses aux questions concernant le protocole PlutotBonneConfidentialité, RSA, et l'algorithme SDES.

3. **Partie 2: Un peu d’aide**
   - Réponses aux questions sur l'algorithme AES, évaluation expérimentale, et autres types d'attaques.

4. **Partie 3: Analyse des messages**
   - Proposition d'un programme Python utilisant Scapy pour filtrer et déchiffrer les messages.

5. **Partie 4: Un peu de recul**
   - Réponses aux questions supplémentaires sur l'utilisation des clés, l'inspiration de PlutotBonneConfidentialité, et d'autres applications du protocole.

6. **Rendu**
   - Répartition des tâches.
   - Code source inclus dans l'archive.
   - Fichiers requis pour reproduire l'environnement virtuel.
   - Instructions d'exécution du programme.

---

### Répartition des Tâches :

- Nathan Pigoreau :
   - Partie 2 : Un peu d'aide partie python trouver clef avec image
   - Partie 3 : Analyse des messages
   - Rédaction du rapport

- Alexandre Raviart :
   - Partie 1 : Premières tentatives
   - Réponse question partie 2 : Un peu d'aide
   - Partie 4 : Un peu de recul
   - Rédaction du rapport


### Partie 1: Premières tentatives

1. **RSA Utilisé Correctement:**
   - Eve ne peut pas espérer casser RSA s'il est utilisé correctement, car RSA est actuellement difficile à casser en pratique, surtout avec de grandes clés. La sécurité de RSA repose sur la difficulté de factoriser de grands nombres premiers.

2. **SDES Peu Sécurisé:**
   - SDES est peu sécurisé car il utilise un algorithme simplifié, et une attaque par force brute serait possible avec un nombre relativement faible d'essais.

3. **Double SDES plus sûr?**
   - Double SDES n'est pas nécessairement plus sûr. Eve devrait récupérer la clé pour SDES pour chaque itération. Pour rendre cela plus astucieux, elle pourrait utiliser une attaque par cryptanalyse différentielle ou linéaire.

4. **Extension de SDES:**
   - Proposez une extension pour chiffrer des textes plus longs, en utilisant une technique de découpage du texte en blocs.

5. **Fonctions de Cassage:**
   - Implémentez les fonctions [`cassage_brutal`](https://github.com/araviart/SAE_CRYPTO/blob/e3fff55bbb6148f26ab4bd322661f0567a2fd4f1/part1.py#L111) et  [`cassage_astucieux`](https://github.com/araviart/SAE_CRYPTO/blob/e3fff55bbb6148f26ab4bd322661f0567a2fd4f1/part1.py#L129) pour tester différentes clés. Vous pouvez trouver le code source de ces fonctions dans le fichier [part1.py](part1.py) du même dossier que ce rapport.

    - Descriptif du Script `main`

        Le script `main` fourni permet des tests approfondis des fonctions de cassage implémentées dans le projet. Il utilise des options en ligne de commande pour définir le mode de test : "test" pour des tests spécifiques et "aleatoire" pour des tests aléatoires.

        - Options de Test

            - Test Spécifique (`test`)

                Le script effectue des tests sur les fonctions de cassage brutal et astucieux en utilisant un texte spécifique (`text1` dans l'exemple) chiffré avec les clés spécifiées (`key_test1` et `key_test2`). Les temps d'exécution des deux méthodes de cassage sont imprimés.

                ```bash
                python part1.py test 
                ```

            - Test Aléatoire (`aleatoire`)

                Le script propose à l'utilisateur de lancer un test aléatoire. Si l'utilisateur accepte, il génère deux clés aléatoires (`clef_aléatoire1` et `clef_aléatoire2`) et effectue des tests de cassage brutal et astucieux sur un autre texte (`text2` dans l'exemple). Les temps d'exécution des deux méthodes de cassage sont imprimés.

                ```bash
                python part1.py aleatoire
                ```

            - Exécution par Défaut

                Si aucune option n'est spécifiée en ligne de commande, le script invite l'utilisateur à choisir un mode de test ("test" ou "aleatoire") et effectue les tests en conséquence.

                ```bash
                python part1.py
                ```

## Remarque sur les Clés de Test

Les clés de test `key_test1` et `key_test2` sont initialement définies à 5 et 63 respectivement. Ces clés sont utilisées dans les tests spécifiques et peuvent être remplacées par d'autres valeurs selon les besoins du testeur.

## Remarque sur les temps d'éxecution

Les temps d'exécution des fonctions de cassage sont mesurés en utilisant la fonction [`time.time()`](https://docs.python.org/3/library/time.html#time.time) de Python.. Les temps d'exécution affichés sont en secondes.

 - Exemple de Temps d'Exécution en utilisant les clefs test1 et test2

    ```bash
    python part1.py test
    ```

    ```bash
    Temps d'exécution du cassage brutal : 0.000997304916381836
    Temps d'exécution du cassage astucieux : 0.000997304916381836
    ```

- Pour des raisons de temps il n'y aura pas de test de temps d'Exécution pour le test aléatoire. Cependant, en regardant le principes utiliser pour le cassage brutal on peut voir que le temps d'éxécution maximum sera de 1024*1024 actions soit 1048576 actions. Pour le cassage astucieux le temps d'éxécution maximum sera de 1024 + 1024 actions soit 2048 actions.

- Avec un raisonement basics pour le texte 1:
   - Le cassage brutal prend 149.9277458190918 secondes en sachant que la clef 1 est de 5 et la clef 2 est de 63. Soit 149.9277458190918 secondes pour 5 * 1024 + 63 actions soit 5183 actions donc un total de environ d'environ 35 actions par seconde, donc pour le temps maximum on aurait 1048576 * 35 soit environ 36 700 160 qui nous donne environ 611 669 minutes ou environ 10 194 heures ou environ 424 jours soit un peu plus d'un an. 

   - Pour le cassage astucieux le temps d'éxécution est de 14.942676782608032 secondes pour un total de 1024 + 63 actions soit 1087 actions donc un total de environ 72 actions par seconde , donc pour le temps maximum on aurait 2048 * 13 soit environ 147 456 secondes qui nous donne environ 2 457 minutes ou environ 41 heures.

   Ce qui nous donne une différence de temps d'éxécution maximale de 10 153 heures soit environ 423 jours soit un peu plus d'un an de différence entre le cassage brutal et le cassage astucieux.

### Partie 2: Un peu d’aide

1. **AES 256 bits:**
   - AES avec des clés de 256 bits est considéré comme très sécurisé. Il est actuellement pratiquement impossible à casser en utilisant des méthodes d'attaque connues.

2. **Évaluation expérimentale:**
   ```bash
   Temps d'exécution pour AES - Cryptage : 0.0030002593994140625
   Temps d'exécution pour AES - Décryptage : 0.007001161575317383
   Temps d'exécution pour SDES - Cryptage : 0.11375284194946289
   Temps d'exécution pour SDES - Décryptage : 0.10687613487243652
   ```
   

### Partie 3: Analyse des messages

Dans cette section, nous avons utilisé la bibliothèque Scapy pour capturer et déchiffrer des messages. Le code source est disponible dans le fichier [part3.py](part3.py) du même dossier que ce rapport.

Le processus de déchiffrement utilise une clé de 256 bits (`clef_256`) définie dans le fichier de constantes. Les messages capturés sont traités à l'aide de la bibliothèque Crypto et de l'algorithme de chiffrement AES en mode CBC.

La fonction `filter_packets` est responsable de filtrer les paquets capturés et d'extraire les données chiffrées, puis de les déchiffrer en utilisant la clé et le vecteur d'initialisation (IV). Les messages déchiffrés sont ensuite affichés en UTF-8, à moins qu'une erreur de déchiffrement ne survienne. Dans ce cas, le message est affiché en hexadécimal.

La fonction `main` est responsable de lancer la capture et d'appeler la fonction `filter_packets` pour chaque paquet capturé.

1. **Messages déchiffrés:**
   - Les messages déchiffrés sont affichés dans le terminal. Ils sont afficher dans le terminal après l'éxécution du script.

   - Voici l'affichage : 
   
      ```bash
      La crypto c'est trop bien!
      Je suis complètement d'accord!
      ```

### Partie 4: Un peu de recul

1. **Utilisation de la même clé par Alice et Bob:**
   - Ce n'est généralement pas une bonne pratique de toujours utiliser la même clé. Les clés devraient être régulièrement mises à jour pour renforcer la sécurité. En cas de compromission, une clé unique compromettrait tous les échanges passés et futurs.

2. **Protocole PlutotBonneConfidentialité inspiré d'un vrai protocole réseau:**
   - Le protocole PlutotBonneConfidentialité semble s'inspirer du protocole SSL/TLS. La partie associée à la certification des clés, qui est absente dans PlutotBonneConfidentialité, est probablement liée au processus de vérification des certificats pour assurer l'authenticité des clés publiques.

3. **Autres exemples d'utilisation utile de ce protocole:**
   - Outre l'échange de messages romantiques, ce protocole peut être utile dans des contextes tels que la transmission sécurisée de données financières, la communication entre entreprises partenaires ou toute situation nécessitant une confidentialité élevée.

4. **Applications de messagerie utilisant un chiffrement de bout en bout:**
   - Deux exemples d'applications sont WhatsApp et Signal. Ces applications utilisent des mécanismes cryptographiques robustes pour garantir que seuls les destinataires prévus peuvent déchiffrer les messages.

5. **Lois incitant à déchiffrer les communications:**
   - Les arguments en faveur de ces lois soulignent souvent la nécessité de prévenir la criminalité en ligne, le terrorisme ou d'autres activités illicites. Cependant, ces lois suscitent des préoccupations majeures en matière de vie privée, car elles pourraient permettre un accès excessif aux communications personnelles sans surveillance adéquate. Les opposants soulignent également que ces lois pourraient créer des vulnérabilités exploitables par des acteurs malveillants.

## Requirements

Pour reproduire l'environnement virtuel utilisé dans ce projet, veuillez installer les dépendances répertoriées dans le fichier [requirements.txt](requirements.txt). Utilisez la commande suivante dans votre terminal pour installer les dépendances :

```bash
pip install -r requirements.txt
