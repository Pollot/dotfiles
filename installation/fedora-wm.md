# Table of contents
- [Installation](#installation)
    - [Packages](#packages)
    - [Dotfiles](#dotfiles)
    - [Final steps](#final-steps)
- [Post installation](#post-installation)

# Installation

### Packages
1. [RPM](https://packages.fedoraproject.org/):
```
sudo dnf install awesome zsh kitty sxhkd rofi neofetch flameshot polkit-gnome \
picom lxappearance gtk-murrine-engine dunst xss-lock i3lock qt5-qtstyleplugins \
network-manager-applet playerctl breeze-icon-theme
```

2. [Copr](https://copr.fedorainfracloud.org/):
```
sudo dnf copr enable frostyx/qtile

sudo dnf install qtile qtile-extras
```

3. [Starship](https://starship.rs/) (shell prompt):
```
curl -sS https://starship.rs/install.sh | sh
```

### Dotfiles
1. Clone this repository:
```
git clone https://github.com/Pollot/dotfiles
```

2. Install dotfiles:
```
cd dotfiles/installation

./install-fedora.sh
```

### Final steps
1. Reboot and start a chosen session.

2. Use nvidia-settings to change your displays configuration. Save changes to X configuration file to preserve them (requires root privileges):
```
sudo nvidia-settings
```

3. Change your GTK, icon and cursor theme using lxappearance.

4. Change font to **Open Sans** and set its size to **11**.

5. Change flatpak applications theme:
```
sudo flatpak override --filesystem=$HOME/.themes

sudo flatpak override --env=GTK_THEME=Catppuccin-Mocha-Standard-Mauve-Dark
```

# Post installation:

1. If you have multiple drives, configure fstab. You can do it using GUI application, for example: ```gnome-disks```.
