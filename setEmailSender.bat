@ECHO OFF
echo You can use this batch file to quickly setup your email credentials.
echo This will be the email that sends your schedule updates daily.
echo It will require at least a username (your email address) and the password you would
echo use to send an email.  You can also add an 'as sender' option, which allows you to send
echo as another email address you have access to (example: service@yourdomain.com).
echo Retype your email if this does not apply to you.
echo.
echo If you would like to manually enter your credentials for the service, create the
echo following environment variables:
echo.
echo 		py_outlook_user = your email address
echo 		py_outlook_pass = your email's password
echo			py_outlook_sender = the email addr to send from (e.g. service@yourdomain.com)
echo					NOTE: you can put your user email as the sender
echo.

set /p username=Enter your email address:
setx py_outlook_user %username%

set /p password=Enter your email password:
setx py_outlook_pass %password%

set /p sender=If you would like to send as another email, enter it here, otherwise retype your email:
setx py_outlook_sender %sender%

pause