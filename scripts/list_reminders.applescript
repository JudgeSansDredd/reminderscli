on run argv
    tell application "Reminders"
        set reminderListName to item 1 of argv
        set reminderList to list reminderListName
        set outputStrings to {}
        set reminderItems to reminders of reminderList
        repeat with reminderItem in reminderItems
            set reminderText to name of reminderItem
            copy reminderText to end of outputStrings
        end repeat
        return outputStrings
    end tell
end run