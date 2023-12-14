# -*- coding: utf-8 -*-
try:
    from qtile_extras import widget  # type: ignore
except ImportError:
    from libqtile import widget

import os.path

from libqtile import bar

import colors
import util

try:
    from qtile_extras.widget.decorations import BorderDecoration  # type: ignore

    def decorations_border(color: str) -> list[object]:  # type: ignore
        return [
            BorderDecoration(
                colour=color,
                border_width=[0, 0, 2, 0],
            )
        ]

except ImportError:

    def decorations_border(color: str) -> list[object]:
        return []


def __cpu(color: str):  # type: ignore
    return widget.CPU(  # type: ignore
        format=" Cpu: {load_percent:>3.0f}%",
        foreground=color,
        decorations=decorations_border(color),
        mouse_callbacks={"Button1": util.cmd_spawn("htop")},
    )


def __memory(color: str):  # type: ignore
    return widget.Memory(  # type: ignore
        format="{MemUsed: .1f}{mm}/{MemTotal: .1f}{mm}",
        fmt="󰍛 Mem: {}",
        measure_mem="G",
        foreground=color,
        decorations=decorations_border(color),
        mouse_callbacks={"Button1": util.cmd_spawn("htop")},
    )


def __disk(color: str):  # type: ignore
    return widget.DF(  # type: ignore
        update_interval=60,
        foreground=color,
        partition="/",
        format="[{p}] {uf}{m} ({r:.0f}%)",
        # format = '{uf}{m} free',
        fmt=" Disk: {}",
        visible_on_warn=False,
        decorations=decorations_border(color),
        mouse_callbacks={"Button1": util.cmd_spawn("watch -n 1 df -h")},
    )


def __net(color: str):  # type: ignore
    return widget.Net(  # type: ignore
        foreground=color,
        prefix="M",
        use_bits=True,
        fmt="󰒍 {}",
        decorations=decorations_border(color),
    )


def __quickexit(color: str):  # type: ignore
    return widget.QuickExit(  # type: ignore
        foreground=color,
        # default_text = '[X]',
        decorations=decorations_border(color),
    )


def __wallpaper(color: str):  # type: ignore
    return widget.Wallpaper(  # type: ignore
        foreground=color,
        fmt=" ",
    )


def __groupbox(**opts):  # type: ignore
    return widget.GroupBox(  # type: ignore
        margin_y=3,
        margin_x=5,
        padding_y=2,
        padding_x=5,
        borderwidth=3,
        active=colors.foreground,
        inactive=colors.magenta,
        rounded=False,
        highlight_method="line",
        this_current_screen_border=colors.cyan,
        this_screen_border=colors.green,
        other_current_screen_border=colors.magenta,
        other_screen_border=colors.green,
        **opts,
    )


def __windowname(color: str, **opts):  # type: ignore
    return widget.WindowName(  # type: ignore
        foreground=color,
        padding=5,
        max_chars=40,
        **opts,
    )


def __currentlayout(color: str, **opts):  # type: ignore
    return widget.CurrentLayout(  # type: ignore
        foreground=color,
        **opts,
    )


def __currentlayouticon(color: str, **opts):  # type: ignore
    return widget.CurrentLayoutIcon(  # type: ignore
        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
        use_mask=True,
        scale=0.9,
        foreground=color,
        **opts,
    )


def __prompt(color: str, **opts):  # type: ignore
    return widget.Prompt(  # type: ignore
        foreground=color,
        prompt="Run: ",
        **opts,
    )


def init_bar():
    spacer = widget.Spacer(length=8)  # type: ignore

    return bar.Bar(
        [
            __groupbox(),
            spacer,
            __currentlayouticon(colors.foreground),
            spacer,
            __currentlayout(colors.foreground),
            spacer,
            __prompt(colors.foreground),
            spacer,
            __windowname(colors.blue),
            __wallpaper(colors.foreground),
            spacer,
            widget.Clock(  # type: ignore
                format="󰥔 %Y-%m-%d(%a) %H:%M",
            ),
            spacer,
            __cpu(colors.magenta),
            spacer,
            __memory(colors.green),
            spacer,
            __disk(colors.blue),
            spacer,
            __net(colors.yellow),
            spacer,
            widget.Systray(padding=3),  # type: ignore
            spacer,
            __quickexit(colors.red),
        ],
        24,
    )


def defaults():
    return {
        "font": "HackGen Console NF",
        "fontsize": 20,
        "padding": 0,
        "foreground": colors.foreground,
        "background": colors.background,
    }


def extension_defaults():
    return defaults()
