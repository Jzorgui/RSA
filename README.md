# RSA

Toutes les fonctions sont contenues dans le fichier fonctions.py, le fichier main.py sert juste à les appeler afin de crypter/décrypter et cracker un message texte.

### Remarques
  - Il est demandé de choisir deux nombres premiers (p et q) tel que n (=p*q) soit supérieur à 255 afin de pouvoir crypter/décrypter chaque caractère du message selon son code Unicode. En effet, comme cela les fonctions prennent en compte la plupart des caractères alpha-numériques Latin.
  - Pour vérifier si un nombre est premier je teste chaque entier entre 2 et sa racine. Si il n'a aucun diviseur alors il est premier.
