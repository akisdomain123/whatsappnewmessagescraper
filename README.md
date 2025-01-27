Track Processed Messages:

A file (processed_messages.txt) is used to store previously processed messages.
When the script runs, it loads the processed messages from this file.
Identify New Messages:

Messages in the chat are compared with the processed messages.
Only unprocessed (new) messages are displayed.
Update Processed Messages:

After processing, new messages are added to the processed messages set and saved back to the file.
How It Works
The script first loads already processed messages from processed_messages.txt.
It scrapes all messages in the chat and filters out messages already logged as processed.
Only new messages are displayed in the terminal.
The new messages are added to the log for future runs.
Output
When a new message appears in the "Demo" chat, it will be displayed, and only once.
Old messages (already processed) will not be shown again.




