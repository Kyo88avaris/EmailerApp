import smtplib
import getpass

"""
Simple Python Scripiting to send out SMTP e-mails

ver 1.0:
initial script


Improvements Required:
* Validations for SMTP Login
* Validations for correct inputs
* Multiple Recipients

"""

print("\nPython Scripting E-mailer Application")

email_server_val = True
while email_server_val:
    print("\nSelect the E-mail Server from the List Below:\n 1. Gmail \n 2. Outlook \n 3. Office 365\n 4. Yahoo Mail")

    email_server = input()

    if email_server == '1':
        smtp = 'smtp.gmail.com'
        auth = 587
        email_server_val = False
    elif email_server == '2':
        smtp = 'smtp.live.com'
        auth = 587
        email_server_val = False
    elif email_server == '3':
        smtp = 'smtp.office365.com'
        auth = 587
        email_server_val = False
    elif email_server == '4':
        smtp = 'smtp.mail.yahoo.com'
        auth = 465
        email_server_val = False
    else:
        print("Invalid Input Detected: Please select from 1 - 4:")



smtp_obj = smtplib.SMTP( smtp , auth)
smtp_obj.ehlo()

smtp_obj.starttls()

email = input("Please Enter your E-mail: ")
password = getpass.getpass("Please Enter your Password: ")

smtp_obj.login(email, password)

from_address = email
verify_bool = True

while verify_bool:
            
    to_address = input('\nRecipient E-mail Address: ')
    subject = input("Input Subject Line: ")
    message = input("Input Message Data: ")

    print("\nRecipient E-mail: {}".format(to_address))
    print("Subject: {}".format(subject))
    print("\nMessage:\n{}".format(message))

    check_info = input("Is the E-mail good to send: use Y/N: ")

    if check_info.lower() == "y":
        verify_bool = False
    else:
        print("Clearing E-mail Information!")




full_mesage = "Subject: " + subject + "\n" + message

smtp_obj.sendmail(from_address,to_address,full_mesage)
smtp_obj.sendmail(from_address,from_address,full_mesage)


print("Successful E-mail Sent!")
smtp_obj.quit()