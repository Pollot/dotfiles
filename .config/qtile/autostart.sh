#!/bin/sh

# Compositor
picom &

# Authentication agent
lxsession &

# Lock screen
xss-lock betterlockscreen -l