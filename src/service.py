# Lors de cette étape, vous allez créer une API de prédiction qui permettra de prédire la chance d'admission d'un étudiant dans une université.

# Pour cela, créez un script Python service.py dans le dossier src qui permet de charger le modèle sauvegardé, de créer une API de prédiction sécurisée et de la lancer en passant par le service de BentoML.

# L'API doit être accessible via une requête HTTP POST sur un port de votre machine. Elle doit prendre en entrée toutes les variables nécessaires à la prédiction et renvoyer la prédiction de la chance d'admission pour un étudiant.

# Concernant les endpoints, vous devrez obligatoirement créer un endpoint nommé login pour sécuriser l'accès à l'API (vous êtes libres de choisir la méthode de sécurisation que vous voulez) et un endpoint nommé predict pour effectuer les prédictions, mais vous n'êtes pas limité à un seul endpoint si vous voulez ajouter d'autres fonctionnalités interessantes à votre API.

# N'oubliez pas de tester votre API en faisant de l'inférence sur des données de test que vous choisirez.