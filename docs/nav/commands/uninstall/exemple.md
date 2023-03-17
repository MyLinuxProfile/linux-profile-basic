# Exemple

## Permissions

Run the installation commands with administrator permission.

- Input

```bash
linuxp uninstall --module package --sudo
```

- Command result

```bash
sudo apt uninstall python3
sudo apt uninstall python3-pip
```

## Debug

Run the installation commands in test mode. In test mode the commands are not
actually executed on the machine, they are just displayed in the terminal.

- Input

```bash
linuxp uninstall --module package --debug
```

- Command result

```bash
echo 'sudo apt uninstall python3'
echo 'sudo apt uninstall python3-pip'
```

## Group

This command groups the items for executing the command.

- Input

```bash
linuxp uninstall --module package --group
```

- Command result

```bash
sudo apt uninstall python3 python3-pip
```

## Uninstall Package

### Module

**Full Command**
```bash
linuxp uninstall --module package
```
**Short Command**
```bash
linuxp uninstall -m package
```

### Tag

**Full Command**
```bash
linuxp uninstall --module package --tag util
```
**Short Command**
```bash
linuxp uninstall -m package -t util
```

### Item

**Full Command**
```bash
linuxp uninstall --module package --tag util --item vim
```

**Short Command**
```bash
linuxp uninstall -m package -t util -i vim
```

## Uninstall Script

### Module

**Full Command**
```bash
linuxp uninstall --module script
```
**Short Command**
```bash
linuxp uninstall -m script
```

### Tag

**Full Command**
```bash
linuxp uninstall --module script --tag system
```
**Short Command**
```bash
linuxp uninstall -m script -t system
```

### Item

**Full Command**
```bash
linuxp uninstall --module script --tag system --item clean_my_linux
```

**Short Command**
```bash
linuxp uninstall -m script -t system -i clean_my_linux
```


## Uninstall Alias

### Module

**Full Command**
```bash
linuxp uninstall --module alias
```
**Short Command**
```bash
linuxp uninstall -m alias
```

### Tag

**Full Command**
```bash
linuxp uninstall --module alias --tag util
```
**Short Command**
```bash
linuxp uninstall -m alias -t util
```

### Item

**Full Command**
```bash
linuxp uninstall --module alias --tag util --item play_music
```

**Short Command**
```bash
linuxp uninstall -m alias -t util -i play_music
```