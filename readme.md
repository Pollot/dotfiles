# Screenshots
<img src="screenshots/update.jpg">

# Table of Contents
- [List of software](#list-of-software)
    - [Qtile](#qtile)
    - [Catppuccin](#catppuccin)
    - [Wallpapers](#wallpapers)
    - [Picom](#picom)
    - [Zsh](#zsh)
    - [Rofi](#rofi)
    - [Nerd Font](#nerd-font)
    - [Grub](#grub)
- [Installation](#installation)

# List of software
- Window manager: [Qtile](#qtile)
- Colour scheme: [Catppuccin](#catppuccin)
- Wallpapers: [Catppuccin](#wallpapers)
- GTK theme: [Catppuccin](https://github.com/catppuccin/gtk)
- Cursor theme: [Volantes](https://www.gnome-look.org/p/1356095)
- Compositor: [Picom](#picom)
- Shell: [Zsh](#zsh)
- Terminal: [Kitty](https://sw.kovidgoyal.net/kitty/)
- Prompt: [Starship](https://starship.rs/)
- Launcher: [Rofi](#rofi)
- Fetch: [Neofetch](https://github.com/dylanaraps/neofetch)
- Notifications: [Dunst](https://dunst-project.org/)
- Nerd Font: [Fira Code](#nerd-font)
- Bootloader: [Grub](#grub)

## Catppuccin
Catppuccin is a community-driven pastel theme that aims to be the middle ground between low and high contrast themes. It consists of 4 soothing warm palettes with 26 eye-candy colors each, perfect for coding, designing, and much more!
- [Official repository](https://github.com/catppuccin/catppuccin)
- [Project's documentation](https://github.com/catppuccin/catppuccin/tree/dev/docs)

I use **Catppuccin Mocha** palette in my configurations.
## Qtile
#### Information:
- [Official website](http://www.qtile.org/)
- [Qtile documentation](http://docs.qtile.org/en/stable/)
- [Qtile extras documentation](https://qtile-extras.readthedocs.io/en/stable/index.html)
#### Dependencies:
- [Qtile extras](https://qtile-extras.readthedocs.io/en/stable/manual/install.html)
- [Psutil](https://pypi.org/project/psutil/)
- [Nerd font](#nerd-font)
- [Open Sans font](https://fonts.google.com/specimen/Open+Sans)

## Wallpapers
[Official repository](https://github.com/catppuccin/wallpapers). Wallpapers I use:
- Modified version (gimp file included) of [unicat](https://github.com/catppuccin/wallpapers/blob/main/minimalistic/black5_unicat.png) by [Pocco81](https://github.com/Pocco81)
- [Flatppuccin](https://github.com/catppuccin/wallpapers/blob/main/flatppuccin/flatppuccin_4k_macchiato.png) by [Adal Zanabria](https://github.com/AdalZanabria)

## Picom
There are a lot of Picom forks, but I decided to stick to the main one (made by [yshui](https://github.com/yshui)). However, the latest version is required. The easiest way to install it is by using the [AUR](https://aur.archlinux.org/).
- [Official repository](https://github.com/yshui/picom)
- [AUR package](https://aur.archlinux.org/packages/picom-git)

## Zsh
[Official website](https://www.zsh.org/). Plugins I use:
- [Autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
- [Syntax highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)
- [Directory history](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/dirhistory)
- [Sudo](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/sudo)

## Rofi
I'm **not** an author of the Rofi config included in this repository. It's: [Catppuccin for Rofi - Siduck's Theme](https://github.com/catppuccin/rofi/tree/main/basic).

## Nerd Font
I use **Fira Code Nerd Font Mono**. You can download its latest release from: [Nerd Fonts website](https://www.nerdfonts.com/font-downloads).

**<p align="center">Remember to install the mono variant of chosen Nerd Font. Icons are not centered in the regular version.</p>**

## Grub
**Not included in my repository**. I use: [Catppuccin for Grub](https://github.com/catppuccin/grub).

# Installation

### Basic configuration
1. Install Arch using the [official installation guide](https://wiki.archlinux.org/title/installation_guide).

2. Create a user and add it to the wheel group:
```
useradd -mG wheel [username]
```

3. Uncomment the following line in ```/etc/sudoers``` to allow members of the wheel group to use sudo:
```
%wheel ALL=(ALL:ALL) ALL
```

4. Set user's password:
```
passwd [username]
```

5. Log out from the root account and log into the newly created one.

6. Enable multilib repository (required for 32-bit software and libraries on 64-bit installs). Uncomment the [multilib] section in ```/etc/pacman.conf```:
```
[multilib]
Include = /etc/pacman.d/mirrorlist
```

### Packages
1. Update system:
```
sudo pacman -Syu
```

2. Install base-devel package if you haven't already:
```
sudo pacman -S --needed base-devel
```

3. Install basic packages:
```
sudo pacman -S xorg-server xorg-xinit qtile git zsh kitty starship firefox rofi \
neofetch alsa-utils flameshot htop gnome-keyring lxsession-gtk3 lxappearance \
dunst
```

4. Install AUR helper *yay* :
```
git clone https://aur.archlinux.org/yay
cd yay
makepkg -si
cd
```

5. Install AUR packages (don't remove qtile-extras build dependencies):
```
yay -S qtile-extras-git picom-git catppuccin-gtk-theme-mocha
```

6. Install psutil:
```
pip install psutil
```

7. Install drivers. On Nvidia graphic's card follow [this guide](https://wiki.archlinux.org/title/NVIDIA). **For the Maxwell (NV110/GMXXX) series and newer:**
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

### Finishing

1. Reboot:
```
sudo reboot
```

2. X server session should automatically start up after logging in.

3. Use lxappearance to change your GTK and cursor theme.

4. Use nvidia-settings to change your displays configuration.

5. Configure audio - for example install PipeWire:
```
sudo pacman -S pipewire lib32-pipewire pipewire-alsa \
pipewire-pulse pipewire-jack lib32-pipewire-jack
```

### Optional
1. Enable automatic unlocking gnome-keyring on login. Edit ```/etc/pam.d/login``` with root priviligies and add the following lines [full guide](https://wiki.archlinux.org/title/GNOME/Keyring):
```
auth       optional     pam_gnome_keyring.so

session    optional     pam_gnome_keyring.so auto_start

password   optional     pam_gnome_keyring.so
```

<h3 align="center">Enjoy</h3>