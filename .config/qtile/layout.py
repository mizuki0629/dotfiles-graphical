# -*- coding: utf-8 -*-
from libqtile.config import Match
from libqtile.layout.base import Layout
from libqtile.layout.columns import Columns
from libqtile.layout.floating import Floating
from libqtile.layout.max import Max
from libqtile.layout.xmonad import MonadTall, MonadWide

import colors


def init() -> list[Layout]:
    layout_theme = {
        "border_width": 8,
        "margin": 12,
        "border_focus": colors.magenta,
        "border_normal": colors.nord3,
    }
    return [
        MonadTall(**layout_theme),
        Max(name="Max"),
        MonadWide(**layout_theme),
        Columns(**layout_theme),
        # Try more layouts by unleashing below layouts.
        # layout.Stack(**layout_theme, num_stacks=2),
        # layout.Bsp(**layout_theme),
        # layout.Matrix(**layout_theme),
        # layout.RatioTile(**layout_theme),
        # layout.Tile(**layout_theme),
        # layout.TreeTab(**layout_theme),
        # layout.VerticalTile(**layout_theme),
        # layout.Zoomy(**layout_theme),
    ]


def init_floating() -> Floating:
    return Floating(
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            *Floating.default_float_rules,
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(wm_class="1password"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
        ]
    )
