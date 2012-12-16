import mailbox
for message in mailbox.mbox('teste100.mbox'):
    subject = message['subject']       # Could possibly be None.
    if subject and 'bailux' in subject.lower():
        print message["From"]
