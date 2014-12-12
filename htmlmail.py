#!/usr/bin/python

import smtplib

smtpObj = smtplib.SMTP('10.11.0.25', 25)

sender = 'presidents_office@pcom.edu'
receivers = 'marcwe@pcom.edu'

message = """From: PCOM <president's_office@pcom.edu>
To: marcwe <marcwe@pcom.edu>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

try:
   smtpObj = smtplib.SMTP('10.11.0.25', 25)
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"