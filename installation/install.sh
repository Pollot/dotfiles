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

cp -r scripts $HOME

ln -sf $HOME/.config/bash/.bash_profile $HOME/.bash_profile

# GTK 4
mkdir $HOME/.config/gtk-4.0
ln -sf $HOME/.themes/Catppuccin-Macchiato-Standard-Mauve-Dark/gtk-4.0/assets $HOME/.config/gtk-4.0/assets
ln -sf $HOME/.themes/Catppuccin-Macchiato-Standard-Mauve-Dark/gtk-4.0/gtk.css $HOME/.config/gtk-4.0/gtk.css
ln -sf $HOME/.themes/Catppuccin-Macchiato-Standard-Mauve-Dark/gtk-4.0/gtk-dark.css $HOME/.config/gtk-4.0/gtk-dark.css

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