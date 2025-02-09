# -*- coding: utf-8 -*-
from libqtile.backend.base.window import WindowType
from libqtile.config import Group, Match


def is_youtube_music(window: WindowType):
    result = "youtube music" in (window.name or "").lower()
    return result


def init():
    return [
        Group(name=str(idx), **group)  # type: ignore
        for idx, group in enumerate(
            [
                {
                    "label": "󰵮",
                },
                {
                    "label": "󰀖",
                },
                {
                    "label": "♫",
                    "matches": [
                        Match(func=is_youtube_music),
                    ],
                },
                {
                    "label": "",
                    "matches": [
                        Match(wm_class="org.remmina.Remmina"),
                    ],
                },
                {"label": "5"},
                {"label": "6"},
                {"label": "7"},
                {"label": "8"},
                {"label": "9"},
            ],
            start=1,
        )
    ]
