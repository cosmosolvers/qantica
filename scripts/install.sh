#!/bin/bash

# determiner le système d'exploitation
os=$(uname)
case "$os" in
  Linux*)
    install_dir="/usr/local/bin"
    ;;
  Darwin*)
    install_dir="/usr/local/bin"
    ;;
  MINGW*|MSYS*)
    install_dir="/c/Program Files/qantica"  # ou tout autre répertoire de votre choix
    ;;
  *)
    echo "Système d'exploitation non pris en charge"
    exit 1
    ;;
esac

# créer le répertoire d'installation
mkdir -p "$install_dir"

# copier le script qant dans le répertoire d'installation
cp qant "$install_dir"

# rendre le script exécutable (Linux et macOS)
if [ "$os" = "Linux" ] || [ "$os" = "Darwin" ]; then
  chmod +x "$install_dir/qant"
fi

# ajouter le répertoire d'installation au PATH
case "$os" in
  Linux*)
    echo "export PATH=\"\$PATH:$install_dir\"" >> ~/.bashrc
    ;;
  Darwin*)
    echo "export PATH=\"\$PATH:$install_dir\"" >> ~/.bash_profile
    ;;
  MINGW*|MSYS*)
    echo "export PATH=\"\$PATH:$install_dir\"" >> ~/.bashrc
    ;;
esac

# if [[ "$os" == "Linux*" || "$os" == "Darwin*" ]]; then
#   echo 'export PATH="$PATH:'"$install_dir"'"' >> ~/.bashrc  # ou tout autre fichier de profil de shell utilisé
#   source ~/.bashrc  # Recharger la configuration du shell actuel
# elif [[ "$os" == "MINGW*" || "$os" == "MSYS*" ]]; then
#   echo "$install_dir" >> $HOME/.bash_profile
# fi

echo "========== successful!!! ==========="
