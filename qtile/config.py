from typing import List  # noqa: F401

import re
import socket

from libqtile import qtile
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess
from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

# Variables
mod = "mod4"
terminal = guess_terminal()
term = "termite"
Vol = "eww open vol"
Power = "eww open power"
Spotify = "eww open spotify"
Editor = "subl3"
Web = "google-chrome-stable"
Filer = "nemo"
Panel = "eww open-many sidebar webapps webapps2 mpd calendar weather sys"
Wall = "feh -g 240x170+1095+246 --zoom 18 ~/Imagens/*"

# Layouts
gaps = 20
borderwidth = 0

# Colors
normal = '#DDE4C7'
highlight = '#6FB4F0'

keys = [
    # Switch between windows
    Key([mod], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),

    Key([mod], "s", lazy.spawn(Editor), desc="Launch Editor"),
    Key([mod], "n", lazy.spawn(Filer), desc="Launch Filer"),
    Key([mod], "c", lazy.spawn(Web), desc="Launch Browser"),
    Key([mod], "e", lazy.spawn(Panel), desc="Launch Panel"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    #Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

group_names = [("One", {'layout': 'monadtall'}),
               ("Two", {'layout': 'monadtall'}),
               ("Tree", {'layout': 'monadtall'}),
               ("Four", {'layout': 'monadtall'}),
               ("Five", {'layout': 'monadtall'}),
               ("Six", {'layout': 'monadtall'}),
               ("Seven", {'layout': 'monadtall'}),
               ("Eight", {'layout': 'monadtall'}),
               ("Nine", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layouts = [
    layout.Columns(border_focus_stack ='#F76538',
        margin = gaps,
        border_normal = normal,
        border_focus = highlight,
        border_width = borderwidth,),

    layout.Max(margin = gaps,
        border_normal = normal,
        border_focus = highlight,
        border_width = borderwidth,),

    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),

    layout.Matrix(margin = gaps,
           border_normal = normal,
           border_focus = highlight,
           border_width = borderwidth,),

    layout.MonadTall(margin = gaps,
        border_normal = normal,
        border_focus = highlight,
        border_width = borderwidth,),

    layout.MonadWide(margin = gaps,
        border_normal = normal,
        border_focus = highlight,
        border_width = borderwidth,),

    layout.RatioTile(margin = gaps,
        border_normal = normal,
        border_focus = highlight,
        border_width = borderwidth,),

    layout.Tile(margin = gaps,
        border_normal = normal,
        border_focus = highlight,
        border_width = borderwidth,),

    # layout.TreeTab(),
    layout.VerticalTile(margin = gaps,
        border_normal = normal,
        border_focus = highlight,
        border_width = borderwidth,),
]

widget_defaults = dict(
    font = 'monospace',
    fontsize = 15,
    padding = 3,
    background= normal,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                       text = " ??? ",
                       fontsize = 20,
                       padding = 0,
                       background = highlight,
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(Spotify)}
                       ),
                widget.GroupBox(borderwidth = 2,
                    this_current_screen_border = highlight,),

                widget.CurrentLayout(background = highlight,),
                widget.Prompt(foreground = highlight),
                widget.Spacer(),

                widget.TextBox(
                       text = " ??? ",
                       fontsize = 20,
                       padding = 0,
                       background = highlight,
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(Vol)}
                       ),

                widget.PulseVolume(fontsize = 15,
                                    margin = 1,
                                    foreground = '#708090'),
                widget.Sep(
                    linewidth = 0,
                    padding = 30,
                ),

                 widget.TextBox(
                    text=" ??? ",
                    fontsize = 20,
                    background = highlight
                ),

                widget.Clock(format='%a, %I:%M %p',
                    foreground = '#708090'),

                widget.Systray(icon_size = 15),
                widget.Sep(
                    linewidth = 0,
                    padding = 10,
                ),

                widget.TextBox(
                       text = " ??? ",
                       fontsize = 20,
                       padding = 0,
                       background = highlight,
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(Power)}
                       ),
            ],
            40,
            margin=[18, 12, 5, 12],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_normal = normal,
    border_focus = highlight,
    border_width = borderwidth,
    float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'), # GPG key password entry
    Match(title='feh'),
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
