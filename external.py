#!/usr/bin/python

import smtplib

smtpObj = smtplib.SMTP('10.11.0.25', 25)

sender = 'presidents_office@pcom.edu'
receivers = 'marcwe@pcom.edu'

part1 = """From: PCOM President's Office<president's_office@pcom.edu>"""
part2 = """To: marcwe <""" + receivers + """>"""
part3 = """MIME-Version: 1.0
Content-type: text/html
Subject: Holiday Greeting Card 2014



<font color="blue">Please adjust your volume settings to hear sound.</font><br />
<br />
<a href="http://dev.pcom.edu/communications/marcom/presidentscard_2014/holidaycard_external_2014.html" target="_blank"><img src="http://dev.pcom.edu/communications/marcom/presidentscard_2014/externalemail.png" width="425" height="406" /></a>
<br><br><a href ="mailto:president%27s_office@pcom.edu?subject=2014_card_remove">Please remove me from this list</a>
"""
message = part1 + part2 + part3
try:
   smtpObj = smtplib.SMTP('10.11.0.25', 25)
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"