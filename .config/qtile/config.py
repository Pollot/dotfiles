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
terminal = "kitty"
browser = "firefox"
menu = "rofi -show drun"
audio = "alsamixer"

location = "Warsaw"
weather = "firefox https://www.yr.no/en/forecast/daily-table/2-756135/Poland/Mazovia/Warszawa/Warsaw"
clock = "firefox https://www.timeanddate.com/worldclock/"

gap_size = 6

font_default = "sans"
font_nerd = "FiraCode Nerd Font Mono"
font_weather = "Weather Icons"

wlp1 = "~/Wallpapers/hashtags-black.png"
wlp2 = "~/Wallpapers/arch-black.png"

# OpenWeatherMap API key
owm_api = "9f48fca94a15edcd4705c0ae0a92895a"

##########################
######## Colours #########
##########################

# Source: https://github.com/catppuccin/catppuccin

rosewater = "#f5e0dc"
flamingo = "#f2cdcd"
pink = "#f5c2e7"
mauve = "#cba6f7"
red = "#f38ba8"
maroon = "#eba0ac"
peach = "#fab387"
yellow = "#f9e2af"
green = "#a6e3a1"
teal = "#94e2d5"
sky = "#89dceb"
sapphire = "#74c7ec"
blue = "#89b4fa"
lavender = "#b4befe"
text = "#cdd6f4"
subtext1 = "#bac2de"
subtext0 = "#a6adc8"
overlay2 = "#9399b2"
overlay1 = "#7f849c"
overlay0 = "#6c7086"
surface2 = "#585b70"
surface1 = "#45475a"
surface0 = "#313244"
base = "#1e1e2e"
mantle = "#181825"
crust = "#11111b"


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
    # Layouts
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
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
        desc="Move focus to the next monitor"
        ),
    Key([mod], "comma",
        lazy.prev_screen(),
        desc="Move focus to the prev monitor"
        ),
    # Switch between windows
    Key([mod], "j",
        # lazy.layout.previous(),
        lazy.group.prev_window(),
        desc="Move focus to the previous window"
        ),
    Key([mod], "k",
        # lazy.layout.next(),
        lazy.group.next_window(),
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
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window left"
        ),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window right"
        ),
    # Window controls
    Key([mod], "h",
        lazy.layout.shrink_main(),
        desc="Shrink master pane"
        ),
    Key([mod], "l",
        lazy.layout.grow_main(),
        desc="Expand master pane"
        ),
    Key([mod], "m",
        lazy.window.toggle_maximize(),
        desc="Toggle window maximize"
        ),
    Key([mod], "n",
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


##########################
######### Groups #########
##########################

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
                desc="Switch to & move focused window to group {}".format(
                    i.name),
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
    "margin": gap_size,
    "border_focus": blue,
    "border_normal": base,
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme),
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


#########################
######## Widgets ########
#########################

# Decorations
arrow_right = {
    "decorations": [PowerLineDecoration(path="arrow_right")]
}

arrow_left = {
    "decorations": [PowerLineDecoration(path="arrow_left")]
}

rounded_right = {
    "decorations": [PowerLineDecoration(path="rounded_right")]
}

rounded_left = {
    "decorations": [PowerLineDecoration(path="rounded_left")]
}

slash_back = {
    "decorations": [PowerLineDecoration(path="back_slash")]
}

slash_forward = {
    "decorations": [PowerLineDecoration(path="forward_slash")]
}

border = {
    "decorations": [RectDecoration(
        colour=mauve,
        radius=10,
        filled=True,
        padding_y=4,
        group=True
    )]
}


widget_defaults = dict(
    font=font_default,
    fontsize=12,
    padding=8,
    background=base,
    foreground=text,
)

extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.Spacer(
            background=crust,
            length=3,
        ),
        widget.CurrentScreen(
            background=crust,
            active_color=blue,
            inactive_color=overlay0,
            active_text="",
            inactive_text="",
            font=font_nerd,
            fontsize=40,
            **rounded_right,
        ),
        widget.CurrentLayoutIcon(
            background=mantle,
            use_mask=True,
            foreground=blue,
            padding=0,
            scale=0.6,
        ),
        widget.Spacer(
            background=mantle,
            length=12,
        ),
        widget.GroupBox(
            background=mantle,
            disable_drag=True,
            fontsize=24,
            font=font_nerd,
            highlight_method="line",
            active=text,
            inactive=overlay0,
            block_highlight_text_color=blue,
            highlight_color=[mantle, mantle],
            other_current_screen_border=overlay0,
            other_screen_border=overlay0,
            this_current_screen_border=blue,
            this_screen_border=blue,
            **rounded_left,
        ),
        widget.TaskList(
            border=blue,
            unfocused_border=overlay0,
            padding=6,
            icon_size=16,
            txt_floating="[Floating] ",
            txt_maximized="[Maximized] ",
            txt_minimized="[Minimized] ",
        ),
        widget.Systray(
        ),
        widget.Spacer(
            length=10,
        ),
        widget.Spacer(
            length=10,
            **border,
        ),
        widget.TextBox(
            foreground=crust,
            text="墳 ",
            font=font_nerd,
            fontsize=14,
            padding=0,
            mouse_callbacks={"Button3": lazy.spawn(terminal + " -e " + audio)},
            **border,
        ),
        widget.Volume(
            padding=0,
            volume_app=terminal + " -e " + audio,
            foreground=crust,
            **border,
        ),
        widget.Spacer(
            length=10,
            **border,
        ),
        widget.Spacer(
            length=10,
            **rounded_right,
        ),
        widget.NvidiaSensors(
            background=blue,
            foreground=crust,
            padding=0,
            format="GPU: {temp}°C",
        ),
        widget.Spacer(
            background=blue,
            length=8,
            **slash_forward,
        ),
        widget.CPU(
            background=green,
            foreground=crust,
            width=80,
            format="CPU: {load_percent}%",
        ),
        widget.Memory(
            background=green,
            foreground=crust,
            padding=0,
            width=78,
            format="MEM: {MemPercent}%",
            **slash_forward,
        ),
        widget.Net(
            background=yellow,
            foreground=crust,
            padding=4,
            width=55,
            interface="eno1",
            format="{down}",
        ),
        widget.TextBox(
            background=yellow,
            foreground=crust,
            padding=0,
            text="",
            font=font_nerd,
        ),
        widget.Spacer(
            background=yellow,
            length=10,
        ),
        widget.Net(
            background=yellow,
            foreground=crust,
            interface="eno1",
            format="{up}",
            padding=4,
            width=55,
        ),
        widget.TextBox(
            text="祝",
            font=font_nerd,
            padding=0,
            background=yellow,
            foreground=crust,
        ),
        widget.Spacer(
            background=yellow,
            length=8,
            **slash_forward,
        ),
        widget.OpenWeather(
            background=peach,
            foreground=crust,
            location=location,
            format="{icon} {main_temp: .0f}°{units_temperature}",
            font=font_weather,
            app_key=owm_api,
            mouse_callbacks={"Button1": lazy.spawn(weather)},
            **slash_forward,
        ),
        widget.Clock(
            format="%A, %d %B - %H:%M:%S",
            background=red,
            foreground=crust,
            mouse_callbacks={"Button1": lazy.spawn(clock)},
        ),
    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[6]  # removing systray
    return widgets_screen2


screens = [
    Screen(
        wallpaper=wlp1,
        wallpaper_mode="fill",
        top=bar.Bar(
            init_widgets_screen1(),
            32,
            margin=[gap_size, gap_size, 0, gap_size],
        )
    ),
    Screen(
        wallpaper=wlp2,
        wallpaper_mode="fill",
        top=bar.Bar(
            init_widgets_screen2(),
            32,
            margin=[gap_size, gap_size, 0, gap_size],
        ),
    ),
]


##########################
######## Floating ########
##########################

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=blue,
    border_normal=base,
    border_width=2,
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


wmname = "Qtile"
