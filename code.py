"""
An App program for Adafruit MACROPAD. This was modified from the original
Adafruit Macropad Hotkeys code (https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/main/Macropad_Hotkeys).
It enables you to more easily create complex layouts and has other advanced 
features, including double-tap support.
"""

from apps.func import FuncKeysApp
from apps.key import Key, KeyApp, SettingsSelectKey, SettingsValueKey
from apps.nav import NavApp
from apps.numpad import NumpadApp
from app_pad import AppPad
from apps.switcher import AppSwitcherApp
from apps.window import WindowManagementApp
from commands import (
    ConsumerControlCode,
    Media,
    PreviousAppCommand,
    SwitchAppCommand,
)
from constants import (
    COLOR_APPS,
    COLOR_FUNC,
    COLOR_LINUX,
    COLOR_MAC,
    COLOR_MEDIA,
    COLOR_NAV,
    COLOR_NUMPAD,
    COLOR_WINDOWS,
    COLOR_WINMAN,
    OS_SETTING,
    OS_LINUX,
    OS_MAC,
    OS_WINDOWS,
    PREVIOUS_APP_SETTING,
)

app_pad = AppPad()


macro_settings = {
    OS_SETTING: OS_MAC,
    PREVIOUS_APP_SETTING: [],
}


class MacroSettingsApp(KeyApp):
    name = "Macropad Settings"

    key_0 = SettingsSelectKey("MAC", 0x555555, OS_SETTING, OS_MAC, PreviousAppCommand())
    key_1 = SettingsSelectKey(
        "WIN", 0x00A4EF, OS_SETTING, OS_WINDOWS, PreviousAppCommand()
    )
    key_2 = SettingsSelectKey(
        "LIN", 0x25D366, OS_SETTING, OS_LINUX, PreviousAppCommand()
    )

    encoder_button = PreviousAppCommand()


func_keys_app = FuncKeysApp(app_pad, macro_settings)
nav_app = NavApp(app_pad, macro_settings)
numpad_app = NumpadApp(app_pad, macro_settings)
settings_app = MacroSettingsApp(app_pad, macro_settings)
window_manager_app = WindowManagementApp(app_pad, macro_settings)


app_switcher_app = AppSwitcherApp(app_pad, macro_settings)


class HomeApp(KeyApp):
    """
    Main menu app that displays when starting the Macropad. Includes media
    controls, a selector for the host OS, and buttons to switch to various
    the other defined apps.
    """

    name = "Home"

    key_0 = SettingsValueKey(
        OS_SETTING,
        SwitchAppCommand(settings_app),
        color_mapping={
            OS_MAC: COLOR_MAC,
            OS_WINDOWS: COLOR_WINDOWS,
            OS_LINUX: COLOR_LINUX,
        },
        text_template="[ {value} ]",
    )

    key_3 = Key(text="Num", color=COLOR_NUMPAD, command=SwitchAppCommand(numpad_app))
    key_4 = Key(text="Nav", color=COLOR_NAV, command=SwitchAppCommand(nav_app))
    key_5 = Key(text="Func", color=COLOR_FUNC, command=SwitchAppCommand(func_keys_app))

    key_6 = Key(
        text="Apps", color=COLOR_APPS, command=SwitchAppCommand(app_switcher_app)
    )
    key_8 = Key(
        text="WinMan", color=COLOR_WINMAN, command=SwitchAppCommand(window_manager_app)
    )

    # Fourth row
    key_9 = Key("<<", COLOR_MEDIA, Media(ConsumerControlCode.SCAN_PREVIOUS_TRACK))
    key_10 = Key(">||", COLOR_MEDIA, Media(ConsumerControlCode.PLAY_PAUSE))
    key_11 = Key(">>", COLOR_MEDIA, Media(ConsumerControlCode.SCAN_NEXT_TRACK))

    encoder_button = Media(ConsumerControlCode.MUTE)

    encoder_increase = Media(ConsumerControlCode.VOLUME_INCREMENT)
    encoder_decrease = Media(ConsumerControlCode.VOLUME_DECREMENT)

    def __init__(self, app_pad):
        super().__init__(app_pad, settings=macro_settings)


app_pad.add_app(HomeApp)
app_pad.run()
