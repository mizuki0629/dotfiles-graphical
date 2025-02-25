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
                border_width=[0, 0, 3, 0],
            )
        ]

except ImportError:

    def decorations_border(color: str) -> list[object]:
        return []


def __cpu(color: str):  # type: ignore
    return widget.CPU(  # type: ignore
        format=" Cpu:{load_percent:>3.0f}%",
        foreground=color,
        decorations=decorations_border(color),
        mouse_callbacks={"Button1": util.cmd_spawn("htop")},
    )


def __memory(color: str):  # type: ignore
    return widget.Memory(  # type: ignore
        format="{MemUsed: .1f}{mm}/{MemTotal: .1f}{mm}",
        fmt="󰍛 Mem:{}",
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
        # format="{down:3.0f}{down_suffix} ↓↑ {up:3.0f}{up_suffix}",
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
        inactive=colors.nord10,
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
        # max_chars=40,
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
        scale=0.7,
        foreground=color,
        **opts,
    )


def __prompt(color: str, **opts):  # type: ignore
    return widget.Prompt(  # type: ignore
        foreground=color,
        prompt="Run: ",
        **opts,
    )


def __checkupdates():  # type: ignore
    return widget.CheckUpdates(  # type: ignore
        custom_command="apt list --upgradable",
        custom_command_modify=(lambda x: x - 1),
        colour_have_updates=colors.nord11,
        colour_no_updates=colors.nord10,
        # distro="Ubuntu",
        no_update_string="No updates",
    )


def init_bar():
    spacer = widget.Spacer(length=10)  # type: ignore

    return bar.Bar(
        [
            spacer,
            __currentlayouticon(colors.foreground),
            spacer,
            __groupbox(),
            spacer,
            __prompt(colors.foreground),
            spacer,
            __windowname(colors.foreground),
            __checkupdates(),
            spacer,
            widget.Systray(padding=10),  # type: ignore
            spacer,
            __cpu(colors.yellow),
            spacer,
            __memory(colors.green),
            spacer,
            __net(colors.cyan),
            spacer,
            widget.Clock(  # type: ignore
                format="%m/%d(%a) %H:%M",
                decorations=decorations_border(colors.foreground),
            ),
            spacer,
        ],
        30,
    )


def defaults():
    return {
        "font": "ComicCode Nerd Font",
        "fontsize": 19,
        "padding": 0,
        "foreground": colors.foreground,
        "background": colors.background,
    }


def extension_defaults():
    return defaults()
