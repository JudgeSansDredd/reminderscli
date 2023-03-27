from gui.whiptail import TERMINAL_WIDTH, wt
from Reminders.Config import Config
from Reminders.Reminder import Reminder


def new_reminder():
    title, code = wt.inputbox("What is the title?")
    if code:
        return
    body, code = wt.inputbox("What is the body?")
    if code:
        return
    r = Reminder(title)
    r.body = body
    r.save()

def list_reminders():
    pass

###################
# Main Line Logic #
###################
def main():
    # Make sure our config file is written and has necessary info
    proceed = Config.set_configuration()
    if not proceed:
        return

    reminders = [
        x[:(TERMINAL_WIDTH - 39)] + '...'
        if len(x) > TERMINAL_WIDTH - 39
        else x
        for x
        in Reminder.all()
    ]

    code = 0
    while code == 0:
        _, code = wt.checklist("Your checklist", reminders)

if __name__ == '__main__':
    main()
