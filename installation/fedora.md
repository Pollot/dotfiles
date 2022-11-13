# Table of contents
- [Installation](#installation)
    - [Basic configuration](#basic-configuration)
    - [Packages](#packages)

# Installation
Install Fedora (I recommend sticking to the workstation edition) using an iso from the [official website](https://getfedora.org/). Remember to update your system after installation.

### Basic configuration
1. Configure DNF. Edit ```/etc/dnf/dnf.conf``` with root privileges. I recommend adding the parameters:
```
fastestmirror=True
max_parallel_downloads=10
```
You can read about full configuration options in the [DNF docs](https://dnf.readthedocs.io/en/latest/conf_ref.html).

2. Enable [RPM Fusion repositories](https://rpmfusion.org/RPM%20Fusion) and install multimedia packages using the [official configuration guide](https://rpmfusion.org/Configuration).

3. [Enable flatpak](https://flatpak.org/setup/Fedora).

4. Install drivers. For Nvidia graphics card follow [this guide](https://rpmfusion.org/Howto/NVIDIA).

5. [Configure Xorg as the default GNOME session](https://docs.fedoraproject.org/en-US/quick-docs/configuring-xorg-as-default-gnome-session/) if you don't use and plan to use Wayland.

6. Change GDM monitors configuration if it's wrong ([forum post](https://ask.fedoraproject.org/t/login-screen-on-wrong-monitor/4242/3)):
```
sudo cp ~/.config/monitors.xml /var/lib/gdm/.config/ 
```

### Packages