on run argv
    tell application "Reminders"
        set reminderListName to item 1 of argv
        set outputStrings to {}
        tell reminderListName
            -- set reminderItems to reminders of reminderListName
            -- repeat with reminderItem in reminderItems
                -- set reminderText to name of reminderItem whose completed is false
                -- copy reminderText to end of outputStrings
            -- end repeat
        end tell
    end tell
end run