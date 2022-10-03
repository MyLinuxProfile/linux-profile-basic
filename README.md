# linux-profile-basic

![GitHub Org's stars](https://img.shields.io/github/stars/MyLinuxProfile?label=LinuxProfile&style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/MyLinuxProfile/linux-profile-basic?style=flat-square)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/MyLinuxProfile/linux-profile?style=flat-square)

# Introduction
Linux Profile is a Linux profile management tool. With this project it is possible, from commands executed in the console, to create a 'json' file to store backup configurations. such as information about installed packages, alias, terminal settings. It also allows with a single command to restore saved configurations.

## Getting Started

`linux_profile` installation involves:

1 - Installing dependencies

2 - Downloading linux_profile core

3 - Installing linux_profile

<hr>

#### 1 - Installing dependencies

| Package Manager    | Command                   |
| :----------------: | :-----------------------: |
| Aptitude	         | `apt install curl git`    |
| DNF	             | `dnf install curl git`    |
| Pacman	         | `pacman -S curl git`      |
| Zypper	         | `zypper install curl git` |

#### 2 - Downloading linux_profile core
| Method             | Command                                                                                      |
| :----------------: | :------------------------------------------------------------------------------------------: |
| Git   	         | `git clone https://github.com/MyLinuxProfile/linux-profile-basic.git ~/linuxp --branch master` |

#### 3 - Installing linux_profile

<details>
  <summary>Bash & Git</summary>
    
  Add the following to ~/.bashrc:

    export PATH=$PATH":$HOME/linuxp"

</details>

## Commands

| #      | Command                    | Param         | Argument              | Param           | Argument      |
|--------|:---------------------------|:--------------|:----------------------| :---------------|:--------------|
| 01     | ``linux_profile init``     |               |                       |                 |               |
| 02     | ``linux_profile add``      | ``--module``  | ``package`` ``alias`` |                 |               |
| 03     | ``linux_profile install``  | ``--module``  | ``package`` ``alias`` | ``--category``  | ``default``   |


**RESOURCES**
- GitHub: https://github.com/MyLinuxProfile/linux-profile-basic
- Docs:   https://linuxprofile.com
