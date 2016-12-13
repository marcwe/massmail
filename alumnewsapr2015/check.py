import smtplib

smtp = smtplib.SMTP()
smtp.connect('10.11.0.25', 25)
# orig server = smtplib.SMTP('mail')
# orig server.set_debuglevel(True)  # show communication with the server
smtp.set_debuglevel(True)  # show communication with the server
try:
    # orig dhellmann_result = server.verify('dhellmann')
    # orig notthere_result = server.verify('notthere')
    dhellmann_result = smtp.verify('marcwe@pcom.edu')
    notthere_result = smtp.verify('notthere')
finally:
    smtp.quit()

print 'dhellmann:', dhellmann_result
print 'notthere :', notthere_result
