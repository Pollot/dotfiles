#!/bin/sh

if [[ $EUID -eq 0 ]]; then
  echo -e "\nThis script must NOT be run as root."
  exit 1
fi

PS3='Please enter your choice: '
options=("Awesome" "Qtile" "TTY")
select opt in "${options[@]}"
do
	case $opt in
    	"Awesome")
        	exec startx "$HOME/.config/X11/xinitrc-awesome"
        	;;
		"Qtile")
        	exec startx "$HOME/.config/X11/xinitrc-qtile"
        	;;
    	"TTY")
        	break
        	;;
    	*) echo "Invalid option, try again.";;
	esac
done

# exec ensures that the user is logged out when the X server exits, crashes or is killed
