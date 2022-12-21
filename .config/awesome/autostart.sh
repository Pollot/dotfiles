#!/bin/sh

# Function checking whether there is already an instance of program running
function run { 
    if ! pgrep $1 ; 
    then 
        $@& 
    fi 
}

# Hotkey daemon
run sxhkd

# Lock screen
run xss-lock -- i3lock -c 000000

# Compositor
run picom

# Authentication agent
run /usr/libexec/polkit-gnome-authentication-agent-1

# Network Manager Applet
run nm-applet