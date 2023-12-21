# Rapport de Projet SAE Crypto

**Membres du Projet :**
- **Noms :** Pigoreau, Raviart
- **Prénoms :** Nathan, Alexandre
- **Groupes :** 23, 22

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

- Alexandre Raviart :


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