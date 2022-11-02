#!/bin/sh

if [[ $EUID -eq 0 ]]; then
  echo "This script must NOT be run as root" 1>&2
  exit 1
fi

cd ..

cp -r .config/* $HOME/.config/

cp -r scripts $HOME

cp -r Wallpapers $HOME

rm $HOME/.bash_profile

cp bash/.bash_profile $HOME

echo "Dotfiles installed"