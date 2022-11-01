#!/bin/sh

if [[ $UID != 0 ]]; then
    echo "Please run this script with sudo:"
    echo "sudo $0 $*"
    exit 1
fi

cd ../fonts

cp -r google /usr/share/fonts && cp -r nerd-fonts /usr/share/fonts

fc-cache -r

echo "Fonts installed (use fc-list to validate)"
