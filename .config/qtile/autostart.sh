#!/bin/sh

# Hotkey daemon
sxhkd &

# Lock screen
xss-lock -- i3lock -c 000000 &

# Compositor
picom &

# Authentication agent
/usr/libexec/polkit-gnome-authentication-agent-1 &

# Network Manager Applet
nm-applet