# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile workspaces

from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import mod, keys


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
groups = [Group(i) for i in [
    " \uf269  ", # nf-fa-firefox,
    " \ue62b ", # nf-dev-terminal,
    " \ue795  ", # nf-fa-code,
    " \uf308  ", # nf-seti-config,
    " \uf013  ", # nf-fa-folder,
    " \ue5ff  ", # nf-mdi-image,
    " \uf03e  ", # nf-fa-video_camera,
    " \uf03d  ", # nf-fa-video_camera,
    " \uf1bc  " # nf-fa-video_camera,
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
