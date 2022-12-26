# Table of contents
- [Installation](#installation)
    - [Packages](#packages)
    - [Dotfiles](#dotfiles)
    - [Final steps](#final-steps)
- [Post installation](#post-installation)

# Installation

### Packages
1. [RPM](https://packages.fedoraproject.org/)
```
sudo dnf install gnome-tweaks zsh kitty neofetch gtk-murrine-engine qt5-qtstyleplugins
```

2. [Flatpak](https://flatpak.org/):
```
flatpak install flathub com.mattjakeman.ExtensionManager
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
1. Install chosen extensions. I recommend:
    - [User Themes](https://extensions.gnome.org/extension/19/user-themes/)
    - [AppIndicator and KStatusNotifierItem Support](https://extensions.gnome.org/extension/615/appindicator-support/)
    - [Blur my Shell](https://extensions.gnome.org/extension/3193/blur-my-shell/)
    - [Clipboard Indicator](https://extensions.gnome.org/extension/779/clipboard-indicator/)
 
2. Change your GTK3, shell and cursor theme using ```gnome-tweaks```.

3. Change flatpak applications theme:
```
sudo flatpak override --filesystem=$HOME/.themes

sudo flatpak override --env=GTK_THEME=Catppuccin-Mocha-Standard-Mauve-Dark
```

# Post installation:

1. If you have multiple drives, configure fstab using ```gnome-disks```.

2. Customize keyboard shortcuts in settings.
