on run argv
    tell application "Reminders"
        set reminderList to list item 1 of argv
        tell reminderList
            make new reminder at end with properties {name: item 2 of argv, body: item 3 of argv}
        end tell
    end tell
end run