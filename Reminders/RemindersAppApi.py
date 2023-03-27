from applescript import AppleScript

from Reminders.Config import Config


class RemindersAppApi:
    def __init__(self):
        self.default_list = Config.get_default_list()

    def _new_reminder(self, title, body):
        new_reminder_script = AppleScript(path="./scripts/new_reminder.applescript")
        new_reminder_script.run(self.default_list, title, body)

    def _get_reminders(self):
        get_reminder_script = AppleScript(path="./scripts/list_reminders.applescript")
        get_reminder_script.run(self.default_list)

    @classmethod
    def new_reminder(cls, title, body):
        cls()._new_reminder(title, body)

    @classmethod
    def get_reminders(cls):
        cls()._get_reminders()
