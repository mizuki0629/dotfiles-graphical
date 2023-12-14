# -*- coding: utf-8 -*-
import os.path
import subprocess
from typing import Literal

from libqtile import hook
from libqtile.config import Group, Key, Mouse, Rule, Screen
from libqtile.layout.base import Layout
from libqtile.layout.floating import Floating

import group
import key
import layout
import mouse as mouseconfig
import screen
import widget

mod = "mod4"


groups: list[Group] = group.init()
keys: list[Key] = key.init(mod, groups)
mouse: list[Mouse] = mouseconfig.init(mod)
# mouse: list[Mouse] = mouse.init(mod)

layouts: list[Layout] = layout.init()
floating_layout: Floating = layout.init_floating()

widget_defaults = widget.defaults()
extension_defaults = widget.extension_defaults()
screens: list[Screen] = screen.init()

dgroups_key_binder = None
dgroups_app_rules: list[Rule] = []

follow_mouse_focus: bool = True
bring_front_click: bool = False

floats_kept_above: bool = True
cursor_warp: bool = False
auto_fullscreen: bool = True
focus_on_window_activation: Literal["urgent", "focus", "smart", "never"] = "smart"
reconfigure_screens: bool = True
auto_minimize: bool = True
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname: str = "LG3D"


@hook.subscribe.startup_once  # type: ignore
def autostart():
    home = os.path.expanduser("~")
    subprocess.Popen([home + "/.config/qtile/autostart.sh"])


@hook.subscribe.shutdown  # type: ignore
def shutdown():
    home = os.path.expanduser("~")
    subprocess.Popen([home + "/.config/qtile/shutdown.sh"])
