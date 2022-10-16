# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Edited by:
#
# #####  ######  #       #       ######  #######
# #   #  #    #  #       #       #    #     #
# #####  #    #  #       #       #    #     #
# #      #    #  #       #       #    #     #
# #      ######  ######  ######  ######     #
#
# More information: https://github.com/Pollot/dot-files

##########################
######## Imports #########
##########################

import os
import subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras.widget.decorations import RectDecoration

##########################
####### Variables ########
##########################

mod = "mod4"
terminal = "alacritty"
browser = "firefox"
menu = "rofi -show run"
audio = "alsamixer"

location = "Warsaw"
weather = "firefox https://www.yr.no/en/forecast/daily-table/2-756135/Poland/Mazovia/Warszawa/Warsaw"
clock = "firefox https://www.timeanddate.com/worldclock/"

font_nerd = "MesloLGS NF"
font_default = "sans"
wlpr_dir = "~/Wallpapers/gray-cyan.png"

# Colours
gray_dark = "#222831"
gray_light = "#393e46"
gray_inactive = "#4c566a"
cyan = "#00adb5"
white = "#ffffff"
black = "#000000"
red = "#ff4400"
blue = "#215578"

##########################
######## Keybinds ########
##########################

keys = [
	# Basics
	Key([mod], "Return", 
    	lazy.spawn(terminal), 
    	desc="Launch terminal"
    	),
    Key([mod, "shift"], "return", 
    	lazy.spawn(menu), 
    	desc="Spawn a command using a rofi"
    	),
    Key([mod], "b", 
    	lazy.spawn(browser), 
    	desc="Launch a browser"
    	),
    Key([mod, "shift"], "c", 
    	lazy.window.kill(), 
    	desc="Kill focused window"
    	),
    # Qtile
    Key([mod, "shift"], "q", 
    	lazy.shutdown(), 
    	desc="Shutdown Qtile"
    	),
    Key([mod, "shift"], "r", 
    	lazy.reload_config(), 
    	desc="Reload the config"
    	),
	# Switch between monitors
    Key([mod], "w",
        lazy.to_screen(0),
        desc="Move focus to monitor 1"
        ),
    Key([mod], "e",
        lazy.to_screen(1),
        desc="Move focus to monitor 2"
        ),
    Key([mod], "period",
        lazy.next_screen(),
        desc='Move focus to the next monitor'
        ),
    Key([mod], "comma",
        lazy.prev_screen(),
        desc='Move focus to the prev monitor'
        ),
    # Switch between windows
    Key([mod], "j", 
    	lazy.layout.down(), 
    	desc="Move focus down"
    	),
    Key([mod], "k", 
    	lazy.layout.up(), 
    	desc="Move focus up"
    	),
    Key([mod], "space", 
    	lazy.layout.next(), 
    	desc="Move focus to the next window"
    	),
    # Move windows
    Key([mod, "shift"], "j", 
    	lazy.layout.shuffle_down(),
    	desc="Move window down"
    	),
    Key([mod, "shift"], "k", 
    	lazy.layout.shuffle_up(), 
    	desc="Move window up"
    	),
    # Window controls
    Key([mod], "h",
        lazy.layout.shrink(),
        desc="Shrink selected pane"
        ),
    Key([mod], "l",
        lazy.layout.grow(),
        desc="Expand selected pane"
        ),
    Key([mod], "m", 
    	lazy.window.toggle_fullscreen(), 
    	desc="Toggle window fullscreen"
    	),
    Key([mod], "f",
        lazy.window.toggle_floating(),
        desc="Toggle window floating mode"
        ),
    # Layouts
    Key([mod], "Tab", 
    	lazy.next_layout(), 
    	desc="Toggle between layouts"
    	),
]

groups = [
	Group("1", label="", layout="monadtall"),
	Group("2", label="", layout="monadtall"),
	Group("3", label="", layout="monadtall"),
	Group("4", label="", layout="monadtall"),
	Group("5", label="調", layout="max"),
	Group("6", label="ﭮ", layout="monadtall"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + control + letter of group = switch to & move focused window to group
            Key(
                [mod, "control"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = move focused window to group
            Key(
            	[mod, "shift"], 
            	i.name, 
            	lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name),
            ),
        ]
    )

#########################
######## Layouts ########
#########################

layout_theme = {
	"border_width": 2,
	"margin": 6,
	"border_focus": cyan,
	"border_normal": gray_dark,
}
                
layouts = [
	layout.MonadTall(**layout_theme),
	layout.MonadWide(**layout_theme),
	layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme),
    #layout.Floating(**layout_theme),
    #layout.Columns(**layout_theme),
    #layout.Stack(num_stacks=2, **layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Tile(**layout_theme),
    #layout.TreeTab(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Zoomy(**layout_theme),
]

#########################
######## Widgets ########
#########################

# Decorations
arrow = {
	"decorations": [PowerLineDecoration(path = "arrow_right")]
}

rounded = {
	"decorations": [PowerLineDecoration(path = "rounded_right")]
}

slash = {
	"decorations": [PowerLineDecoration(path = "back_slash")]
}

border = {
	"decorations": [RectDecoration(
		colour = cyan, 
		radius = 10, 
		filled = True, 
		padding_y = 4, 
		group = True)]
}


widget_defaults = dict(
    font = font_default,
    fontsize = 12,
    padding = 8,
    background = gray_dark,
    foreground = white,
)

extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
    	widget.CurrentLayoutIcon(
            scale = 0.6,
            use_mask = True,
            ),
		widget.GroupBox(
	    	fontsize = 18,
	    	font = font_nerd,
	    	highlight_method = "block",
	    	active = white,
	    	block_highlight_text_color = white,
	    	inactive = gray_dark,
	    	disable_drag = True,
	    	other_current_screen_border = blue,
	    	other_screen_border = gray_light,
	    	this_current_screen_border = blue,
	    	this_screen_border = gray_light,
	    	**border,
	    	),
	    widget.Systray(
	    	),
		widget.WindowName(
			),
		widget.Sep(
			linewidth = 0,
			padding = 10,
			**border,
			),
		widget.TextBox(
			text = "墳 ",
			font = font_nerd,
			fontsize = 14,
			padding = 0,
			mouse_callbacks = {"Button3": lazy.spawn(terminal + " -e " + audio)},
			foreground = black,
			**border,
			),
		widget.Volume(
			padding = 0,
			volume_app = terminal + " -e " + audio,
			foreground = black,
			**border,
			),
		widget.Sep(
			linewidth = 0,
			padding = 10,
			**border,
			),
		widget.Sep(
			linewidth = 0,
			padding = 10,
			**rounded,
			),
		widget.NvidiaSensors(
			format = "GPU: {temp}°C",
			padding = 0,
			threshold = 60,
			foreground_alert = red,
			background = gray_light,
			),
		widget.CPU(
			format = "CPU: {load_percent}%",
			background = gray_light,
			width = 80,
			),
		widget.Memory(
			format = "MEM: {MemPercent}%",
			padding = 0,
			background = gray_light,
			width = 70,
			),
		widget.Sep(
			linewidth = 0,
			background = gray_light,
			**slash,
			),
		widget.Net(
			interface = "eno1",
			format = "{down}",
			padding = 4,
			background = cyan,
			foreground = black,
			width = 55,
			),
		widget.TextBox(
			text = "",
			font = font_nerd,
			padding = 0,
			background = cyan,
			foreground = black,
			),
		widget.Sep(
			linewidth = 0,
			background = cyan,
			),
		widget.Net(
			interface = "eno1",
			format = "{up}",
			padding = 4,
			background = cyan,
			foreground = black,
			width = 55,
			),
		widget.TextBox(
			text = "祝",
			font = font_nerd,
			padding = 0,
			background = cyan,
			foreground = black,
			),
		widget.Sep(
			linewidth = 0,
			background = cyan,
			**slash,
			),
        widget.OpenWeather(
        	location = location,
        	format = "{icon} {main_temp: .0f}°{units_temperature}",
    		background = gray_light,
			mouse_callbacks = {"Button1": lazy.spawn(weather)},
			**slash,
            ),
        widget.Clock(
            format = "%A, %d %B - %H:%M", 
            background = cyan,
            foreground = black,
			mouse_callbacks = {"Button1": lazy.spawn(clock)},
            ),
    	]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[2] # removing systray
    return widgets_screen2

screens = [
    Screen(wallpaper=wlpr_dir, top=bar.Bar(init_widgets_screen1(), 32, margin=6)),
    Screen(wallpaper=wlpr_dir, top=bar.Bar(init_widgets_screen2(), 32, margin=6))
]

##########################
######## Floating ########
##########################

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
    ]
)

##########################
######### Rules ##########
##########################

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

##########################
####### Autostart ########
##########################

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])
    
# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
