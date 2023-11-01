Deployment
==========

Pipeline CI/CD en place avec DockerHub et GitHub actions: - Sur toutes
les branches - Workflow ``.github/workflows/run-tests.yml`` : -
Vérification du linting - Exécution des tests automatisés - Vérification
couverture de test > 80% - Sur la branche main (en plus des actions
communes à toutes les branches) - Workflow
``.github/workflows/deploy.yml`` : - Création d’une image Docker -
Publication de l’image Docker sur DockerHub - Récupération de l’image
depuis le serveur d’application - Build du conteneur et lancement de
l’image

Configuration
~~~~~~~~~~~~~

Docker
^^^^^^

Nécessite Docker Desktop installé sur la machine locale.

DockerHub
^^^^^^^^^

Nécessite un compte dockerHub.

GitHub
^^^^^^

Nécessite un compte GitHub.

Serveur de production
^^^^^^^^^^^^^^^^^^^^^

Nécessite un serveur fonctionnant avec ubuntu. Informations nécessaires
: - Adresse IPv4 - Utilisateur - Mot de passe

Projet Sentry paramétré dans l’application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nécessite un projet sentry avec un code DSN à remplacer dans le fichier

Etapes
~~~~~~

1. Modifier ``docker-compose.yml``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dans le fichier, remplacer ``image: kivtor/ocp13:latest`` par
``image: <utilisateur_dockerhub>/<nom_repository>:latest``.
Avec :
- <utilisateur_dockerhub> = nom d’utilisateur dockerhub
- <nom_repository> = nom du repository dockerhub dans lequel sont stockées les images Docker

2. Modifier ``.github/workflows/deploy.yml``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dans le fichier, remplacer ``image: kivtor/ocp13:latest`` par
``image: <utilisateur_dockerhub>/<nom_repository>:latest``.
Avec :
- <utilisateur_dockerhub> = nom d’utilisateur dockerhub
- <nom_repository> = nom du repository dockerhub dans lequel sont stockées les images Docker

3. Installer Docker sur le serveur
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il faut exécuter les commandes suivantes en se connectant au serveur via
ssh avec la commande :

.. code:: bash

   ssh user@ip_address

Avec l’utilisateur et l’adresse ip du serveur destiné à héberger
l’application

1. Mettre à jour la liste des packets :

.. code:: bash

   sudo apt update

2. Installer pré-requisites pour permettre à ``apt`` d’échanger des
   packets en https :

.. code:: bash

   sudo apt install apt-transport-https ca-certificates curl software-properties-common

3. Ajouter clé GPG pour le repository Docker

.. code:: bash

   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

4. Ajouter le repository Docker aux sources Apt

.. code:: bash

   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"

5. Assurez-vous que vous installez depuis le registre Docker

.. code:: bash

   apt-cache policy docker-ce

Vous devriez voir un output similaire à ceci :

.. code:: bash

   docker-ce:
     Installed: (none)
     Candidate: 5:19.03.9~3-0~ubuntu-focal
     Version table:
        5:19.03.9~3-0~ubuntu-focal 500
           500 https://download.docker.com/linux/ubuntu focal/stable amd64 Packages

6. Notez que ``docker-ce`` n’est pas installé, mais que le candidat pour
   installation vient du repository Docker pour Ubuntu (``focal``)
7. Installez Docker :

.. code:: bash

   sudo apt install docker-ce

Docker devrait être installé maintenant. 8. Vérifiez que c’est bien
installé :

.. code:: bash

   sudo systemctl status docker

La réponse devrait être similaire à ceci:

.. code:: bash

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

Le service se montre actif et en cours d’exécution (``active(running)``)

4. Installer Docker Compose sur le serveur
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il faut exécuter les commandes suivantes en se connectant au serveur via
ssh avec la commande :

.. code:: bash

   ssh user@ip_address

Avec l’utilisateur et l’adresse ip du serveur destiné à héberger
l’application 1. Télécharger et enregistrer l’exécutable:

.. code:: bash

   sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

2. Corriger permission pour que la commande ``docker-compose`` soit
   exécutable:

.. code:: bash

   sudo chmod +x /usr/local/bin/docker-compose

3. Vérifier que l’installation a bien été faite :

.. code:: bash

   docker-compose --version

Il devrait y avoir une réponse similaire à ceci :

.. code:: bash

   docker-compose version 1.29.2, build 5becea4c

5. Créer une clé publique RSA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toujours connecté au serveur via ssh

1. Exécuter cette commande et faire entrée à chaque question :

.. code:: bash

   ssh-keygen -m PEM -t rsa -b 4096

2. Visualizer le contenu du fichier de clé publique

.. code:: bash

   cat ~/.ssh/id_rsa.pub

3. Créer un fichier ``authorized_keys`` :

.. code:: bash

   touch ~/.ssh/authorized_keys

4. Copier clé publique vers le fichier ``authorized_keys``

.. code:: bash

   cp ~/.ssh/id_rsa.pub ~/.ssh/authorized_keys

5. Mettre à jour les permissions

.. code:: bash

   chmod 600 ~/.ssh/authorized_keys
   chmod 600 ~/.ssh/id_rsa

6. Copier le résultat de ce code (nous allons le coller dans un fichier
   local)

.. code:: bash

   cat ~/.ssh/id_rsa

7. Se déconnecter du server

.. code:: bash

   exit

8. Créer un fichier private_key.pem sur votre machine local ajouter le
   contenu que vous avez copié après cette commande
   ``cat ~/.ssh/id_rsa``
9. Se connecter à nouveau en utilisant le fichier ``.pem``

.. code:: bash

   ssh -i private_key.pem user@ip_address

Si vous êtes connecté alors tout est ok. On passe à l’étape suivante.

6. Créer un token de connexion DockerHub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Connectez-vous à dockerHub
2. Sur votre profil, allez sur ``Account Settings``
3. Allez dans le menu sécurité
4. Appuyez sur |img.png|
5. Donner un nom au Token (GitHub par exemple), laisser les droits Read,
   Write, Delete
6. Appuyez sur générer
7. Copiez les informations et enregistrez-le dans un endroit sûr

7. Paramétrer les secrets sur GitHub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Aller dans l’interface de paramétrage des secrets Github :

Dans le repository gitHub du projet aller dans :
- Settings
- Security > Secrets and variables
- Actions

Créer les secrets suivants :

+--------------------+------------------------------------------------------+
| Nom de secret      | Description                                          |
+====================+======================================================+
| DOCKERHUB_TOKEN    | <Token DockerHub créé lors de l’étape précédente>    |
+--------------------+------------------------------------------------------+
| DOCKERHUB_USERNAME | <Nom d’utilisateur du compte dockerHub>              |
+--------------------+------------------------------------------------------+
| OVH_IP_ADDRESS     |                                                      |
+--------------------+------------------------------------------------------+
| OVH_PRIVATE_KEY    | <Clé privée crée à l’étape 4>                        |
+--------------------+------------------------------------------------------+
| OVH_USER           | <Nom d’utilisateur du serveur de production>         |
+--------------------+------------------------------------------------------+
| SECRET_KEY         | <Secret key de l’application Django du fichier .env> |
+--------------------+------------------------------------------------------+
| SENTRY_DSN         | <Code DSN de connexion à Sentry du fichier .env>     |
+--------------------+------------------------------------------------------+

8. Testez les workflow :
^^^^^^^^^^^^^^^^^^^^^^^^

-  Faites une modification de code dans une branche non main et commitez
   et pushez votre code vers GitHub → le workflow de vérification de
   linting, tests automatisés et couverture de code s’exécute
-  Faites une modification de code dans une branche main, commitez et
   pushez le code vers GitHub → s’éxecutent dans GitHub actions :

   -  Le workflow de vérification de code
   -  Le workflow de livraison continue → Votre application s’exécute
      dans votre serveur de production

.. |img.png| image:: ../img.png