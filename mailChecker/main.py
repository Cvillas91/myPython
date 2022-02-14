from email import message
import imaplib
import email

imap_server = "imap.gmail.com"
email_address = "youremail@gmail.com"
password = "yourpassword"

imap = imaplib.IMAP4_SSL(imap_server,993)
imap.login(email_address, password)

imap.select("Inbox")
_, msgnums = imap.search(None, "ALL")

for msgnum in msgnums[0].split():
    _, data = imap.fetch(msgnum, "(RFC822)")
    
message = email.message_from_bytes(data[0][1])
print(f"Message Number: {msgnum}")
print(f"From: {message.get('From')}")
print(f"To: {message.get('To')}")
print(f"BCC: {message.get('BCC')}")
print(f"Date: {message.get('Date')}")
print(f"Subject: {message.get('Subject')}")

print("Content:")
for part in message.walk():
    if part.get_content_type() == "text/plain" : 
        print(part.as_string())

imap.close()
