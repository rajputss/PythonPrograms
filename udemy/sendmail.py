import smtplib as mail

# create smtp server connection
mailserver = mail.SMTP("example.net")
mailserver.login("testusr", "testpassword")
msg = '''FROM: Sender Name <sender@example.net>
TO: <reciepient@example.net>
SUBJECT: This is test subject
Content-Type: text\html
MIME-Version: 1.0
TEST BODY OF EMAIL MESSAGE.'''
mailserver.sendmail("sender@example.net", "reciepient@example.net", msg)
