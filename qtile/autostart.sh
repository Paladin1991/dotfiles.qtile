#!/bin/bash
setxkbmap -model abnt2 -layout br -variant abnt2
picom -b --config ~/.config/qtile/picom.conf
~/.fehbg &
exec /usr/lib/xfce4/notifyd/xfce4-notifyd &
eww daemon
xsetroot -cursor_name left_ptr &
exit
