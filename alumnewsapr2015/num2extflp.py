# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.
import time

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

urlFile = open("mailList.txt", "r+")
mailList = [i.strip() for i in urlFile.readlines()]


# Define these once; use them twice!
strFrom = "Alumni Office <Alumni@pcom.edu>"
strTo = 'marcwe@pcom.edu'

for recip in mailList:
	strTo = recip
	print "%r" % (strTo)

	# Create the root message and fill in the from, to, and subject headers
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = 'Updates from the PCOM Alumni Office'
	msgRoot['From'] = strFrom
	msgRoot['To'] = strTo
	msgRoot.preamble = 'This is a multi-part message in MIME format.'

	# Encapsulate the plain and HTML versions of the message body in an
	# 'alternative' part, so message agents can decide which they want to display.
	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)

	#msgText = MIMEText('This is the alternative plain text message.')
	msgText = MIMEText('click on http://goo.gl/FJHdpS for the Alumni Newsletter')
	msgAlternative.attach(msgText)

	# We reference the image in the IMG SRC attribute by the ID we give it below
	#msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!', 'html')
	msgText = MIMEText('<img alt="http://www.pcom.edu/Alumni_Relations___Development/alumnewsimg/alumnews.png" src="http://www.pcom.edu/Alumni_Relations___Development/alumnewsimg/alumnews.png" usemap="#alumnews">    <map name="alumnews">      <area shape="rect" coords="160,389,419,437" href="https://www.facebook.com/PCOMAlumni" alt="facebook" target="_blank">      <area shape="rect" coords="77,455,458,495" href="http://goo.gl/FJHdpS" alt="newsletter" target="_blank">      <area shape="rect" coords="160,200,520,280" href="http://goo.gl/FJHdpS" alt="newsletter" target="_blank">    </map><br><br><a href="http://goo.gl/FJHdpS">Updates from Alumni Relations and Development</a><BR><BR><a href="alumni@pcom.edu?subject=March2015newsletter">Please help me get this newsletter</a>', 'html')
	#msgText = MIMEText('<font color="blue">Are you wondering how your gift to PCOM makes a difference?<br><br>', 'html')
	msgAlternative.attach(msgText)

	# This example assumes the image is in the current directory
	#fp = open('Selection_582.jpg', 'rb')
	##   fp = open('Selection_582.jpg', 'rb')
	##   msgImage = MIMEImage(fp.read())
	##   fp.close()

	# Define the image's ID as referenced above
	##  msgImage.add_header('Content-ID', '<image1>')
	##  msgRoot.attach(msgImage)


	# Send the email (this example assumes SMTP authentication is required)
	import smtplib
	smtp = smtplib.SMTP()
	smtp.connect('10.11.0.25', 25)
	#smtp.login('exampleuser', 'examplepass')
	smtp.sendmail(strFrom, strTo, msgRoot.as_string())
	smtp.quit()
	# Wait for 5 seconds
	time.sleep(.1)
