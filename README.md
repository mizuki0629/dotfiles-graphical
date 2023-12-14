# dotfiles-graphical
dotfiles for unix graphical tools

## install
The installation can be done in several ways.

### 1. copy
copy dotfiles to your home dirctory

### 2. rrcm
[rrcm](https://github.com/mizuki0629/rrcm) is simple dotfiles management and deploy tool.

edit your .config/rrcm/config.yaml
```yaml
---
dotfiles:
  windows: "%USERPROFILE%\\dotfiles"
  mac: "${HOME}/.dotfiles"
  linux: "${HOME}/.dotfiles"
repos:
# add config for this repository
  - name: graphical
    url: 'https://github.com/mizuki0629/dotfiles-graphical.git'
    deploy:
      home:
        linux: "${HOME}"
      .config:
        linux: "${XDG_CONFIG_HOME}"
```

clone and deploy
```sh
rrcm update
```

### 3. use other tools
