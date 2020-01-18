##  A FAIRE
- [x] Mettre en place un système listant simplement les projets au travers d'une commande
- [x] Introduire de la notion de dossier par défaut
	- Le dossier par défaut contient la liste des dossiers qui seront considéré comme dossier de projet par logizar
	- Ce sont ces dossiers qui seront scannés afin de trouver des projets qui peuvent être [hébergé par logizar]
- [x] Mettre en place en système de reconnaissance de dossier de projet [hébergeable par logizar]
	- Un dossier des hébergeable s'il contient un fichier [todo.md]
	- le chemin vers les dossiers de projet seront enregistré dans un fichier(projets.lgz) dans le dossier data/
- [x] Faire une commande qui affiche les dossiers de projets hébergeable trouvé [list3]

- [x] Mise en place de la base de la chaine d'execution

- Ajout de logizar au PATH automatiquement afin de l'ouvrir directement depuis un terminal
	- Après tentative il est préférable de faire cette fonctionnalité après(Une mauvaise manipulation du path peut endommagé le système)

- Ajout d'une instruction de temporisation au fichier zar

- créer un exécutable pour lgz.py


## BRAINSTRORMING
- Faire une commande pour configurer les dossiers de projets par défaut


## RECENT
- Vérifier qu'une clé existe avant de faire un get_dir

- Travailler sur un version utilisable de Logizar CLI 
	- L'exécution des commandes directemet dans le cli néccéssite l'utilsation de l'instruction: 
		- "python PATH/lgz.py [arguments]" ou 
		- "python -m lgz [arguments]" 
	- Cette dernière est la meilleure car elle fonctionne partout mais depend de la définition du PYTHONPATH

	- Créer un exécutable


# NOTE
- La version du cli actuel dépend du PATH windows et PYTHONPATH de python
- Créer une commande pour ignorer un dossier lgz ignore: [Nom dossier]
- Les dossiers qui possèdent un fichier zar ou un fichier todo.md sont considérés comme des dossiers lgz
- Gérer le cas de la non existence du dossier data/ 0.0.2


## COMMANDES
- ^open: [0-9]+ :: Commande pour ouvrir un dossier de projet enregistré suite à un scanne à partir de son id
- ^open2: (.)+ :: Commande pour ouvrir un dossier de projet enregistré suite à un scanne à partir du nom du dossier
- ^scan :: Recherche les dossiers lgz dans les dossiers de projet. Une fois l'ensemble des projets trouvés ces derniers sont enregistrés dans le fichier data/projers.lgz. Un dossier lgz possède un fichier zar ou todo.md à sa racine
- ^list3 :: Affiche la liste des dossiers lgz
- ^shell: ((.)|[0-9])+ :: Lance un terminal sur le dossier spécifié en paramètre
- ^cmd: (.)+ :: les paramètres commen étant une commande du terminal windows
- ^run: ((.)|[0-9])+ :: Lance la chaine d'exécution du dossier lgz passer en paramètre



## WIKI TECHNIQUE
Lorsque que le CLI est lancé le fichier projets.lgz est chargé et les dossiers lgz sont chargés globalement.
Pour mettre à jour la liste des dossiers lgz il faut lancer la commande [scan]