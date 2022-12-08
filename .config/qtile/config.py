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
# Edited by: https://github.com/Pollot
# More information: https://github.com/Pollot/dot-files

#########################
######## Imports ########
#########################

import os
import subprocess

from libqtile import (
    bar,
    layout,
    widget,
    hook,
    qtile,
)
from libqtile.config import (
    Click,
    Drag,
    Group,
    Key,
    Match,
    Rule,
    Screen,
)
from libqtile.lazy import lazy

# Colours
from colours import *

# OpenWeatherMap API key and symbols
from owm import owm_api, owm_symbols

# Power menu
from powermenu import show_power_menu


##########################
####### Variables ########
##########################

# mod4 -> Windows key ; mod1 -> ALT
mod = "mod4"

notification = "notify-send -t 1000 'Qtile'"

# Applications for widgets mouse callbacks
terminal = "kitty --class floating"
audio = "pavucontrol"
audio2 = "alsamixer"
process_monitor = "htop"
weather_app = "gnome-weather"
calendar_app = "gnome-calendar"
clock_app = "gnome-clocks"

# Updates widget
distro = "Fedora"
update = "sudo dnf update"
# distro = "Arch_checkupdates"
# update = "sudo pacman -Syu"

# OWM widget
city_id = "756135"  # openweathermap.org/city/[city id]

gap_size = 8
font_size = 16
icon_small = 20
icon_normal = 22
icon_big = 26  # group and weather icons

font_default = "Open Sans"
font_nerd = "FiraCode Nerd Font Mono"

wlp1 = "~/Wallpapers/city.jpg"
wlp2 = "~/Wallpapers/stardust.jpg"


##########################
######## Keybinds ########
##########################

keys = [
    # Basics
    Key([mod, "control", "shift"], "q",
        lazy.shutdown(),
        desc="Quit Qtile"
        ),
    Key([mod, "shift"], "r",
        lazy.reload_config(),
        desc="Reload config"
        ),
    Key([mod], "w",
        lazy.function(show_power_menu),
        desc="Show power menu"
        ),
    Key([mod, "shift"], "c",
        lazy.window.kill(),
        desc="Kill focused window"
        ),
    # Layouts
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
        ),
    # Switch between monitors
    Key([mod], "q",
        lazy.to_screen(0),
        desc="Move focus to screen 0"
        ),
    Key([mod], "e",
        lazy.to_screen(1),
        desc="Move focus to screen 1"
        ),
    # Switch between windows
    Key([mod], "j",
        lazy.layout.up(),
        desc="Move focus up"
        ),
    Key([mod], "k",
        lazy.layout.down(),
        desc="Move focus down"
        ),
    Key([mod], "space",
        lazy.group.next_window(),
        desc="Move focus to next window in the group"
        ),
    # Move windows
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_up(),
        desc="Move window up"
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_down(),
        desc="Move window down"
        ),
    Key([mod, "shift"], "q",
        lazy.window.toscreen(0),
        desc="Move window to screen 0"
        ),
    Key([mod, "shift"], "e",
        lazy.window.toscreen(1),
        desc="Move window to screen 1"
        ),
    # Resize windows
    Key([mod, "control"], "j",
        lazy.layout.shrink(),
        desc="Shrink window"
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow(),
        desc="Expand window"
        ),
    Key([mod], "h",
        lazy.layout.shrink_main(),
        desc="Shrink master pane"
        ),
    Key([mod], "l",
        lazy.layout.grow_main(),
        desc="Expand master pane"
        ),
    Key([mod, "control"], "n",
        lazy.layout.normalize(),
        desc="Normalize"
        ),
    # Change windows state
    Key([mod, "shift"], "m",
        lazy.window.toggle_maximize(),
        desc="Toggle window maximize"
        ),
    Key([mod, "shift"], "n",
        lazy.window.toggle_minimize(),
        desc="Toggle window minimize"
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle window fullscreen"
        ),
    # Floating controls
    Key([mod], "f",
        lazy.window.toggle_floating(),
        desc="Toggle window floating mode"
        ),
    Key([mod], "bracketleft",
        lazy.group.prev_window(),
        lazy.window.bring_to_front(),
        desc="Cycle previous floating window",
        ),
    Key([mod], "bracketright",
        lazy.group.next_window(),
        lazy.window.bring_to_front(),
        desc="Cycle next floating windows",
        ),
]


########################
######## Groups ########
########################

groups = [
    Group("1", label="", layout="monadtall"),
    Group("2", label="", layout="monadtall"),
    Group("3", label="", layout="monadtall"),
    Group("4", label="ﳳ", layout="max"),
    Group("5", label="調", layout="max"),
    Group("6", label="ﭮ", layout="max"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key([mod],
                i.name,
                lazy.group[i.name].toscreen(),
                lazy.spawn(notification + " 'Group " + i.name + "'"),
                desc="Switch to group {}".format(i.name),
                ),
            # mod1 + control + letter of group = switch to & move focused window to group
            Key([mod, "control"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                lazy.spawn(notification + " 'Group " + i.name + "'"),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
                ),
            # mod1 + shift + letter of group = move focused window to group
            Key([mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name),
                ),
        ]
    )

# Moves windows to chosen groups
dgroups_app_rules = [
    Rule(Match(wm_class="code"), group="2"),
    Rule(Match(wm_class="firefox"), group="3"),
    Rule(Match(wm_class="keepassxc"), group="4"),
    Rule(Match(wm_class="lutris"), group="5"),
    Rule(Match(wm_class="Steam"), group="5"),
    Rule(Match(wm_class="discord"), group="6"),
]


@hook.subscribe.client_managed
def auto_switch(window):
    if window.group.name != qtile.current_group.name:
        window.group.cmd_toscreen()
        qtile.cmd_spawn(notification + " 'Group " +
                        qtile.current_group.name + "'")


#########################
######## Layouts ########
#########################

layout_theme = {
    "border_width": 2,
    "margin": gap_size,
    "border_focus": mauve,
    "border_normal": base,
}

layouts = [
    layout.MonadTall(
        new_client_position="top",
        change_size=40,
        **layout_theme,
    ),
    layout.MonadWide(
        new_client_position="top",
        change_size=40,
        **layout_theme,
    ),
    layout.Max(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Floating(**layout_theme),
    # layout.Columns(**layout_theme),
    # layout.Stack(num_stacks=2, **layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme),
]


##########################
#### Widgets defaults ####
##########################

widget_defaults = dict(
    background=mantle,
    foreground=text,
    font=font_default,
    fontsize=font_size,
    padding=0,
)

extension_defaults = widget_defaults.copy()


#################################
#### Screen specific widgets ####
#################################
# Defined in functions:
# They need to be independent
# from other screens.


def current_layout_icon():
    return widget.CurrentLayoutIcon(
        scale=0.6,
    )


def group_box():
    return widget.GroupBox(
        disable_drag=True,
        padding=6,
        margin_y=5,
        font=font_nerd,
        fontsize=icon_big,
        highlight_method="line",
        active=text,
        inactive=overlay0,
        highlight_color=[mantle, mantle],
        block_highlight_text_color=mauve,
        other_current_screen_border=mauve,
        other_screen_border=mantle,
        this_current_screen_border=mauve,
        this_screen_border=overlay0,
    )


def systray():
    return widget.Systray(
        icon_size=icon_small,
        padding=10,
    )


def tasklist():
    return widget.TaskList(
        highlight_method="block",
        title_width_method="uniform",
        border=surface0,
        padding=10,
        margin_y=-6,
        rounded=False,
        icon_size=0,
        # font=font_nerd,
        fontsize=font_size,
        txt_floating=" 禎 ",
        txt_maximized=" ⤢ ",
        txt_minimized=" ⚊ ",
    )


########################
#### Normal Widgets ####
########################
# Defined as standard variables:
# They can be mirrored on other
# screens to save resources.

volume_text = widget.TextBox(
    foreground=mauve,
    text="墳",
    font=font_nerd,
    fontsize=icon_normal,
    mouse_callbacks={"Button1": lazy.spawn(
        "amixer set Master toggle")},
)

volume = widget.Volume(
    foreground=mauve,
    volume_app=terminal + " -e " + audio2,
    mouse_callbacks={"Button1": lazy.spawn(audio)},
)

updates_text = widget.TextBox(
    foreground=blue,
    text="ﮮ",
    font=font_nerd,
    fontsize=icon_normal,
    mouse_callbacks={"Button1": lazy.spawn(
        terminal + " -e sudo pacman - Syu")},
)

updates = widget.CheckUpdates(
    colour_no_updates=blue,
    colour_have_updates=blue,
    update_interval=1800,
    no_update_string="Up to date",
    display_format="{updates}",
    initial_text="Checking...",
    distro=distro,
    execute=terminal + " -e " + update,
)

memory_text = widget.TextBox(
    foreground=green,
    text="",
    font=font_nerd,
    fontsize=icon_normal,
)

memory = widget.Memory(
    foreground=green,
    format="{MemPercent:.0f}%",
    mouse_callbacks={"Button1": lazy.spawn(
        terminal + " -e " + process_monitor)},
)

owm_text = widget.OpenWeather(
    foreground=green,
    app_key=owm_api,
    cityid=city_id,
    format="{icon}",
    weather_symbols=owm_symbols,
    font=font_nerd,
    fontsize=icon_big,
)

owm = widget.OpenWeather(
    foreground=green,
    cityid=city_id,
    app_key=owm_api,
    format="{main_temp:.0f}°{units_temperature}",
    mouse_callbacks={"Button1": lazy.spawn(weather_app)},
)

calendar_text = widget.TextBox(
    foreground=peach,
    text="",
    font=font_nerd,
    fontsize=icon_normal,
)

calendar = widget.Clock(
    foreground=peach,
    format="%a, %b %-d",
    mouse_callbacks={"Button1": lazy.spawn(calendar_app)},
)

clock_text = widget.TextBox(
    foreground=red,
    text="",
    font=font_nerd,
    fontsize=icon_normal,
)

clock = widget.Clock(
    foreground=red,
    format="%-H:%M:%S",
    mouse_callbacks={"Button1": lazy.spawn(clock_app)},
)


#########################
######## Spacers ########
#########################

spacer_normal = widget.Spacer(
    length=20,
)

spacer_medium = widget.Spacer(
    length=10,
)

spacer_small = widget.Spacer(
    length=6,
)


#########################
##### Widgets lists #####
#########################

def widgets_screen1():
    widgets = [
        spacer_small, current_layout_icon(), group_box(),

        tasklist(), systray(),

        # spacer_medium, volume_text, spacer_small, volume,

        # spacer_normal, memory_text, spacer_small, memory,

        spacer_normal, owm_text, spacer_small, owm,

        spacer_normal, updates_text, spacer_small, updates,

        spacer_normal, calendar_text, spacer_small, calendar,

        spacer_normal, clock_text, spacer_small, clock, spacer_medium,
    ]
    return widgets


def widgets_screen2():
    widgets = widgets_screen1()
    del widgets[4:6]  # remove systray and normal spacer
    widgets.insert(4, spacer_medium)  # add spacer after tasklist
    return widgets


#########################
######## Screens ########
#########################

screens = [
    Screen(
        wallpaper=wlp1,
        wallpaper_mode="fill",
        top=bar.Bar(
            widgets_screen1(),
            32,
            background=mantle,
        )
    ),
    Screen(
        wallpaper=wlp2,
        wallpaper_mode="fill",
        top=bar.Bar(
            widgets_screen2(),
            32,
            background=mantle,
        )
    ),
]


##########################
######## Floating ########
##########################

mouse = [
    Drag([mod], "Button1",
         lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3",
         lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button1",
          lazy.window.bring_to_front()),
]

floating_layout = layout.Floating(
    border_focus=red,
    border_normal=base,
    border_width=2,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="floating"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="org.gnome.Weather"),
        Match(wm_class="gnome-calendar"),
        Match(wm_class="org.gnome.clocks"),
    ]
)


#########################
######### Rules #########
#########################

follow_mouse_focus = True
cursor_warp = False

auto_fullscreen = True
auto_minimize = False

bring_front_click = True

focus_on_window_activation = "smart"

reconfigure_screens = True

wmname = "Qtile"


#########################
####### Autostart #######
#########################

@ hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])
