on run argv
    tell application "Reminders"
        set reminderlist to list "Reminders"
        tell reminderlist
            make new reminder at end with properties {name: item 1 of argv, body: item 2 of argv}
        end tell
    end tell
end run