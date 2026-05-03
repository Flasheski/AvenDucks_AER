# 🦆 Projet d'Activité JPO : Epiduck

## 🎯 Contexte et Objectifs
Cette activité a été conçue dans le cadre du test pour devenir AER.
L'objectif est d'animer un atelier de 2 heures lors d'une JPO (Journée Portes Ouvertes), destiné à un public large (des collégiens aux parents), pour les sensibiliser à la programmation de manière ludique et visuelle.

## 🎮 Concept du Jeu : "AvenDuck"
Le projet est un jeu vidéo en 2D développé en Python avec la bibliothèque **Pygame**. 
Le joueur incarne un canard (aux couleurs d'Epitech) qui doit affronter différents boss pour récupérer des pierres spéciales.

**Fonctionnalités principales :**
* **Menu principal :** Jouer, Quitter.
* **Contrôles simples :** `Q` et `D` pour se déplacer (gauche/droite), `E` pour attaquer.
* **Équipement :** Le joueur commence sans arme et doit ramasser une épée ou d'autres armes (comme un pistolet à eau ou un bazooka) sur le sol pour pouvoir attaquer.
* **Progression :** Plusieurs niveaux de difficulté (de Easy à Difficile), avec des boss (ex: `BossEasy`) aux mécaniques adaptées.

## 🧠 Approche Pédagogique : Le Projet "à trous"
Pour s'assurer que l'activité rentre dans le format de 2h tout en offrant un sentiment d'accomplissement immédiat, l'atelier repose sur un projet pré-structuré.

1.  **Squelette fourni :** L'architecture du jeu (classes, boucle principale, chargement des assets visuels) est déjà en place pour éviter de perdre les participants sur des détails techniques complexes.
2.  **Remplissage progressif :** Les participants doivent compléter des blocs de code spécifiques (les "trous") pour faire fonctionner ou débloquer des mécaniques du jeu.
3.  **Gamification de l'apprentissage :** Chaque niveau de difficulté dans le code permet de débloquer le niveau correspondant dans le jeu. Plus ils codent, plus ils avancent dans leur partie ! Cela permet parfaitement de s'adapter aux différents niveaux de chacun assurant la satisfaction de chacun selon leurs compétences techniques.

### Exemples d'étapes de code pour les participants (selon le niveau) :
* **Étape 1** (Niveau 1 - Les Bases) : Apprendre à se repérer sur un plan cartésien (coordonnées X/Y). Les participants remplissent les variables pour définir la taille de la fenêtre de jeu, faire avancer/reculer le canard, et coder la détection de collision pour ramasser la première arme.

* **Étape 2** (Niveau 2 - Physique et Interface Utilisateur) : Introduire la notion d'accélération et la manipulation d'interface graphique. Ils complètent le code simulant la gravité lors d'un saut, lient la variable des points de vie (PV) à l'affichage dynamique d'une barre de vie à l'écran, et gèrent la direction des tirs.

* **Étape 3** (Niveau 3 - Logique algorithmique) : Maîtriser les conditions et les événements clavier. Le grand final consiste à "écouter" les touches du joueur pour déclencher de nouvelles actions, et à utiliser des conditions (if) pour créer l'armure du boss final (un tir normal est inefficace, le joueur doit coder une condition pour infliger 100 points de dégâts avec une attaque spéciale !).

## 🛠️ Déploiement et Prérequis
* **Technologie :** Python et la bibliothèque `pygame`.
* **Simplicité :** Des simples dossiers contenant les scripts `.py` et le dossier `assets/` (images PNG). 
* **Avantage JPO :** Totalement gratuit, aucune licence requise. Fonctionne sur n'importe quel poste équipé de Python, avec une commande rapide `pip install pygame`.
