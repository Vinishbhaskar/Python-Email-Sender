# Email-Sender-Bot
A Python script that sends emails, including attachments, to up to 50 recipients at a time using the built-in smtplib library. It also includes a feature for sending mail with Carbon copy(Cc) and Blind carbon copy(Bcc) to multiple recipients.

### Features
- Sends emails to up to 50 recipients at a time
- Includes attachments
- Includes feature for sending mail with Carbon copy(Cc) and Blind carbon copy(Bcc) to multiple recipients
- Incorporates error handling and retry logic to enhance email delivery rate
### Dependencies
- Python 3.x
- smtplib

### Usage
The script takes in recipient's email address, subject, message and attachments as input and sends the email.

First off all, clone this repo using the command
```
$ git clone https://github.com/Vinishbhaskar/Python-Email-Sender.git
```
<p>This script will sent message with Resume file so keep your resume in root director of "Email-Sender-Bot" which you have cloned </p>
<p> You Have to paste your message in 'msg.py' file manually with variable-name 'company_name', in case you wanted to mention it followed by variable 'subject'.</p>

### Create Password from google (<a href = "https://support.google.com/mail/answer/185833?hl=en-GB"> password token generate </a>)

- click on 'select app' choose 'Other' then name it 'mailpy' then click on 'Generate'
- you will get your token password then copy it then paste in 'main.py' with variable = "user_pass"


### Note
The script is intended for educational and personal use only. And for sending emails in bulk, one must check with their service provider and follow the regulations.

This repository is created by Vinish Bhaskar as a part of his personal projects and showcases his skills in building script and working with smtplib. The script is open source, so anyone can use it, improve it, and suggest new features. Please feel free to submit pull requests and open issues if you have any questions or suggestions.
