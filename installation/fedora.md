# Table of contents
- [Installation](#installation)
    - [Basic configuration](#basic-configuration)
    - [Packages](#packages)
    - [Dotfiles](#dotfiles)
    - [Final steps](#final-steps)
- [Post installation](#post-installation)
- [Optional software](#optional-software)
    - [Recommended packages](#recommended-packages)
        - [Visual Studio Code](#visual-studio-code)
        - [lf](#lf)
    - [Gaming](#gaming)
        - [xone](#xone)

# Installation
Install Fedora using an iso from the [official website](https://getfedora.org/). **Remember to update your system after installation.**

### Basic configuration
1. Configure DNF. Edit ```/etc/dnf/dnf.conf``` with root privileges. I recommend adding the following parameters:
```
fastestmirror=True
max_parallel_downloads=10
```
You can read about full configuration options in the [DNF docs](https://dnf.readthedocs.io/en/latest/conf_ref.html).

2. [Enable RPM Fusion repositories](https://rpmfusion.org/Configuration).

3. [Install multimedia packages](https://rpmfusion.org/Howto/Multimedia).

4. [Enable Flatpak](https://flatpak.org/setup/Fedora).

5. Install drivers. For Nvidia graphics card follow [this guide](https://rpmfusion.org/Howto/NVIDIA).

6. Configure Xorg as the default GDM display server if you don't use and plan to use Wayland. Open ```/etc/gdm/custom.conf``` and uncomment the following line:
```
WaylandEnable=false
```

7. Change GDM monitors configuration if it's wrong:
```
sudo cp ~/.config/monitors.xml /var/lib/gdm/.config/ 
```

### Packages
1. [RPM](https://packages.fedoraproject.org/):
```
sudo dnf install zsh kitty rofi neofetch pavucontrol flameshot htop polkit-gnome \
lxappearance dunst xss-lock i3lock
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
1. Reboot and start a Qtile session.

2. Use nvidia-settings to change your displays configuration. Save changes to X configuration file to preserve them (requires root privileges):
```
sudo nvidia-settings
```

3. Use lxappearance to change your GTK and cursor theme.

# Post installation:
Enable automatic unlocking gnome-keyring on login. Edit ```/etc/pam.d/login``` with root priviligies and add the following lines ([full guide](https://wiki.archlinux.org/title/GNOME/Keyring)):
```
auth       optional     pam_gnome_keyring.so

session    optional     pam_gnome_keyring.so auto_start

password   optional     pam_gnome_keyring.so
```

# Optional software

### Recommended packages
- GUI file manager: [nemo](https://packages.fedoraproject.org/pkgs/nemo/nemo/), [nemo-fileroller](https://packages.fedoraproject.org/pkgs/nemo-extensions/nemo-fileroller/)
- TUI file manager: [lf ﰬ](#lf)
- Text/Code editor: [Visual Studio Code ﰬ](#visual-studio-code)
- Password manager: [keepassxc](https://packages.fedoraproject.org/pkgs/keepassxc/keepassxc/)
- Communication: [Discord](https://flathub.org/apps/details/com.discordapp.Discord)<sup>Flatpak</sup>, [Signal](https://flathub.org/apps/details/org.signal.Signal)<sup>Flatpak</sup>
- Graphic design: [gimp](https://packages.fedoraproject.org/pkgs/gimp/gimp/)
- Video editing: [kdenlive](https://kdenlive.org/en/)<sup>RPM Fusion</sup>

Installation:
```
sudo dnf install nemo nemo-fileroller keepassxc gimp kdenlive

flatpak install flathub com.discordapp.Discord org.signal.Signal
```

#### Visual Studio Code
- [Official installation guide](https://code.visualstudio.com/docs/setup/linux)

#### lf
1. Dowload  ```lf-linux-amd64.tar.gz``` (if you have amd64 CPU) from [releases page](https://github.com/gokcehan/lf/releases).

2. Extract archive:
```
cd Downloads

tar xf lf-linux-amd64.tar.gz
```

3. Move the executable to the binaries path:
```
sudo mv lf /usr/local/bin
```

### Gaming
- [steam](https://store.steampowered.com/)<sup>RPM Fusion</sup>
- [lutris](https://packages.fedoraproject.org/pkgs/lutris/lutris/)
- [ProtonUp-Qt](https://flathub.org/apps/details/net.davidotek.pupgui2)<sup>Flatpak</sup>
- [xone ﰬ](#xone)

Installation:
```
sudo dnf install steam lutris

flatpak install flathub net.davidotek.pupgui2
```

#### xone
- [GitHub repository with installation guide](https://github.com/medusalix/xone)