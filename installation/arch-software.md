# Table of contents
- [Recommended packages](#recommended-packages)
- [Gaming](#gaming)
- [Extras](#extras)
    - [WireGuard VPN](#wireguard-vpn)

# Recommended packages
- GUI file manager: [nemo &darr;](#nemo)
- Flatpak: [flatpak](https://flatpak.org/setup/Arch)
- Disk utility: [gnome-disk-utility](https://archlinux.org/packages/extra/x86_64/gnome-disk-utility/)
- TUI file manager: [lf](https://archlinux.org/packages/community/x86_64/lf/)
- Github cli tool: [github-cli](https://archlinux.org/packages/community/x86_64/github-cli/)
- Communication: [discord](https://wiki.archlinux.org/title/Discord), [signal-desktop](https://archlinux.org/packages/community/x86_64/signal-desktop/)
- Office suite: [libreoffice-fresh](https://wiki.archlinux.org/title/LibreOffice)
- Process viewer: [htop](https://archlinux.org/packages/extra/x86_64/htop/)
- Audio control: [pavucontrol](https://archlinux.org/packages/extra/x86_64/pavucontrol/)
- Graphic design: [gimp](https://wiki.archlinux.org/title/GIMP)
- Simplified man pages: [tldr](https://archlinux.org/packages/community/any/tldr/)
- Nvidia VA-API driver: [libva-nvidia-driver](https://aur.archlinux.org/packages/libva-nvidia-driver)<sup>AUR</sup>
- Text/Code editor: [visual-studio-code-bin](https://aur.archlinux.org/packages/visual-studio-code-bin)<sup>AUR</sup>

Installation:
```
sudo pacman -S flatpak gnome-disk-utility lf github-cli discord \
signal-desktop libreoffice-fresh htop pavucontrol gimp tldr

yay -S libva-nvidia-driver visual-studio-code-bin
```

### Nemo
- [Package](https://archlinux.org/packages/community/x86_64/nemo/)

1. Install Nemo and chosen extensions:
```
sudo pacman -S nemo nemo-fileroller
```

2. Set Nemo as default file browser:
```
xdg-mime default nemo.desktop inode/directory application/x-gnome-saved-search
```

3. Change the default terminal emulator to kitty:
```
gsettings set org.cinnamon.desktop.default-applications.terminal exec kitty
```

# Gaming
- [steam](https://wiki.archlinux.org/title/steam)
- [lutris](https://archlinux.org/packages/community/any/lutris/)
- [xone-dkms](https://aur.archlinux.org/packages/xone-dkms)<sup>AUR</sup> (requires [linux-headers](https://archlinux.org/packages/core/x86_64/linux-headers/))

Installation:
```
sudo pacman -S steam lutris linux-headers

yay -S xone-dkms
```

Lutris wine dependencies:
```
sudo pacman -S --needed wine-staging giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls \
mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error \
lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo \
sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama \
ncurses lib32-ncurses ocl-icd lib32-ocl-icd libxslt lib32-libxslt libva lib32-libva gtk3 \
lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader
```

# Extras

### WireGuard VPN
1. Download configuration file from your VPN service provider.

2. Rename it to ```wg.conf``` - interface name will be set to the file name.

3. Add it to the Network Manager using the following command:
```
sudo nmcli connection import type wireguard file [path]/wg.conf
```

4. Use ```nm-connection-editor``` to change its settings (e.g. name, auto-connection).
