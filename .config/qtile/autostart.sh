#!/bin/sh

# Compositor
picom &

# Authentication agent
/usr/libexec/polkit-gnome-authentication-agent-1 &

# Network Manager Applet
nm-applet &

# VPN, change "Warsaw" to the name of your VPN profile
nmcli connection up Warsaw &

# Lock screen
xss-lock -- i3lock -c 000000