### **These instructions may not be up-to-date. I don't use Arch anymore.**

# Table of contents
- [Basic configuration](#basic-configuration)
- [Installation](#installation)
    - [Packages](#packages)
    - [Dotfiles](#dotfiles)
    - [Final steps](#final-steps)
- [Post installation](#post-installation)
- [Additional software](arch-software.md)

# Basic configuration
1. Install Arch using the [official installation guide](https://wiki.archlinux.org/title/installation_guide).

2. Enable multilib repository (required for 32-bit software and libraries on 64-bit installs). Uncomment the ```[multilib]``` section in ```/etc/pacman.conf```:
```
[multilib]
Include = /etc/pacman.d/mirrorlist
```

3. Uncomment the following line in ```/etc/sudoers``` to allow members of the wheel group to use sudo:
```
%wheel ALL=(ALL:ALL) ALL
```

4. Create a user and add it to the wheel group:
```
useradd -mG wheel [username]
```

5. Set user's password:
```
passwd [username]
```

6. Log out from the root account and log into the newly created one.

# Installation

### Packages
1. Update system:
```
sudo pacman -Syu
```

2. Install base-devel package if you haven't already:
```
sudo pacman -S --needed base-devel
```

3. Install audio server:
```
sudo pacman -S pipewire lib32-pipewire pipewire-alsa pipewire-pulse \
pipewire-jack lib32-pipewire-jack wireplumber
```

4. Install basic packages:
```
sudo pacman -S xorg-server xorg-xinit git awesome zsh kitty sxhkd starship firefox rofi neofetch \
alsa-utils flameshot gnome-keyring polkit-gnome lxappearance dunst pacman-contrib xss-lock \
i3lock gnome-clocks gnome-weather gnome-calendar network-manager-applet
```

5. Install AUR helper *yay* :
```
git clone https://aur.archlinux.org/yay

cd yay

makepkg -si

cd
```

6. Install AUR packages:
```
yay -S qtile-git qtile-extras-git picom-git qt5-styleplugins
```

7. Install drivers. On Nvidia graphics card follow [this guide](https://wiki.archlinux.org/title/NVIDIA). **For the Maxwell (NV110/GMXXX) series and newer:**
```
sudo pacman -S nvidia nvidia-settings lib32-nvidia-utils
```

### Dotfiles
1. Clone this repository:
```
git clone https://github.com/Pollot/dotfiles
```

2. Install dotfiles:
```
cd dotfiles/installation

./install.sh
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

sudo flatpak override --filesystem=$HOME/.icons

sudo flatpak override --env=GTK_THEME=Catppuccin-Mocha-Standard-Mauve-Dark
```

# Post installation
1. Change X11 keyboard layout. You can add the following line in the ```~/.config/X11/xinitrc-[]```:
```
setxkbmap [your layout] &
```

2. Install and enable [reflector](https://wiki.archlinux.org/title/reflector):
```
sudo pacman -S reflector

sudo systemctl enable reflector
```
Reflector service parameters are specified in ```/etc/xdg/reflector/reflector.conf```. Customize it to your preference.

3. Enable automatic unlocking gnome-keyring on login. Edit ```/etc/pam.d/login``` with root priviligies and add the following lines ([full guide](https://wiki.archlinux.org/title/GNOME/Keyring)):
```
auth       optional     pam_gnome_keyring.so

session    optional     pam_gnome_keyring.so auto_start

password   optional     pam_gnome_keyring.so
```

4. Configure your printer. Install required packages:
```
sudo pacman -S cups system-config-printer

sudo systemctl enable cups
```
Then open printer configuration software and add your printer.

# [Additional software](arch-software.md)
