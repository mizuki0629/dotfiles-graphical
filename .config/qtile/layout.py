# -*- coding: utf-8 -*-
from libqtile.config import Match, InvertMatch, MatchAll
from libqtile.layout.base import Layout
from libqtile.layout.columns import Columns
from libqtile.layout.floating import Floating
from libqtile.layout.max import Max
from libqtile.layout.xmonad import MonadTall, MonadWide

import colors


def init() -> list[Layout]:
    layout_theme = {
        "border_width": 4,
        "margin": 4,
        "border_focus": colors.cyan,
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
            MatchAll(
                Match(wm_type="utility"),
                InvertMatch(Match(wm_class="firefox", role="PictureInPicture")),
            ),
            Match(wm_type="notification"),
            Match(wm_type="toolbar"),
            Match(wm_type="splash"),
            Match(wm_type="dialog"),
            Match(wm_class="file_progress"),
            Match(wm_class="confirm"),
            Match(wm_class="dialog"),
            Match(wm_class="download"),
            Match(wm_class="error"),
            Match(wm_class="notification"),
            Match(wm_class="splash"),
            Match(wm_class="toolbar"),
            Match(func=lambda c: c.has_fixed_size()),
            Match(func=lambda c: c.has_fixed_ratio()),
            # Run the utility of `xprop` to see the wm class and name of an X client.
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(wm_class="1password"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
        ]
    )
