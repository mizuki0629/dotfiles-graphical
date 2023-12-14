# -*- coding: utf-8 -*-
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

__default_terminal = "kitty"


def cmd_spawn(cmd: str):
    terminal = guess_terminal(__default_terminal)
    if terminal is None:
        raise Exception("No terminal found")
    return lazy.spawn(terminal + " " + cmd)
