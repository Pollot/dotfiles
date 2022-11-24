#!/bin/sh

if [[ $EUID -eq 0 ]]; then
  echo -e "\nThis script must NOT be run as root."
  exit 1
fi

cd ..

# Configuration files

cp -r .config $HOME

cp -r Wallpapers $HOME

cp -r .themes $HOME

cp -r .icons $HOME

cp bash/fedora/.bash_profile $HOME

echo -e "\nConfiguration files installed.\n"


# Zsh plugins

git clone https://github.com/zsh-users/zsh-autosuggestions $HOME/.config/zsh/zsh-autosuggestions

echo

git clone https://github.com/zsh-users/zsh-syntax-highlighting $HOME/.config/zsh/zsh-syntax-highlighting

ln -s $HOME/.config/zsh/.zshrc $HOME/.zshrc

echo -e "\nZsh plugins installed.\n"


# Fonts

sudo cp -r fonts /usr/share

sudo fc-cache -r

echo -e "\nFonts installed."