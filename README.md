# Amazon Search Results Scraper (FR)

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


#
#
# Amazon Search Results Scraper (EN)

This program is designed to help you obtain the search results from Amazon, including the name of the items, their price, rating, and link to access them directly.

## Requirements

Before you can use this program, you need to ensure that you have the following:

- Python 3 installed on your computer
- The following Python libraries installed:
    - Clouscraper
    - BeautifulSoup4
    - Pandas

## Installation

To install the required Python libraries, you can use the pip package manager. Open your terminal and enter the following commands:

```bash
pip install cloudscraper
pip install beautifulsoup4
pip install pandas
```

Once the libraries are installed, you can download the ZIP folder or clone the project to your computer using the following command:

```bash
git clone https://github.com/L0rest/AmazonArticlesScraper.git
```

## Usage

To use the program, you need to execute the amazonScrap.py file directly on your IDE or from your terminal using the following command:

```bash
python amazonScrap.py
```

You will be prompted to enter the search term you want to scrape, as well as the number of Amazon pages desired. Once you have entered your search term, the program will begin collecting information on the corresponding products on Amazon.

The collected information will be stored in a CSV file named AmazonArticles.csv. You can open this file with Microsoft Excel or any other software that is compatible with CSV files.

## Contact

If you have any questions, suggestions for improvement, or comments about this program, please feel free to contact me at the following email address: lorest.git@gmail.com