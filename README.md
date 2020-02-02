# Logizar CLI

Logizar est un lanceur de projet permettant à partir d'un invite de commande de manipuler les dossiers de projets au travers d'une batterie de commandes facilitant sont accèssibilité. En effet Logizar permet à partir d'une seule ligne de commande mettre en place l'environement de travail d'un projet.

Logizar CLI est en cours de dévéloppement et donc sa documentation n'est pas encore complète. Vous pouvez toutefois consulter le fichier todo.md qui contient quelque informations sur le projet. 

---

## Comment l'utiliser ?

Il suffit d'ajouter build\exe.win-amd64-3.7\ à votR$re PATH. Ainsi l'utilitaire sera disponible dans votre terminal. En pratique l'utilitaire s'utilise de la manière suivante:

	# Cette commande permet de lancer un projet du dossier fox en mode utilisation d(le lancement du projet est personnalisé par l'utilisateur dans un fichier nommé zar à la racine du projet)

	lgz run fox

	# Celle-ci ouvre un terminal sur le dossier du projet fox

	lgz shell fox

	# Celle-ci ouvre le dossier du projet fox

	lgz open fox

**Attention: Logizar est optimisé pour windows pour l'instant** 