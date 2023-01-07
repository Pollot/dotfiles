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
1. Install *Fedora Workstation* or *chosen spin* using an iso from the [official website](https://getfedora.org/) or [spins website](https://spins.fedoraproject.org/).

2. Update system and reboot.

3. Change your DE settings to your liking.

4. Remove software you won't use.

5. Configure DNF. Edit ```/etc/dnf/dnf.conf``` with root privileges. I recommend adding the following parameters:
```
fastestmirror=True
max_parallel_downloads=10
```
You can read about full configuration options in the [DNF docs](https://dnf.readthedocs.io/en/latest/conf_ref.html).

6. [Enable Flatpak](https://flatpak.org/setup/Fedora). If you use GUI package/software manager (e.g.: ```gnome-software```, ```plasma-discover```), enable it in software repositories as well.

7. [Enable RPM Fusion repositories](https://rpmfusion.org/Configuration).

8. [Install multimedia packages](https://rpmfusion.org/Howto/Multimedia).

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

9. Replace display manager monitors configuration with yours:
- GDM:
```
sudo cp ~/.config/monitors.xml /var/lib/gdm/.config/ 
```
- SDDM:
    1. Edit ```/etc/sddm/Xsetup``` with root privileges. Use xrandr to set up monitors.
    2. Uncomment ```DisplayCommand=/etc/sddm/Xsetup``` in ```/etc/sddm.conf```.

10. **If you don't use and plan to use Wayland**, you can force GDM to use X11 instead. Open ```/etc/gdm/custom.conf``` with root privileges and uncomment the following line:
```
WaylandEnable=false
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

sudo flatpak override --env=GTK_THEME=Catppuccin-Mocha-Standard-Mauve-Dark
```

# Post installation:
If you have multiple drives, configure fstab. You can do it using GUI application, for example: ```gnome-disks``` or ```kde-partitionmanager```.

# [Additional software](fedora-software.md)
