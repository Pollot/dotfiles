#!/bin/sh

if [[ $EUID -eq 0 ]]; then
  echo "This script must NOT be run as root." 1>&2
  exit 1
fi

cd ..

# Configuration files

cp -r .config/* $HOME/.config

cp -r scripts $HOME

cp -r Wallpapers $HOME

cp bash/.bash_profile $HOME

echo -e "Configuration files installed.\n"


# Zsh plugins

git clone https://github.com/zsh-users/zsh-autosuggestions $HOME/.config/zsh

echo

git clone https://github.com/zsh-users/zsh-syntax-highlighting $HOME/.config/zsh

ln -s $HOME/.config/zsh/.zshrc $HOME/.zshrc

echo -e "\nZsh plugins installed."


# Fonts

sudo

cp -r fonts/google /usr/share/fonts

cp -r fonts/nerd-fonts /usr/share/fonts

fc-cache -r

echo -e "\nFonts installed."