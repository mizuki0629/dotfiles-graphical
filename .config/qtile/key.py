# -*- coding: utf-8 -*-
from libqtile.config import Group, Key
from libqtile.lazy import lazy


def init(mod: str, groups: list[Group]) -> list[Key]:
    terminal = "kitty"

    # fmt: off
    keys = [
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
        Key([mod, "control"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([mod, "control"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
        Key([mod, "control"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        Key([mod, "shift"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([mod, "shift"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([mod, "shift"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "shift"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        Key([mod], "i", lazy.layout.grow()),
        Key([mod], "n", lazy.layout.normalize()),
        Key([mod], "o", lazy.layout.maximize()),
        Key([mod], "m", lazy.layout.shrink()),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        # Toggle between different layouts as defined below
        Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
        Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
        Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
        Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        Key([mod], "r", lazy.spawn("rofi -show combi"), desc="Spawn a rofi drun"),
        # Key([mod], 'r', lazy.run_extension(extension.DmenuRun(
        #     dmenu_prompt=">",
        #     dmenu_font="HackGen Console NF-20",
        #     # background="#15181a",
        #     # foreground="#00ff00",
        #     selected_background="#079822",
        #     selected_foreground="#fff",
        #     dmenu_height=24,  # Only supported by some dmenu forks
        # ))),
    ]

    for i in groups:
        keys.extend(
            [
                # mod1 + letter of group = switch to group
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                ),
                # mod1 + shift + letter of group = switch to & move focused window to group
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                ),
                # Or, use below if you prefer not to switch to that group.
                # # mod1 + shift + letter of group = move focused window to group
                # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                #     desc="move focused window to group {}".format(i.name)),
            ]
        )

    return keys
