#!/bin/sh

# Keyboard layout
setxkbmap pl &

# Compositor
picom &

# Authentication agent
lxsession &

# Lock screen
xss-lock -- betterlockscreen -l