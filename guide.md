# Mettre en place son environnement de travail


Dans ce guide on va voir comment :
- Mettre en place son environnement Linux 
- Mettre en place les différents outils 
- Mettre en pratique les commandes importantes

# 📚 Installation

## Etape 1 : Installer WSL via le powershell 
        wsl --install

Cela permet d’installer une plateforme de machine virtuelle, un sous-système Windows pour Linux et Ubuntu. (Ne pas fermer la console)

Puis on redémarre son PC.

Au redémarrage, une console Ubuntu est ouverte : 

On entre simplement notre prénom et un mdp **que l'on est sûr de pas perdre** !

## Etape 2 : [Installez uv](https://github.com/astral-sh/uv)

![uv](images/uv.png)

Il suffira de taper la commande :

        curl -LsSf https://astral.sh/uv/install.sh | sh

**Puis redémarrez le terminal !** 

Pour installer n'importe quel module python, on prendra l'habitude de taper : 

        uv pip install module_python

Le lien envoie vers la documentation (n'hésitez pas à la consulter).

## Etape 3 : Installer VSCode

        sudo apt install code --classic

Vous pouvez également télécharger la version pour Windows directement sur leur site : https://code.visualstudio.com/

Puis dans la section `Extensions`, installez quelques extensions très utiles pour la suite :

- Python
- Jupyter
- Remote - SSH
- WSL
- Continue - Llama3

## Etape 4 : Installer Python, Anaconda

## Etape 5 (Optionnel, voir avec responsable) : Installer l'autosuggestion [zsh/ohmyzsh](https://rdr-it.io/ameliorer-son-terminal-avec-zsh-sur-ubuntu-debian/) terminal

        sudo apt install zsh
        sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

        ___________________________________________________________________
        # Ohmyzsh permet entre autre de changer le thème de son terminal
        On peut aller sur ce site pour trouver le thème qui nous convient.
        Puis
        nano .zshrc 
        Et dans le paramètre ZSH_THEME, remplacer le thème par défaut.
        _____________________________________________________________________

        git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions
        echo "source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh" ~/.zshrc
        Puis redémarrer le terminal

        git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.zsh/zsh-syntax-highlighting
        echo "source ~/.zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"  ~/.zshrc
        Puis redémarrer le terminal

        git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
        git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting


        vim ~/.zshrc (permet de gérer toutes les dépendances et lien avec bash)
        puis dans le (git) ajouter avec i zsh-autosuggestions et zsh-syntax-highlighting
        et copier coller tout en bas ceci (en adaptant en fonction de l'appareil) : 
        export PATH="/home/remy/.local/bin:$PATH"

        . "$HOME/.cargo/env"

        export PYENV_ROOT="$HOME/.pyenv"
        [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
        eval "$(pyenv init -)"
        puis esc :wq


# 📚 Les commandes et bonnes pratiques linux

## Création de ses propres alias quand on est amené à taper souvent les mêmes commandes : 

        vim .bashrc ou/zshrc #pour créer mes alias
        i (insert)
        alias mon_alias='la commande bash'
        esc (echap)
        :q #pour quitter simplement
        : wq # svg des modifs 
        Puis relancer le termianl ou faire source $HOME/.bashrc ou/zshrc

## Les classiques (⚠️Ne pas omettre les espaces ⚠️) :

        ls # pour voir tout les dossiers du repertoire courant
        cd nom_repertoire # pour accéder au repertoire souhaiter
        cd - # pour revenir en arrière
        cd .. # pour remonter d'un dossier 
        cd\ # pour revenir à la racine
        mkdir nom_dossier_a_creer # pour créer un dossier 
        clear # effacer le repertoire 
        pwd # pour afficher le chemin du répertoire dans lequel on se trouve
        ________________________________
        sudo # pour les installations importantes avec les droits admin
        # Demande toujours un mdp
        exemple : sudo apt install rename 
        pour installer la commande permettant de rename un dossier

        rename ancienNom nouveauNom
        # Utiliser mv ça marche mieux
        __________________________________

        rm # pour supprimer un fichier du dossier
        rm -r # pour vider le répertoire et le supprimer.
        rm -rf + le nom du dossier à supprimer # supprimer précisement un dossier
        cp # pour copier des fichiers et des répertoires
        mv # permet de déplacer ou de renommer des fichiers et des répertoires


        git clone url_du_projet_à_cloner # Récupérer l'entièreté d'un github 
        exemple : git clone https://github.com/vienneraphael/scalene-codecarbon-workshop


        crtl+%  # pour ouvrir une console linux directement dans vs code

        code ./ # pour lancer vs code à partir du répertoire dans lequel on se trouve
        exemple : Après plusieurs cd/ls pour attérir dans mon répertoire de travail,
        je tape code ./ et j'accède directement au contenu de mon répertoire de travail


## Créer un environnement virtuel de travail 

        # Méthode de base mais très lent, privilégier uv
        python -m venv <environment name>
        source <environment name>/bin/activate
        pip install modules_necessaires_pour ce projet
        code ./
        deactivate # pour quitter cet environnement virtuel

        pip freeze # Pour voir les modules installés


        # Plus rapide pour les pip 
        uv venv + Si on veut :nom_de_environnement 
        # A faire seulement la première fois, après on tape directement :
        source nom_de_environnement/bin/activate (alias sa)
        # Installation des modules utiles, exemple : 
        uv pip install scalene numpy  setuptools
        uv pip install scalene==1.5.34

        # Si requirements 
        uv pip install -r requirements.txt

        # Si pyproject.toml(beaucoup mieux)(toujours conserver les espaces)
        uv pip install -e . 

## Afficher les informations du système dans un terminal
        sudo apt install neofetch

Puis 

        neofetch


## Avoir des informations sur son cpu

        lscpu

## Si une commande n'est plus reconnue 
    #Dans le powershell
    wsl --shutdown
    #Puis dans le powershell
    wsl
    #Revenir dans le terminal linux  


## Pour créer une commande ssh
    # exemple pour générez une clef ssh sur windows ou linux 
    ssh-keygen -t rsa -b 4096 -C "votre_adresse_mail"
    en fonction de si c'est sur linux ou windows : 
    cat .ssh/id_rsa_datacraft.pub
    cat /mnt/c/Users/admin/.ssh/id_rsa.pub

## Pour obtenir sa clé ssh  
    cat .ssh/id_rsa.pub

# Source : 

https://juliend.github.io/linux-cheatsheet/