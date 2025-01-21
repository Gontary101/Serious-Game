# ECO-FACTORY CHALLENGE Companion App

Bienvenue dans l’application de bureau **ECO-FACTORY CHALLENGE Companion App**, développée en Python (Tkinter). Cette application s'inscrit comme un outil complet pour gérer vos joueurs, terrains, usines, ressources, travailleurs, technologies, pollution et coûts, tout en fournissant une vue d'historique des actions et résultats de chaque round. Avec cette version, vous accédez à de nouvelles fonctionnalités, notamment :

- **Historique des Actions** : Un onglet *History* récapitule les décisions de chaque joueur à chaque round.
- **Gestion Avancée des Tours** : Calculez vos revenus, dépenses, pollution et bien plus encore grâce à un bouton de calcul de round, jusqu'à 6 rounds (ou jusqu'à ce qu'un joueur atteigne 3000 EC).
- **Transport Personnalisé** : Choisissez entre des routes de transport électrique ou à carburant fossile (chacun ayant un coût et une pollution distincts).
- **Gestion des Travailleurs** : Embauchez et assignez des ingénieurs, techniciens, conseillers environnementaux, ou travailleurs universels. Chaque rôle a un salaire et des avantages uniques.
- **Système de Ressources et Commerce** : Générez des ressources, utilisez-les pour alimenter vos usines, et faites des échanges ou des ventes auprès de la banque à des tarifs variés.
- **Achat et Vente de Technologies** : Investissez dans différentes technologies pour optimiser vos usines, réduire votre pollution ou améliorer vos bénéfices, avec la possibilité de revendre la technologie pour un remboursement partiel.
- **Conditions de Fin de Partie** : La partie peut se terminer dès qu’un joueur atteint 3000 EC ou qu’on dépasse le nombre maximal de rounds (6). Un calcul final détermine le gagnant en fonction de ses points de pollution.

---

## Table des Matières
1. [Description](#description)  
2. [Prérequis](#prérequis)  
3. [Installation](#installation)  
4. [Utilisation](#utilisation)  
5. [Fonctionnalités Clés](#fonctionnalités-clés)  
   - [Dashboard](#dashboard)  
   - [Terrain](#terrain)  
   - [Factories](#factories)  
   - [Technologies](#technologies)  
   - [Workers](#workers)  
   - [Resources](#resources)  
   - [Pollution & Costs](#pollution--costs)  
   - [History](#history)  
6. [Contribution](#contribution)  
7. [Licence](#licence)  
8. [Remerciements](#remerciements)  

---

## Description
**ECO-FACTORY CHALLENGE Companion App** est un utilitaire essentiel pour tous les joueurs du jeu de plateau/d’entreprise écoresponsable **ECO-FACTORY CHALLENGE**. Elle vous offre :

- Une **interface complète** pour gérer **jusqu’à 4 joueurs** (avec ajout dynamique).
- L’**achat et la gestion** de terrains, y compris leur coût, leurs ressources et leur propriétaire.
- La **création, la suppression et la gestion** d’usines en tenant compte de leurs coûts, besoins en ressources, terrains autorisés et pollution produite.
- Un **système avancé** de **transport** (électrique vs fossile) avec des coûts et des pollutions variables, modulés par certaines **technologies**.
- La **gestion des travailleurs** (ingénieurs, techniciens, conseillers environnementaux, travailleurs universels), leur salaire et leur assignation aux usines appropriées.
- La **production, consommation** et **échange** de ressources (vente à la banque ou troc entre joueurs si vous le souhaitez).
- Un **onglet pollution et coûts** pour calculer précisément vos dépenses (maintenance, salaires, taxe carbone, transport) et vos revenus à chaque tour.
- Un **système d’historique** (nouvel onglet *History*) qui récapitule les actions de chaque joueur sous forme de tableau, à chaque round.
- Une **simulation en tours** : appuyez sur **Calculate Round** pour mettre à jour l’état de la partie (revenus, dépenses, pollution, etc.). La partie se termine automatiquement si un joueur atteint 3000 EC ou si on dépasse le nombre maximal de rounds.

---

## Prérequis
- **Python 3.x** : Téléchargement depuis [python.org](https://www.python.org/downloads/).  
- **Tkinter** : Habituellement inclus avec Python. Si ce n’est pas le cas, installez-le selon votre OS :
  - **Windows/macOS** : Normalement déjà inclus.
  - **Linux (Debian/Ubuntu)** : `sudo apt-get install python3-tk`.

---

## Installation

1. **Récupérez le Code Source**  
   - Téléchargez (ou clonez) le fichier `eco_factory_challenge.py` depuis le dépôt ou la source.

2. **Vérifiez votre version de Python**  
   Dans un terminal ou invite de commande, exécutez :
   ```bash
   python --version
   ```
   ou
   ```bash
   python3 --version
   ```

3. **Installez Tkinter si nécessaire**  
   Sous Linux/Debian/Ubuntu :
   ```bash
   sudo apt-get install python3-tk
   ```

4. **Lancez l’Application**  
   Dans le dossier contenant `eco_factory_challenge.py`, exécutez :
   ```bash
   python eco_factory_challenge.py
   ```
   ou
   ```bash
   python3 eco_factory_challenge.py
   ```
   L’interface graphique devrait s’ouvrir dans une fenêtre de 1600×900.

---

## Utilisation

### 1. Création et Sélection d’un Joueur
- Dans la zone supérieure, cliquez sur **Add Player** pour ajouter un joueur (jusqu’à 4 maximum).  
- Donnez-lui un nom puis sélectionnez-le dans la liste déroulante.  

### 2. Navigation par Onglets
- **Dashboard** : Vue globale de vos Eco-Credits, Pollution Points et Carbon Credits.  
- **Terrain** : Liste des terrains disponibles à l’achat, leurs ressources et leur propriétaire.  
- **Factories** : Liste/gestion des usines (construction, retrait).  
- **Technologies** : Achat de technologies, suppression avec remboursement partiel.  
- **Workers** : Embauche, assignation et retrait des travailleurs.  
- **Resources** : Inventaire des ressources, production, consommation et commerce (vente ou échange).  
- **Pollution & Costs** : Calcul des coûts (salaires, maintenance, transport), de la pollution et de la taxe carbone.  
- **History** : Historique des actions, par joueur et par round, avec un affichage en mode tableau.  

### 3. Déroulement d’un Round
1. **Effectuez vos actions** : Achetez des terrains, embauchez des travailleurs, construisez des usines, acquérez des technologies, etc.  
2. **Cliquez sur "Calculate Round"** (onglet *Pollution & Costs*) : L’application calcule les revenus, dépenses, pollution, et applique les changements (achat de ressources, vente, etc.).  
3. **Vérification de fin de partie** :  
   - Si un joueur atteint **3000 EC**, la partie s’arrête immédiatement et détermine le vainqueur.  
   - Si vous dépassez **6 rounds**, la partie s’arrête également et calcule un score final basé sur l’EC et la pollution.  

4. **Consultez l’onglet "History"** pour un récapitulatif détaillé des actions de chaque joueur à ce round.  

---

## Fonctionnalités Clés

### Dashboard
Affiche les informations majeures concernant le joueur sélectionné :
- **Eco-Credits (EC)** : Votre argent disponible.
- **Pollution Points (PP)** : Votre pollution cumulée.
- **Carbon Credits** : Pour compenser vos émissions, selon les règles du jeu.

### Terrain
- **Liste des Terrains** : Chaque tuile affiche son type, son coût, ses ressources, son potentiel de compensation carbone (offset) et le nom du propriétaire.
- **Achat de Terrain** : Si vous avez suffisamment d’EC, vous pouvez acquérir un terrain qui n’est pas encore possédé.  
- **Ressources Disponibles** : Les ressources peuvent être exploitées par la construction d’usines autorisées sur le terrain.

### Factories
- **Construction d’Usine** : Sélectionnez le type d’usine (exemple : "Timber Logging Camp", "Crop Farm", etc.), puis choisissez un terrain vous appartenant et compatible.  
- **Coûts et Pollution** : Chaque usine a un coût de construction, un coût opérationnel, une pollution générée, et peut nécessiter certaines ressources pour fonctionner.  
- **Transport** : Gérez le type de transport (électrique ou fossile) pour l’acheminement des ressources, affectant coûts et pollution.  
- **Assignation de Travailleurs** : Pour un fonctionnement optimal, certaines usines exigent un certain nombre de travailleurs d’un rôle précis.  
- **EC Output** : Nombre d’EC générés directement chaque round (en plus d’autres bénéfices potentiels).

### Technologies
- **Achat de Technologies** : Investissez dans des améliorations (ex: réduction de pollution, optimisation de production, rabais de transport).  
- **Coûts et Maintenance** : Chaque technologie a un coût d’achat et un entretien (maintenance) qui vous est facturé à chaque round.  
- **Prérequis** : Certaines technologies exigent un certain rôle de travailleur (ex: *Engineer*, *Technician*, etc.) ou une autre technologie déjà acquise.  
- **Remboursement Partiel** : Vous pouvez revendre une technologie pour récupérer la moitié de son coût initial.

### Workers
- **Rôles** : *Engineer*, *Technician*, *Environmental Advisor*, *Universal Worker*.  
- **Salaire et Bénéfices** : Chaque rôle a un salaire (prélevé à chaque round) et offre des avantages particuliers (réduction de pollution, boost de production, etc.).  
- **Embauche** : Vérifiez que vous avez suffisamment d’EC pour payer le salaire du premier round.  
- **Assignation** : Les usines peuvent exiger ou bénéficier de certains rôles. Assignez-les pour maximiser votre efficacité.

### Resources
- **Inventaire** : Consultez la quantité de chaque ressource disponible pour le joueur sélectionné.  
- **Production / Consommation** : Les usines produisent et consomment des ressources (ou les vendent).  
- **Commerce** : Achetez des ressources manquantes à la banque (à prix majoré) ou vendez votre surplus pour obtenir des EC. Effectuez aussi des échanges entre joueurs si désiré.

### Pollution & Costs
- **Pollution Totale (PP)** : Cumul de la pollution générée par vos usines et votre transport.  
- **Taxe Carbone** : 5 EC par point de pollution, prélevés à chaque round.  
- **Salaires, Maintenance et Transport** : Coûts liés aux travailleurs, aux technologies, et au transport.  
- **Calculate Round** : Lance le calcul des revenus (production, ventes, etc.) et des dépenses, modifie vos EC et PP, et vérifie les conditions de fin de partie.

### History
- **Tableau des Actions** : Chaque round, chaque joueur voit un résumé de ses décisions (achat de terrains, constructions, embauches, ventes, etc.) et son résultat économique (net gain/perte, pollution).  
- **Multilignes** : Les actions et les données économiques sont affichées dans un tableau ajusté, permettant une vue condensée de chaque round.  
- **Conservation des Logs** : L’historique vous aide à retracer les stratégies et changements au fil de la partie.

---

## Contribution
Nous accueillons toute proposition d’amélioration ou de correction. Pour contribuer :

1. **Fork** le dépôt.
2. Créez une nouvelle branche pour votre fonctionnalité  
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Faites vos modifications et **commit**-ez  
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push** la branche  
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Ouvrez une **Pull Request** pour examen.

---

## Licence
Ce projet est sous licence MIT. Consultez le fichier [LICENSE](./LICENSE) pour plus de détails.

---

## Remerciements
Un grand merci à la communauté Open Source pour la mise à disposition d’outils et d’exemples de projets. Merci également à tous les testeurs qui ont contribué en fournissant des retours et des suggestions pour faire évoluer cette application.

---

Bon jeu et restez éco-responsables !
```
