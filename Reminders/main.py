from applescript import AppleScript


class Reminders:
    @staticmethod
    def new_reminder(title, body):
        new_reminder_script = AppleScript(path="./scripts/new_reminder.applescript")
        new_reminder_script.run(title, body)
