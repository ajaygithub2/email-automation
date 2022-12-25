# email-automation
Send plain text emails with customized names or other things to multiple email addresses from an excel sheet using python.(only for gmail)


Using the "email_auto.py"

You can send emails to multiple email addresses available in an excel file or in a csv file(use read_csv instead of read_excel)
Note: For sending emails from a gmail account, you can't simply use your gmail password, you have to create an app password in your google account.

Libraries required:

1. smtplib
2. ssl
3. pandas

First 2 packages are by default installed with python.
For pandas, you can install this way:

pip install pandas

Here is a youtube link for how I made this script and how you can create the app password - https://youtu.be/DO-RtrLC43Y
