# 🦆 AvenDuck - Atelier JPO Epitech 🎮

Bienvenue sur le dépôt d'**AvenDuck** (ou Epiduck pour les intimes) ! 

Ce projet a été conçu spécialement pour animer un atelier de 2 heures lors des Journées Portes Ouvertes (JPO). Son but ? Initier un public novice (collégiens, lycéens, parents) à la programmation en Python avec la bibliothèque **Pygame**, le tout de manière ludique et interactive.

Le principe est simple : le code source est déjà pré-structuré, mais il manque des morceaux clés (des "trous"). Les participants doivent compléter ces trous étape par étape pour faire fonctionner le jeu, débloquer des niveaux et finalement vaincre le boss ultime ! 🚀

---

## 🧠 Concept Pédagogique : Le code "à trous"

L'atelier est découpé en 3 niveaux de difficulté croissante, permettant aux participants d'assimiler les bases de la logique algorithmique sans être noyés sous la syntaxe :

*   🟢 **NIVEAU 1 (EASY) - Initialisation du Monde :** Comprendre les repères spatiaux (X, Y) d'un écran. On charge les images, on ajuste la taille de la fenêtre et on affiche le héros.
*   🟡 **NIVEAU 2 (MEDIUM) - La Physique et la Survie :** Introduction à la gravité, aux accélérations et aux interfaces graphiques. On gère le saut du canard, la direction des tirs et on affiche la barre de vie du Boss.
*   🔴 **NIVEAU 3 (HARD) - Contrôles avancés et Armure Lourde :** Maîtrise des conditions (`if/else`) et des événements clavier. On configure les touches d'attaque et on perce l'armure du boss final avec une arme spéciale !

---

## 🕹️ Comment jouer ?

Une fois le code complété, le joueur incarne notre courageux canard Epitech. Voici les contrôles :

*   **Q / D** : Se déplacer vers la gauche ou la droite.
*   **Espace** : Sauter (pour esquiver les attaques ennemies !).
*   **E** : Attaque basique (Tir classique / Épée).
*   **F** : Attaque spéciale (L'artillerie lourde, indispensable au niveau 3 !).

---

## 🛠️ Installation et Prérequis

Le projet est pensé pour être extrêmement simple à déployer sur les machines de l'école.

**Prérequis :**
*   Avoir [Python 3.x](https://www.python.org/downloads/) installé sur la machine.
*   Avoir la bibliothèque Pygame installée.

**Installation :**

1. Clonez ce dépôt ou téléchargez-le sous forme d'archive `.zip`.
2. Ouvrez un terminal et installez Pygame si ce n'est pas déjà fait :
   ```bash
   pip install pygame
