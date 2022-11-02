#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

# run startx if it's not already started and you logged into tty1
# exec ensures that the user is logged out when the X server exits, crashes or is killed
if [ -z "${DISPLAY}" ] && [ "$(tty)" = "/dev/tty1" ]; then
	exec startx "$HOME/.config/X11/xinitrc"
fi
