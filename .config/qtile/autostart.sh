#!/bin/sh

# Compositor
picom &

# Authentication agent
/usr/libexec/polkit-gnome-authentication-agent-1 &

# Lock screen
xss-lock -- i3lock -c 000000