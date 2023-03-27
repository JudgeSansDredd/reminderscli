import os

from whiptail import Whiptail

from Reminders.main import Reminders

#####################
# TERMINAL SETTINGS #
#####################
TERMINAL_WIDTH=os.get_terminal_size().columns
TERMINAL_HEIGHT=os.get_terminal_size().lines
WHIPTAIL_SETTINGS={
    "title": "Reminders",
    "width": TERMINAL_WIDTH - 10,
    "height": TERMINAL_HEIGHT - 10
}
wt = Whiptail(**WHIPTAIL_SETTINGS)

def new_reminder():
    title, code = wt.inputbox("What is the title?")
    if code:
        return
    body, code = wt.inputbox("What is the body?")
    if code:
        return
    Reminders.new_reminder(title, body)

###################
# Main Line Logic #
###################
def main():
    new_reminder()

if __name__ == '__main__':
    main()
