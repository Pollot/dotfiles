#!/bin/sh

if [[ $EUID -eq 0 ]]; then
  echo "This script must NOT be run as root" 1>&2
  exit 1
fi

cd $HOME/.config/zsh

git clone https://github.com/zsh-users/zsh-autosuggestions

echo

git clone https://github.com/zsh-users/zsh-syntax-highlighting

ln -s $HOME/.config/zsh/.zshrc $HOME/.zshrc

echo -e "\nZsh setup completed"
