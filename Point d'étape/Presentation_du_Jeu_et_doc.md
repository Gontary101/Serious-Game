As of Jan 25. 2025
# DÉFI ÉCO-USINE (CONCEPTION & APPLICATION COMPANION)

## 1. VUE D'ENSEMBLE & PRINCIPALES AMÉLIORATIONS

**Objectif Général**\
Construire le réseau industriel le plus performant économiquement tout en demeurant durable. Chaque joueur s’efforce d’obtenir le meilleur *Ratio Capital-Pollution* (EC ÷ (1+PP)) à la fin de la partie.

### Compléments grâce à l’Application Companion

Afin de faciliter la gestion des joueurs, de leurs ressources, terrains, usines, technologies, travailleurs et pollution, une **application de bureau** (en Python + Tkinter) a été créée. Cette application permet de :

- Suivre l’argent (EC) et la pollution (PP) de chaque joueur.
- Gérer l’achat de terrains (tuiles) et la construction d’usines.
- Calculer automatiquement les coûts d’exploitation, la pollution et le transport des ressources.
- Engager, assigner et licencier des travailleurs.
- Acheter et supprimer des technologies, chacune ayant un coût et un effet spécifiques.
- Conclure la partie dès que les conditions de victoire (nombre de tours ou seuil de 3000 EC) sont atteintes.

## 2. OBJECTIFS, PUBLIC & TYPE DE JEU

### Objectifs

- **Transmettre un savoir** : Sensibiliser à la gestion de ressources et à l’équilibre entre rentabilité et impact environnemental.
- **Sensibilisation grand public** : Montrer comment des décisions industrielles (type de transport, choix des ressources, etc.) impactent la pollution et l’économie.
- **Enseignement & formation** : Peut être utilisé en milieu scolaire ou pour des formations, par exemple sur l’économie circulaire, la RSE ou l’aménagement du territoire.

### Public Ciblé

- **Joueuses/Joueurs cibles** :

  - Chercheur·euses
  - Enseignant·es
  - Étudiant·es
  - Professionnel·les et monde associatif

- **Animateur·ices cibles** (pour animer des sessions) :

  - Chercheur·euses
  - Enseignant·es
  - Étudiant·es
  - Professionnel·les et monde associatif

### Type de Jeu (Classification ESAR)

- **Exercice / Stratégie** : Calculs, budget, distances à gérer.
- **Symbolique** : Représentation concrète de l’industrie, du transport, de la pollution et de l'écologie.
- **Assemblage** : Placement de tuiles, construction d’usines.
- **Règles** : Jeu de gestion/plateau avec un cadre de règles détaillé (transport, coûts, ressources, etc.).

### Durée

- En l’état : 60–90 minutes environ.

### Accessibilité

- **Imprimable** (prototype physique possible).
- **Gratuit** (application companion).
- **Téléchargement** : L’application Python est mise à disposition via GitHub.

### Stade d’Avancement

- **Version jouable finalisée (avec suivi)** dans l’application companion.
- **Possibilité d’évoluer** avec un mode multijoueur en ligne et d’autres extensions.

---

## 3. COMPOSANTS & ÉLÉMENTS CLÉS DU JEU

### 3.1 Plateau & Terrain

- **Plateau 4×5** : 20 tuiles de terrain, chacune avec un coût, des ressources (ex : Bois, Eau, Minerais, etc.) et une valeur de compensation carbone potentielle.
- **Types de Terrains** : Plains (Plaines), Forest (Forêt), Mountain (Montagne), Coastal (Côtier), Urban (Urbain).
- **Coût d’Achat** : 200–350 EC selon le terrain.
- **Ressources associées** : Par exemple, la Forêt produit du Bois, la Montagne renferme des Minéraux et du Pétrole, etc.

### 3.2 Monnaies & Suivi

- **Eco-Credits (EC)** : Monnaie principale.
- **Points de Pollution (PP)** : Indicateur des émissions totales (air, eau, transport).
- **Carbon Credits** : Permettent de réduire ou compenser partiellement la pollution.

### 3.3 Usines&#x20;

Parmi les **10** usines par défaut (Timber Logging Camp, Crop Farm, Mine & Smelter, Bioplastics Plant, etc.), chacune possède :

- Un **coût de construction** (150–350 EC).
- Un **coût opérationnel** (15–40 EC/tour).
- Une **pollution de base** (1–8 PP).
- Des **besoins en ressources** (parfois nuls, parfois du Bois, de l’Eau, des Minéraux, etc.).
- Un **output** (Bois, Eau, Plastics, Fish, Consultancy Services, etc.), pouvant parfois générer des revenus (EC Output).
- **Types de terrain autorisés** (Forêt, Urbain, Montagne, etc.).
- **Rôles de travailleurs requis** : Ex. un *Technician* est requis pour le camp de bûcherons, un *Environmental Advisor* pour la Bioplastics Plant, etc.

### 3.4 Technologies

10 cartes de technologies, chacune fournissant un **effet** (réduction de pollution, augmentation de production, économie de coûts, etc.), un coût initial et un coût de maintenance, ainsi que d’éventuels **prérequis** (ex. devoir posséder un *Engineer* ou un *Environmental Advisor*).

Exemples :

- **Solar-Wind Hybrid Array** : -10 EC de coût opérationnel et -3 PP pour une usine.
- **Carbon Capture System** : -6 PP de l’usine assignée.
- **Electric Transport Network** : Réduit la pollution de 50% pour les transports électriques.

### 3.5 Système de Transport

Deux types :

1. **Electric** : Coût 50 EC/distance, Pollution 1 PP/distance.
2. **Fossil Fuel** : Coût 30 EC/distance, Pollution 3 PP/distance.

*Possibilité de réduire ces coûts via certaines technologies (ex. Fossil Fuel Subsidy) ou de diviser la pollution électrique par 2 (Electric Transport Network).*

### 3.6 Travailleurs

- **Engineer** (50 EC/tour) : +20% de production dans les usines avancées.
- **Technician** (30 EC/tour) : Maintien de la production de base.
- **Environmental Advisor** (40 EC/tour) : Réduit la pollution de l’usine à laquelle il est affecté de 3 PP.
- **Universal Worker** (20 EC/tour) : Soutien basique sans bonus particulier.

### 3.7 Gestion de la Pollution & Économie

- **Calcul** : Pollutions des usines + pollutions liées au transport.
- **Réduction** : Technologies, travailleurs *Environmental Advisor*, ou crédits carbone.
- **Taxe Carbone** : 5 EC × (total PP) à chaque tour.

---

## 4. RÈGLES DE JEU RÉVISÉES (SYNTHÈSE)

1. **Draft initial de Terrains** : Chaque joueur achète 2 tuiles de terrain (s’il en a les moyens).

2. **Construction initiale d’Usine** (optionnel) : Chaque joueur peut construire 1 usine.

3. **Tours de Jeu** (jusqu’à 6) :

   - *Phase de Production* : Activer chaque usine, payer les coûts, vérifier et payer les transports.
   - *Phase de Construction & Technologie* : Acheter de nouvelles tuiles, usines, améliorations, cartes de technologie.
   - *Phase de Commerce & Négociation* : Vendre/troquer les ressources ou services (Consultancy Services).
   - *Phase de Maintenance & Pollution* : Calcul de la pollution, taxe carbone, paiement des salaires, maintenance et ajustement du capital.

4. **Victoire** :

   - Le jeu se termine soit après 6 tours, soit quand un joueur atteint 3000 EC.
   - Calcul du score final = `EC ÷ (1 + PP)`. Le plus haut gagne.

*(La version **********************************************Companion App********************************************** gère automatiquement tous ces calculs.)*

---

## 5. RETOUR SUR LE **TRAVAIL D’ÉQUIPE**

Nous sommes une **équipe de 6 personnes** :

- **Membre 1** : Coordination globale et suivi du projet.
- **Membre 2** : Création du plateau physique et des composants (tuiles, pions, etc.).
- **Membre 3** : Programmation de la gestion des terrains et ressources (dans l’application).
- **Membre 4** : Développement des mécanismes des usines et travailleurs (dans l’application).
- **Membre 5** : Conception des règles de transport et de pollution (dont choix entre électrique / hydrocarbure).
- **Membre 6** : Développement et intégration des technologies dans le gameplay (effets et maintenance).

### Points positifs

- **Discussion fluide** : Les prises de décisions ont été menées de façon collaborative.
- **Clarté sur l’objectif** : Nous voulions clairement lier écologie et économie.
- **Flexibilité** : Adaptations rapides face aux problèmes rencontrés.

### Points difficiles

- **Surcharge** : Gérer en parallèle la version physique (maquette) et la version numérique (application) a complexifié l’avancement.
- **Équilibrage** : Les mécaniques du jeu sont riches (pollution, transport, usines, workers…), ce qui rend l’équilibrage long.
- **Gestion Git** : Multiples branches et résolutions de conflits sur GitHub (surtout quand la maquette physique n’était pas synchronisée).
- **Maquette physique peu utile** : Finalement, la version software est plus pertinente pour tester les règles avancées.

### À faire après la présentation

- **Mettre de côté la maquette physique** et rendre l’application *standalone* (intégrant toutes les étapes, règles et un mode multijoueur).
- Continuer le **test d’ergonomie** : Simplifier encore la prise en main, clarifier l’interface, documenter les règles in-app.

---

## 6. RETOUR SUR LES TESTS EFFECTUÉS

1. **Complexité du Jeu** :

   - Les joueurs trouvaient initialement les règles trop nombreuses, et la partie durait trop longtemps.
   - **Solution** : Simplification de la maquette (et des mécaniques secondaires), réduction de la durée à environ 60–90 minutes, et tutoriels plus clairs dans l’application.
   - **Impact** : Le jeu a légèrement dévié de sa visée ultra-simulatoire, mais demeure un **sérieux game** fonctionnel et plus accessible.

2. **Économie non optimale** :

   - Problème : La plupart des joueurs terminaient la partie en déficit.
   - **Solution** : Révision de l’économie (coûts d’usines/transport et revenus) afin que les joueurs puissent maintenir un flux positif de EC.
   - **Implémentation** : Dans la version finale de l’application, les valeurs de base (output, costs, upkeep) ont été ajustées.

3. **Manque de Version de en Français sur l'Application:**

   - **Problème:** L'application companion est en anglais, il manque l'ajout de la langue française.
   - **Solution:** Traduction de l'application en français. (Après la présentation).

1) **Objectifs Atteints** :
   - **Sensibilisation** : Les testeurs se sont rendu compte de l’importance des choix énergétiques et économique afin de trouver le juste milieu.
   - **Jouabilité** : Le jeu est devenu plus fluide après la rationalisation des règles et des coûts.
   - **Reste à Améliorer** : Potentiel d’ajouter un *mode multijoueur en ligne* pour faciliter les parties à distance et d'eliminer le besoin d'une maquette physique.

---

## 7. CONCLUSION

Avec la **Companion App** en Python/Tkinter et l’approche de **jeu de plateau** révisée :

1. **Le système de transport** (électrique vs fossile) est géré automatiquement par l’appli (calcul du coût et de la pollution).
2. **La pollution** (PP) et l’économie (EC) sont suivies en temps réel, avec gestion des taxes carbone.
3. **Les usines** et **technologies** sont cohérentes et intégrées : on achète, on assigne des travailleurs, on produit, on vend.
4. **Les tests utilisateurs** montrent une meilleure compréhension de l’équilibre entre développement industriel et durabilité.

**Prochaine étape** : finaliser la transition en **jeu 100% numérique** (standalone) avec potentiel multijoueur, tout en conservant l’esprit d’un *serious game*.



**Merci pour votre lecture et bonne partie !**
