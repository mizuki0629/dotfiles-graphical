# -*- coding: utf-8 -*-
from libqtile.config import Screen

import widget


def init():
    return [
        Screen(
            top=widget.init_bar(),
        ),
    ]
