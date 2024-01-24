from board import DISPLAY as display
from displayio import Group
import usb_cdc
import supervisor


display.auto_refresh = False
display.root_group = Group()
display.refresh()

supervisor.runtime.autoreload = False
supervisor.set_usb_identification("Manos Technologies", "AppPad RP2040")

usb_cdc.enable(console=True, data=True)


