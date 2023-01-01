# Table of contents
- [Basic configuration](#basic-configuration)
- [Video drivers with secure boot](#video-drivers-with-secure-boot)
- [Installation for window managers](fedora-wm.md)
- [Installation for GNOME](fedora-gnome.md)
- [Optional software](#optional-software)
    - [Recommended packages](#recommended-packages)
    - [Gaming](#gaming)
- [Extras](#extras)

# Basic configuration
1. Install Fedora using an iso from the [official website](https://getfedora.org/).

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

# [Installation for window managers](fedora-wm.md)

# [Installation for GNOME](fedora-gnome.md)

# Optional software

### Recommended packages
- GUI file manager: [nemo &darr;](#nemo)
- TUI file manager: [lf &darr;](#lf)
- Text/Code editor: [Visual Studio Code &darr;](#visual-studio-code)
- Password manager: [Bitwarden &darr;](#bitwarden)
- Process viewer: [htop](https://packages.fedoraproject.org/pkgs/htop/htop/)
- Audio control: [pavucontrol](https://packages.fedoraproject.org/pkgs/pavucontrol/pavucontrol/)
- Graphic design: [gimp](https://packages.fedoraproject.org/pkgs/gimp/gimp/)
- Simplified man pages: [tldr](https://packages.fedoraproject.org/pkgs/tldr/tldr/)
- GitHub cli tool: [gh](https://packages.fedoraproject.org/pkgs/gh/gh/)
- Communication: [Discord](https://flathub.org/apps/details/com.discordapp.Discord)<sup>Flatpak</sup>, [Signal](https://flathub.org/apps/details/org.signal.Signal)<sup>Flatpak</sup>

Installation:
```
sudo dnf install htop pavucontrol gimp tldr gh

flatpak install com.discordapp.Discord flathub org.signal.Signal
```
#### Nemo
- [Package](https://packages.fedoraproject.org/pkgs/nemo/nemo/)

1. Install Nemo and chosen extensions:
```
sudo dnf install nemo nemo-fileroller
```

2. Set Nemo as default file browser:
```
xdg-mime default nemo.desktop inode/directory application/x-gnome-saved-search
```

3. Change the default terminal emulator to kitty:
```
gsettings set org.cinnamon.desktop.default-applications.terminal exec kitty
```

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

#### Visual Studio Code
- [Official installation guide](https://code.visualstudio.com/docs/setup/linux)

#### Bitwarden
- [Official download page](https://bitwarden.com/download/)

### Gaming
- [xone &darr;](#xone)
- [steam](https://store.steampowered.com/)<sup>RPM Fusion</sup>
- [lutris](https://packages.fedoraproject.org/pkgs/lutris/lutris/)
- [mangohud](https://packages.fedoraproject.org/pkgs/mangohud/mangohud/)

Installation:
```
sudo dnf install steam lutris mangohud
```

#### xone
- [GitHub repository with installation guide](https://github.com/medusalix/xone)

# Extras

### WireGuard VPN

1. Download configuration file from your VPN service provider.

2. Rename it to ```wg.conf``` - interface name will be set to the file name.

3. Add it to the Network Manager using the following command:
```
sudo nmcli connection import type wireguard file [path]/wg.conf
```

4. Use ```nm-connection-editor``` to change its settings (e.g. name, auto-connection).