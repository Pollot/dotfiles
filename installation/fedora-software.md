# Table of contents
- [Recommended packages](#recommended-packages)
- [Gaming](#gaming)
- [Extras](#extras)
    - [WireGuard VPN](#wireguard-vpn)

# Recommended packages
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

flatpak install flathub com.discordapp.Discord org.signal.Signal
```
### Nemo
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

### lf
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

### Visual Studio Code
- [Official installation guide](https://code.visualstudio.com/docs/setup/linux)

### Bitwarden
- [Official download page](https://bitwarden.com/download/)

# Gaming
- [xone &darr;](#xone)
- [steam](https://store.steampowered.com/)<sup>RPM Fusion</sup>
- [lutris](https://packages.fedoraproject.org/pkgs/lutris/lutris/)
- [mangohud](https://packages.fedoraproject.org/pkgs/mangohud/mangohud/)

Installation:
```
sudo dnf install steam lutris mangohud
```

### xone
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
