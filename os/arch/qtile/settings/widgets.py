from libqtile import widget
from .theme import colors


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=15, text="?"):
    padding_y = 5  # Ajusta el valor del padding superior
    padding_bottom = 0  # Ajusta el valor del padding inferior
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=5,
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="\ueb6f",  # Icon: nf-oct-triangle_left
        fontsize=50,
        padding=-4
    )


def workspaces():
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color4', 'dark'),

    icon(bg="color4", text='\uf11c ', fontsize=20),  # Icon: nf-fa-keyboard_o

    widget.KeyboardLayout(**base(bg="color4"),
                          configured_keyboards=['us', 'es'], padding=5),

    powerline('color3', 'color4'),

    icon(bg="color3", text='\uf09e '),  # Icon: nf-fa-feed

    widget.Net(interface='enp8s0', **base(bg='color3'), padding=10),

    powerline('color5', 'color3'),

    icon(bg="color5", text='\uf4bc '),  # Icon: nf-fa-microchip

    widget.CPU(**base(bg='color5'), padding=5),

    powerline('color2', 'color5'),

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerline('color1', 'color2'),

    # Icon: nf-mdi-calendar_clock
    icon(bg="color1", fontsize=17, text='\ueab0 '),

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),



]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font ',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
