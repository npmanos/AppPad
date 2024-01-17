"""
An App program for Adafruit MACROPAD. This was modified from the original
Adafruit Macropad Hotkeys code (https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/main/Macropad_Hotkeys).
It enables you to more easily create complex layouts and has other advanced
features, including double-tap support.
"""

import usb_cdc
from usb_cdc import Serial
from utils.app_pad import AppPad
from utils.apps.base import BaseApp
from utils.commands import AppSwitchException
from utils.constants import OS_LINUX, OS_MAC, OS_WINDOWS

try:
    from user import DEFAULT_APP
except ImportError:
    from default_settings import DEFAULT_APP

try:
    from user import AppSettings
except ImportError:
    from default_settings import AppSettings

datacom: Serial = usb_cdc.data  # type: ignore
datacom.write(b"?os")
datacom.flush()
host_os: str = datacom.readline().decode().rstrip('\r\n') #type: ignore
print(host_os)

if host_os.startswith("!os="):
    _, host_os = host_os.split('=', 1)

if host_os not in [OS_LINUX, OS_MAC, OS_WINDOWS]:
    host_os = OS_MAC

BaseApp.load_apps('/apps')

app_pad = AppPad()
current_app: BaseApp = DEFAULT_APP(app_pad, AppSettings(host_os=host_os))

try:
    while True:
        try:
            print(f"Current App = {current_app.name}")
            current_app.run()
        except AppSwitchException as err:
            current_app = err.app
except Exception as e:
    print("Exception in event_stream, importing keyboard and releasing all keys.")

    from adafruit_hid.keyboard import Keyboard
    from usb_hid import devices

    Keyboard(devices).release_all()
    raise e
