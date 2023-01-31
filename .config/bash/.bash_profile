# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs
export QT_QPA_PLATFORMTHEME=gtk2

# run startx if it's not already started and you have just logged into tty1
if [ -z "${DISPLAY}" ] && [ "$(tty)" = "/dev/tty1" ]; then
	$HOME/scripts/session.sh
fi
