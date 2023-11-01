## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

#### Supervision de l'application via Sentry
- Créer un projet SEntry et remplacer le code DSN Sentry dans le fichier `.env`

#### Sécurité de l'application
- Déplacer la variable Secret Key de l'application Django dans  `settings.py` vers le fichier `.env`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Déploiement

Pipeline CI/CD en place avec DockerHub et GitHub actions:
- Sur toutes les branches - Workflow `.github/workflows/run-tests.yml` :
  - Vérification du linting
  - Exécution des tests automatisés
  - Vérification couverture de test > 80%
- Sur la branche main (en plus des actions communes à toutes les branches) - Workflow `.github/workflows/deploy.yml` :
  - Création d'une image Docker
  - Publication de l'image Docker sur DockerHub
  - Récupération de l'image depuis le serveur d'application
  - Build du conteneur et lancement de l'image

### Configuration

#### Docker 
Nécessite Docker Desktop installé sur la machine locale.

#### DockerHub
Nécessite un compte dockerHub.

#### GitHub
Nécessite un compte GitHub.

#### Serveur de production
Nécessite un serveur fonctionnant avec ubuntu.
Informations nécessaires :
- Adresse IPv4
- Utilisateur
- Mot de passe

#### Projet Sentry paramétré dans l'application
Nécessite un projet sentry avec un code DSN à remplacer dans le fichier

### Etapes

#### 1. Modifier `docker-compose.yml`

Dans le fichier, remplacer `image: kivtor/ocp13:latest` par `image: <utilisateur_dockerhub>/<nom_repository>:latest`. Avec :
   - <utilisateur_dockerHub> = nom d'utilisateur dockerhub
   - <nom_repository> = nom du repository dockerhub dans lequel sont stockées les images Docker

#### 2. Modifier `.github/workflows/deploy.yml`
Dans le fichier, remplacer `image: kivtor/ocp13:latest` par `image: <utilisateur_dockerhub>/<nom_repository>:latest`. Avec :
   - <utilisateur_dockerHub> = nom d'utilisateur dockerhub
   - <nom_repository> = nom du repository dockerhub dans lequel sont stockées les images Docker

#### 3. Installer Docker sur le serveur 
Il faut exécuter les commandes suivantes en se connectant au serveur via ssh avec la commande :
```bash
ssh user@ip_address
```
Avec l'utilisateur et l'adresse ip du serveur destiné à héberger l'application

1. Mettre à jour la liste des packets :
```bash
sudo apt update
```
2. Installer pré-requisites pour permettre à `apt` d'échanger des packets en https :
```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
3. Ajouter clé GPG pour le repository Docker
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
4. Ajouter le repository Docker aux sources Apt
```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
```
5. Assurez-vous que vous installez depuis le registre Docker
```bash
apt-cache policy docker-ce
```

Vous devriez voir un output similaire à ceci :
```bash
docker-ce:
  Installed: (none)
  Candidate: 5:19.03.9~3-0~ubuntu-focal
  Version table:
     5:19.03.9~3-0~ubuntu-focal 500
        500 https://download.docker.com/linux/ubuntu focal/stable amd64 Packages
```
6. Notez que `docker-ce` n'est pas installé, mais que le candidat pour installation vient du repository Docker pour Ubuntu (`focal`)
7. Installez Docker :
```bash
sudo apt install docker-ce
```
Docker devrait être installé maintenant.
8. Vérifiez que c'est bien installé :
```bash
sudo systemctl status docker
```

La réponse devrait être similaire à ceci: 
```bash
Output

● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: active (running) since Tue 2020-05-19 17:00:41 UTC; 17s ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 24321 (dockerd)
      Tasks: 8
     Memory: 46.4M
     CGroup: /system.slice/docker.service
             └─24321 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
```

Le service se montre actif et en cours d'exécution (`active(running)`)

#### 4. Installer Docker Compose sur le serveur 
Il faut exécuter les commandes suivantes en se connectant au serveur via ssh avec la commande :
```bash
ssh user@ip_address
```

Avec l'utilisateur et l'adresse ip du serveur destiné à héberger l'application
1. Télécharger et enregistrer l'exécutable:
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
2. Corriger permission pour que la commande `docker-compose` soit exécutable:
```bash
sudo chmod +x /usr/local/bin/docker-compose
```
3. Vérifier que l'installation a bien été faite :
```bash
docker-compose --version
```
Il devrait y avoir une réponse similaire à ceci :
```bash
docker-compose version 1.29.2, build 5becea4c
```

#### 5. Créer une clé publique RSA
Toujours connecté au serveur via ssh

1. Exécuter cette commande et faire entrée à chaque question :
```bash
ssh-keygen -m PEM -t rsa -b 4096
```
2. Visualizer le contenu du fichier de clé publique
```bash
cat ~/.ssh/id_rsa.pub
```
3. Créer un fichier `authorized_keys` :
```bash
touch ~/.ssh/authorized_keys
```
4. Copier clé publique vers le fichier `authorized_keys`
```bash
cp ~/.ssh/id_rsa.pub ~/.ssh/authorized_keys
```
5. Mettre à jour les permissions
```bash
chmod 600 ~/.ssh/authorized_keys
chmod 600 ~/.ssh/id_rsa
```
6. Copier le résultat de ce code (nous allons le coller dans un fichier local)
```bash
cat ~/.ssh/id_rsa
```
7. Se déconnecter du server
```bash
exit
```
8. Créer un fichier private_key.pem sur votre machine local ajouter le contenu que vous avez copié après cette commande `cat ~/.ssh/id_rsa`
9. Se connecter à nouveau en utilisant le fichier `.pem`
```bash
ssh -i private_key.pem user@ip_address
```
Si vous êtes connecté alors tout est ok. On passe à l'étape suivante.

#### 6. Créer un token de connexion DockerHub
1. Connectez-vous à dockerHub
2. Sur votre profil, allez sur `Account Settings`
3. Allez dans le menu sécurité
4. Appuyez sur ![img.png](img.png)
5. Donner un nom au Token (GitHub par exemple), laisser les droits Read, Write, Delete
6. Appuyez sur générer
7. Copiez les informations et enregistrez-le dans un endroit sûr

#### 7. Paramétrer les secrets sur GitHub
Aller dans l'interface de paramétrage des secrets Github :

Dans le repository gitHub du projet aller dans :
- Settings
- Security > Secrets and variables
- Actions

Créer les secrets suivants :

| Nom de secret      | Secret                                               |
|--------------------|------------------------------------------------------|
| DOCKERHUB_TOKEN    | <Token DockerHub créé lors de l'étape précédente>    |
| DOCKERHUB_USERNAME | <Nom d'utilisateur du compte dockerHub>              |
| OVH_IP_ADDRESS     | <Addresse IP du serveur de production>               |
| OVH_PRIVATE_KEY    | <Clé privée crée à l'étape 4>                        |
| OVH_USER           | <Nom d'utilisateur du serveur de production>         |
| SECRET_KEY         | <Secret key de l'application Django du fichier .env> |
| SENTRY_DSN         | <Code DSN de connexion à Sentry du fichier .env>     |


#### 8. Testez les workflow :
   - Faites une modification de code dans une branche non main et commitez et pushez votre code vers GitHub
    &rarr; le workflow de vérification de linting, tests automatisés et couverture de code s'exécute
   - Faites une modification de code dans une branche main, commitez et pushez le code vers GitHub
   &rarr; s'éxecutent dans GitHub actions :
     - Le workflow de vérification de code
     - Le workflow de livraison continue
   &rarr; Votre application s'exécute dans votre serveur de production





