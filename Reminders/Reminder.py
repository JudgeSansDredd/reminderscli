from Reminders.RemindersAppApi import RemindersAppApi


class Reminder:
    def __init__(self, title=None):
        self.id = None
        self.title = title
        self.body = None

    def __repr__(self) -> str:
        return f"Title: {self.title}"

    def save(self):
        if self.id is None:
            RemindersAppApi.new_reminder(self.title, self.body)

    @staticmethod
    def all():
        print("Reminder.all()")
        return RemindersAppApi.get_reminders()
