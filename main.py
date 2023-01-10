import smtplib
import os.path
from email.message import EmailMessage
from msg import msg_body, company_name, subject

# Sender details for Authentication
# create this password from your google account
#  [https://support.google.com/mail/answer/185833?hl=en-GB]

sender = "jiteshece@gmail.com"
user_pass = "euyprqjsgslvhlcx"
sent_from = "Jitesh Kumar"


sent_to = ["jitesh@gmail.com", "test@gmail.com"]
sent_to_cc = ["kejir51247@tohup.com", "example@gmail.com"]
sent_to_bcc = ["vinishbhaskar@gmail.com", "testmail@gmail.com"]


# Keep Your Resume & message.txt file in root directory
# if Resume or message is in different directory then kindle paste its full patch respectively
# update resume_path with your own Resume file name or you can use full path of your Resume

resume_path = "JakesResume.pdf"
message_path = "message.txt"
message_file_name = os.path.isfile(message_path)
resume_file_name = os.path.isfile(resume_path)


# send msg from  a text file
with open(message_path, 'r') as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())


# Adding Resume file
with open(resume_path, "rb") as fp:
    msg = EmailMessage()
    file_type = fp.read()
    resume_file_name = "JakesResume.pdf"


msg = EmailMessage()
msg.set_content(msg_body)
# msg.add_alternative(message_path)
msg.add_attachment(file_type, maintype="pdf",
                   subtype="file_type", filename=resume_file_name)

msg["Subject"] = subject
msg["From"] = sent_from
msg["To"] = ",".join(sent_to)
msg["Cc"] = ",".join(sent_to_cc)
msg["Bcc"] = ",".join(sent_to_bcc)

try:
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.ehlo()
    smtp_server.login(sender, user_pass)
    smtp_server.send_message(msg)
    smtp_server.close()

except Exception as e:
    print("Error found", e)

print("Email Sent successfuly")
