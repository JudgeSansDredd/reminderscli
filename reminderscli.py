from gui.whiptail import wt
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

    reminders = Reminder.all()
    print(reminders)

if __name__ == '__main__':
    main()
