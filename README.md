# Amazon Search Results Scraper

Ce programme est conçu pour vous aider à obtenir les résultats d'une recherche sur Amazon, y compris le nom des articles, leur prix, leur note et leur lien pour y accéder directement.

## Prérequis

Avant de pouvoir utiliser ce programme, vous devez vous assurer que vous avez les éléments suivants :

- Python 3 installé sur votre ordinateur
- Les bibliothèques Python suivantes installées :
    - Clouscraper
    - BeautifulSoup4
    - Pandas

## Installation

Pour installer les bibliothèques Python requises, vous pouvez utiliser le gestionnaire de paquets pip. Ouvrez votre terminal et entrez les commandes suivantes :

```bash
pip install cloudscraper
pip install beautifulsoup4
pip install pandas
```

Une fois les bibliothèques installées, vous pouvez télécharger le dossier ZIP ou cloner le projet sur votre ordinateur en utilisant la commande suivante :

```bash
git clone https://github.com/L0rest/AmazonArticlesScraper.git
```

## Utilisation

Pour utiliser le programme, vous devez exécuter le fichier `amazonScrap.py` directement sur votre IDE ou à partir de votre terminal en suivant la commande suivante :

```bash
python amazonScrap.py
```

Vous serez invité à entrer le terme de recherche que vous souhaitez scraper, ainsi que le nombre de pages Amazon voulues. Une fois que vous avez entré votre terme de recherche, le programme commencera à collecter les informations sur les produits correspondants sur Amazon.

Les informations collectées seront stockées dans un fichier CSV nommé `AmazonArticles.csv`. Vous pouvez ouvrir ce fichier avec Microsoft Excel ou tout autre logiciel compatible avec les fichiers CSV.

## Contact

Si vous avez des questions, des suggestions d'amélioration ou des commentaires sur ce programme, n'hésitez pas à me contacter à l'adresse e-mail suivante : lorest.git@gmail.com

## Licence

Ce programme est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le distribuer. Veuillez consulter le fichier LICENCE pour plus d'informations.
