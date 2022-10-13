# linux-profile

![GitHub Org's stars](https://img.shields.io/github/stars/MyLinuxProfile?label=LinuxProfile&style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/MyLinuxProfile/linux-profile-basic?style=flat-square)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/MyLinuxProfile/linux-profile?style=flat-square)
![PyPI](https://img.shields.io/pypi/v/linuxp)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/linuxp?style=flat-square)
![PyPI - Status](https://img.shields.io/pypi/status/linuxp?style=flat-square)
![PyPI - License](https://img.shields.io/pypi/l/linuxp)

# [Introduction](https://github.com/MyLinuxProfile/linux-profile/wiki)
Linux Profile is a Linux profile management tool. With this project it is possible, from commands executed in the console, to create a 'json' file to store backup configurations. such as information about installed packages, alias, terminal settings. It also allows with a single command to restore saved configurations.

## [Quick Install](https://github.com/MyLinuxProfile/linux-profile/wiki/Installation#quick-install)

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/MyLinuxProfile/linux-profile/master/scripts/install.sh)"

<hr>

## [Getting Started](https://github.com/MyLinuxProfile/linux-profile/wiki/Installation#getting-started)

`linux_profile` installation involves:

### 1. Installing dependencies

| Package Manager    | Command                   |
| :----------------: | :-----------------------: |
| Aptitude	         | `apt install curl git`    |
| DNF	             | `dnf install curl git`    |
| Pacman	         | `pacman -S curl git`      |
| Zypper	         | `zypper install curl git` |


### 2. Downloading linux_profile core

| Method             | Command                                                                                      |
| :----------------: | :------------------------------------------------------------------------------------------: |
| Git   	         | `git clone https://github.com/MyLinuxProfile/linux-profile.git ~/linuxp --branch master` |


### 3. Installing linux_profile
  Add the following to ~/.bashrc:

    export PATH=$PATH":$HOME/linuxp"

<hr>

# [Wiki Page](https://github.com/MyLinuxProfile/linux-profile/wiki)

## Commands:

| #      | Command               | Description                                                                              | Wiki page                    |
|--------|:----------------------|:-----------------------------------------------------------------------------------------| :--------------------------: | 
| 01     | ``linuxp init``       | Initial configuration of profile files and server connection.                            | [Command Init](https://github.com/MyLinuxProfile/linux-profile/wiki/Command---Init) |
| 02     | ``linuxp add``        | Parameter used to add a new item to the list in your profile file.                       | [Command Add](https://github.com/MyLinuxProfile/linux-profile/wiki/Command--Add) |
| 03     | ``linuxp install``    | This parameter is used to install the modules, **package**, **alias** and **script**.    | [Command Install](https://github.com/MyLinuxProfile/linux-profile/wiki/Command-Install) |
| 04     | ``linuxp uninstall``  | Command used to uninstall items. Be **very careful** when running.                       | [Command Uninstall](https://github.com/MyLinuxProfile/linux-profile/wiki/Command--Uninstall) |
| 05     | ``linuxp list``       | Lists all modules in the terminal and can also apply filters to find items.              | [Command List](https://github.com/MyLinuxProfile/linux-profile/wiki/Command-List) |

## Options:
  
### MODULE
  
| Example            |                     | Wiki page      |
| :----------------: | :-----------------: | :------------: |
| ``package``	     | * [ Fixed argument] | [Module](https://github.com/MyLinuxProfile/linux-profile/wiki/Options#module) |
| ``alias``	         | * [ Fixed argument] | [Module](https://github.com/MyLinuxProfile/linux-profile/wiki/Options#module) |
| ``script``	     | * [ Fixed argument] | [Module](https://github.com/MyLinuxProfile/linux-profile/wiki/Options#module) |

### TAG

| Example            |                       | Wiki page      |
| :----------------: | :-------------------: | :------------: |
| ``whatever``	     | [ Any text argument ] | [Tag](https://github.com/MyLinuxProfile/linux-profile/wiki/Options#tag) |

### VALUE

| Example            |                       | Wiki page      |
| :----------------: | :-------------------: | :------------: |
| ``whatever``	     | [ Any text argument ] | [Value](https://github.com/MyLinuxProfile/linux-profile/wiki/Options#value) |

## [Make a profile backup](https://github.com/MyLinuxProfile/linux-profile/wiki/Make-a-profile-backup)

- Saving the profile file:

      cat ~/linuxp/.config/linux_profile.json > ~/backup_profile.json

- Open in a text editor:

      xdg-open ~/backup_profile.json
        
- Open in Google Chrome browser:

      google-chrome ~/backup_profile.json
        
- Open in Firefox browser:

      firefox ~/backup_profile.json

- Open vi text editor:

      vi ~/backup_profile.json

## Profile File 

- Link - [linux_profile.json](https://github.com/MyLinuxProfile/linux-profile/blob/master/docs/linux_profile.json)

## Commit Style
- ⚙️ NO-TASK
- 📝 PEP8
- 📌 ISSUE
- 🪲 BUG
- 📘 DOCS
- 📦 PyPI

**RESOURCES**
- GitHub: https://github.com/MyLinuxProfile/linux-profile-basic
- Docs:   https://linuxprofile.com
