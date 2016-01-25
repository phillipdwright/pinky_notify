# Code taken from 
#  http://jmduke.com/posts/how-to-send-emails-through-python-and-gmail/
#
# Google Apps SMTP settings:
#  https://support.google.com/a/answer/176600?hl=en

from smtplib import SMTP
import os, sys
projectpath = os.path.dirname(__file__)
sys.path.append(projectpath)
import gmail

GMAIL_USERNAME = gmail.username
GMAIL_PASSWORD = gmail.password

# Build the email
email_subject = '\\\\pinky is back up!'
# recipients = ['pwright@medeco.com', 'wright.phillip@gmail.com']
recipients = ['pwright@medeco.com',
				'trippe@medeco.com',
				'cgrant@medeco.com',
				'chenson@medeco.com',
				'rconner@medeco.com',
				'dakers@medeco.com',
				'bbrummette@medeco.com'
				]
headers = '\r\n'.join(['from: Phil Wright <' + GMAIL_USERNAME + '>',
                        'subject: ' + email_subject,
                        'to: ' + recipients[0],
                        'mime-version: 1.0',
                        'content-type: text/html'])
body_of_email = """
					<html>
					Folks,<br><br>
					The PINKY server has been restored to service, 
					and you should be able to create APS and key 
					cutting files on it now as needed.  Please 
					contact me if you continue to experience issues 
					with this process.<br><br>
					Thanks!<br><br>
					Phil
					</html>
					"""
content = headers + "\r\n\r\n" + body_of_email

# Create session
# session = smtplib.SMTP('smtp.gmail.com', 587)
# Changed port to 25 after getting timeout error with 587 & 465
with SMTP('smtp.gmail.com', 25) as session:
    #session = smtplib.SMTP('smtp.gmail.com', 25) 
    session.ehlo()
    session.starttls()
    # Next line failed until I changed my "Less secure apps" setting at
    #  https://www.google.com/settings/security/lesssecureapps
    #  (See https://support.google.com/accounts/answer/6010255 )
    session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
    
    # Send the email!
    session.sendmail(GMAIL_USERNAME, recipients, content)

	
