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

Please adjust your volume settings to hear sound.</span><br />
<br />
<a href="http://dev.pcom.edu/communications/marcom/presidentscard_2014/holidaycard_external_2014.html" target="_blank"><img src="http://dev.pcom.edu/communications/marcom/presidentscard_2014/externalemail.png" width="425" height="406" /></a>
"""

try:
   smtpObj = smtplib.SMTP('10.11.0.25', 25)
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"