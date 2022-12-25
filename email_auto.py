# import required libraries
import smtplib, ssl
import pandas as pd


# you can also enter the path to the file if file is not in the same directory
# use this dataframe to customize anything you want either in body of message or subject
emails = pd.read_excel("exel_file_name.xlsx")

# port that we need
port = 465

# creates a secure ssl connection
context = ssl.create_default_context()

# connects to gmail
server = smtplib.SMTP_SSL("smtp.gmail.com", port, context = context)

# login to your google account (for gmail, you have to generate an app password by going into your google account > Security > App passwords
server.login("yourmail@mail.com", "app-password-generated")

#loop for sending emails
for index in range(len(emails)):
    message = f"""\
Subject: This is the subject.
To: {emails["Emails"][index]}

Hello {emails["Names"][index]}
This is the 2nd line."""
    server.sendmail("yourmail@mail.com", emails["Emails"][index], message)
    print(f"Sent to: {emails['Emails'][index]}")
