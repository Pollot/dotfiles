#!/bin/sh

if [[ $EUID -ne 0 ]]; then
  echo -e "\nThis script must be run with root privileges."
  exit 1
fi

cd ..

cp -r fonts /usr/share

fc-cache -r

echo -e "\nFonts installed."