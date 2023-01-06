# Table of contents
- [Basic configuration](#basic-configuration)
- [Video drivers with secure boot](#video-drivers-with-secure-boot)
- [Installation](#installation)
    - [Packages](#packages)
    - [Dotfiles](#dotfiles)
    - [Final steps](#final-steps)
- [Post installation](#post-installation)
- [Additional software](fedora-software.md)

# Basic configuration
1. Install *Fedora Workstation* using an iso from the [official website](https://getfedora.org/).

2. Update system and reboot.

3. Change GNOME settings to your liking.

4. Remove software you won't use.

5. Configure DNF. Edit ```/etc/dnf/dnf.conf``` with root privileges. I recommend adding the following parameters:
```
fastestmirror=True
max_parallel_downloads=10
```
You can read about full configuration options in the [DNF docs](https://dnf.readthedocs.io/en/latest/conf_ref.html).

6. Configure Xorg as the default GDM display server if you don't use and plan to use Wayland. Open ```/etc/gdm/custom.conf``` and uncomment the following line:
```
WaylandEnable=false
```

7. [Enable Flatpak](https://flatpak.org/setup/Fedora). If you use ```gnome-software```, enable it in software repositories as well.

8. [Enable RPM Fusion repositories](https://rpmfusion.org/Configuration).

9. [Install multimedia packages](https://rpmfusion.org/Howto/Multimedia).

# Video drivers with secure boot
- [Guide i used for auto signing](https://blog.monosoul.dev/2022/05/17/automatically-sign-nvidia-kernel-module-in-fedora-36/)

1. Install the tools required for auto signing to work:
```
sudo dnf install kmodtool akmods mokutil openssl
```

2. Generate a signing key:
```
sudo kmodgenca -a
```

3. Initiate the key enrollment:
```
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```

4. Reboot.

5. You will see MOK Manager interface and will be asked to enroll the key:
    - First select “Enroll MOK“
    - Then “Continue“
    - Hit “Yes” and enter the password from step 3
    - Then select “Reboot”

6. Install NVIDIA drivers: [follow this guide](https://rpmfusion.org/Howto/NVIDIA).

7. Reboot.

8. Configure screens.

9. Replace GDM monitors configuration with yours:
```
sudo cp ~/.config/monitors.xml /var/lib/gdm/.config/ 
```

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
If you have multiple drives, configure fstab. You can do it using GUI application, for example: ```gnome-disks```.

# [Additional software](fedora-software.md)
