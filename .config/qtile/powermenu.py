from libqtile.lazy import lazy

from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupImage,
    PopupText
)

from colours import *


def show_power_menu(qtile):

    controls = [
        PopupImage(
            filename="~/.config/qtile/icons/shutdown.png",
            pos_x=0.15,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            highlight_method='border',
            highlight=text,
            mouse_callbacks={
                "Button1": lazy.spawn("shutdown now")
            }
        ),
        PopupImage(
            filename="~/.config/qtile/icons/logout.png",
            pos_x=0.45,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            highlight_method='border',
            highlight=text,
            mouse_callbacks={
                "Button1": lazy.shutdown()
            }
        ),
        PopupImage(
            filename="~/.config/qtile/icons/reboot.png",
            pos_x=0.75,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            highlight_method='border',
            highlight=text,
            mouse_callbacks={
                "Button1": lazy.spawn("reboot")
            }
        ),
        PopupText(
            text="Shutdown",
            pos_x=0.1,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Logout",
            pos_x=0.396,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Reboot",
            pos_x=0.7,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=600,
        height=150,
        controls=controls,
        background=mantle,
        initial_focus=0,
    )

    layout.show(centered=True)
