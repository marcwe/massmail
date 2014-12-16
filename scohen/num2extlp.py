# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

recips = ['bademail@m.nor' 'marcwe@pcom.edu' , 'marcwepcom@yahoo.com' , 'marcwert@netscape.net', 'pcomalumni@gmail.com' , 'conniee@pcom.edu', 'stephaniecoh@pcom.edu']


# Define these once; use them twice!
strFrom = "Alumni Office <Alumni@pcom.edu>"
strTo = 'marcwe@pcom.edu'

for recip in recips:
	strTo = recip
	
	# Create the root message and fill in the from, to, and subject headers
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = 'Thank you message from our students.'
	msgRoot['From'] = strFrom
	msgRoot['To'] = strTo
	msgRoot.preamble = 'This is a multi-part message in MIME format.'

	# Encapsulate the plain and HTML versions of the message body in an
	# 'alternative' part, so message agents can decide which they want to display.
	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)

	#msgText = MIMEText('This is the alternative plain text message.')
	msgText = MIMEText('click on http://goo.gl/qiD4Nn for the students message')
	msgAlternative.attach(msgText)

	# We reference the image in the IMG SRC attribute by the ID we give it below
	#msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!', 'html')
	msgText = MIMEText('<font color="blue">Are you wondering how your gift to PCOM makes a difference?<br><br>Watch this video to hear from current students about how alumni support makes an impact on their lives.</font><br /><br /><a href="http://goo.gl/qiD4Nn" target="_blank"><img src="cid:image1" width="674" height="366" /></a><br><br> To make your gift to PCOM visit our online giving site <a href="http://www.pcom.edu/donate">pcom.edu/donate</a><br><br>If you have already made a gift, thank you for your support.<br><br><a href ="mailto:alumni@pcom.edu?subject=2014_card_remove">Please remove me from this list</a>', 'html')
	msgAlternative.attach(msgText)

	# This example assumes the image is in the current directory
	fp = open('Selection_582.jpg', 'rb')
	msgImage = MIMEImage(fp.read())
	fp.close()

	# Define the image's ID as referenced above
	msgImage.add_header('Content-ID', '<image1>')
	msgRoot.attach(msgImage)


	# Send the email (this example assumes SMTP authentication is required)
	import smtplib
	smtp = smtplib.SMTP()
	smtp.connect('10.11.0.25', 25)
	#smtp.login('exampleuser', 'examplepass')
	smtp.sendmail(strFrom, strTo, msgRoot.as_string())
	smtp.quit()