import os

from whiptail import Whiptail

TERMINAL_WIDTH=os.get_terminal_size().columns
TERMINAL_HEIGHT=os.get_terminal_size().lines
WHIPTAIL_SETTINGS={
    "title": "Reminders",
    "width": TERMINAL_WIDTH - 10,
    "height": TERMINAL_HEIGHT - 10
}
wt = Whiptail(**WHIPTAIL_SETTINGS)
