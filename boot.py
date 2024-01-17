from usb_cdc import Serial
from apps.home import HomeApp
import usb_cdc
import supervisor
import default_settings

supervisor.runtime.autoreload = False
supervisor.set_usb_identification("Manos Technologies", "AppPad RP2040")

usb_cdc.enable(console=True, data=True)


