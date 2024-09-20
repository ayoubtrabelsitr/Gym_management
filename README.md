# BrothersGym

## Description

BrothersGym est une application de gestion d'une salle de sport qui permet aux administrateurs de gérer les membres, y compris l'ajout, la modification leurs informations ou supprimer des membres. L'application utilise une interface graphique créée avec Tkinter et se connecte à une base de données MySQL pour stocker les données des utilisateurs.

## Fonctionnalités

- **Connexion Administrateur** : Authentification pour accéder à l'application.
- **Gestion des Membres** :
  - **Ajouter un membre** : Formulaire pour saisir les informations d'un nouveau membre.
  - **Modifier un membre** : Mise à jour des informations d'un membre existant.
  - **Supprimer un membre** : Suppression d'un membre de la base de données.
  - **Consulter la liste des membres** : Affichage des informations de tous les membres.

## Structure des Fichiers

- **main.py** : Point d'entrée de l'application, gère la connexion des administrateurs.
- **application.py** : Contient les fonctions pour gérer les utilisateurs (ajouter, modifier, supprimer, consulter).
- **Data.py** : Contient les fonctions de connexion à la base de données et les opérations SQL pour les utilisateurs.
- **Admin.py** : Définit la classe Admin pour gérer les informations des administrateurs.

## Installation


1. Clonez le dépôt :
   ```bash
   git clone https://github.com/ayoubtrabelsitr/Gym_management.git

2. Installez les dépendances nécessaires :
   ```bash
   pip install mysql-connector-python
3. Configurez la base de données MySQL avec les tables appropriées.

## Utilisation

 
1. Lancez l'application :
   ```bash
   python main.py
2. Connectez-vous avec vos identifiants d'administrateur.
3. Utilisez le menu pour gérer les membres.

## Captures
**Page de connexion**

<img src="img/img (1).jpg" width="400"/>
<img src="img/img (2).jpg" width="400"/>

**Page d'accueil**

<img src=".img/img (3).jpg" width="400"/>

**Liste des membres**

<img src=".img/img (4).jpg" width="400"/>

**Supprimer des membres**

<img src=".img/img (5).jpg" width="400"/>

**Ajouter des membres**

<img src=".img/img (6).jpg" width="400"/>

**Modifier des membres**

<img src=".img/im (7).jpg" width="400"/>
