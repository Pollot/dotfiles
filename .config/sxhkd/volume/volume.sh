#!/bin/sh

# You can call this script like this:
# $./volume.sh up
# $./volume.sh down
# $./volume.sh mute

interval="5" # Percentage by which to update the volume
high="$HOME/.config/sxhkd/volume/high-volume.png"
medium="$HOME/.config/sxhkd/volume/medium-volume.png"
low="$HOME/.config/sxhkd/volume/low-volume.png"
muted="$HOME/.config/sxhkd/volume/muted.png"

function get_volume {
    amixer get Master | grep '%' | head -n 1 | cut -d '[' -f 2 | cut -d '%' -f 1
}

function is_muted {
    amixer get Master | grep '%' | grep -oE '[^ ]+$' | grep off > /dev/null
}

function send_notification {
    volume=$(get_volume)
    
    if [[ $volume = 0 ]]; then
        dunstify -i "$muted" -t 1000 -r 2593 "  Volume: $volume%"
    elif [[ $volume < 30 ]] || [[ $volume = 5 ]] && [[ $volume != 100 ]]; then
        dunstify -i "$low" -t 1000 -r 2593 "  Volume: $volume%"
    elif [[ $volume < 75 ]] && [[ $volume != 100 ]]; then
        dunstify -i "$medium" -t 1000 -r 2593 "  Volume: $volume%"
    else
        dunstify -i "$high" -t 1000 -r 2593 "  Volume: $volume%"
    fi
}

function send_notification_muted {
    dunstify -i "$muted" -t 1000 -r 2593 "  Volume: Muted"
}

case $1 in
    up)
        # Set the volume on (if it was muted)
        if is_muted; then
            amixer -D "default" set Master on > /dev/null
            
            # pactl set-sink-mute @DEFAULT_SINK@ false
        fi

        amixer -q sset Master $interval%+

        # pactl set-sink-volume @DEFAULT_SINK@ +5%
        
        send_notification
	    ;;
    down)
        if is_muted ; then
            amixer -D "default" set Master on > /dev/null

            # pactl set-sink-mute @DEFAULT_SINK@ false
        fi

        amixer -q sset Master $interval%-
        
        #pactl set-sink-volume @DEFAULT_SINK@ -5%

        send_notification
	    ;;
    mute)
        amixer -D "default" set Master 1+ toggle > /dev/null
        
        # pactl set-sink-mute @DEFAULT_SINK@ toggle

        if is_muted ; then
            send_notification_muted
        else
            send_notification
        fi
	    ;;
esac
