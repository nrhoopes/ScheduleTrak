import smtplib
import os
import datetime
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Emailer:
    def __init__(self) -> None:
        # Definition of the required environ vars and logging into the smtp server.
        self.email_sender = os.environ.get('py_outlook_sender')
        self.email_login = os.environ.get('py_outlook_user')
        self.email_password = os.environ.get('py_outlook_pass')

        self.__smtp = smtplib.SMTP('smtp.office365.com', 587)
        self.__smtp.ehlo()
        self.__smtp.starttls()
        self.__smtp.ehlo()
        self.__smtp.login(self.email_login, self.email_password)

    def __del__(self):
        # Used for object deletion
        pass

    def logout(self):
        # Logout of the smtp server BEFORE deleting the object
        self.__smtp.quit()
        del self

    def sendDailyUpdate(self, emailList, schedule, colorKey, messages):
        subject = str(schedule[0]) + ' Schedule Update'
        text = 'This will appear if the HTML does not work'
        html = self.__emailHTMLBuilder(schedule, colorKey, messages)

        em = MIMEMultipart('alternative')
        em['From'] = self.email_sender
        # em['To'] = emailList
        em['Subject'] = subject
        # em.set_content(body)

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        em.attach(part1)
        em.attach(part2)
        
        if emailList != []:
            self.__smtp.sendmail(self.email_sender, emailList, em.as_string())
            print('Email Sent for ' + str(datetime.date.today()))
        else:
            print("No recipients set, email not sending...")

    def __emailHTMLBuilder(self, schedule, colorKey, messages):
        todaysDate = datetime.date.today()
        monthName = datetime.date(todaysDate.year, todaysDate.month, todaysDate.day).strftime("%B")
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        dayOfWeek = weekdays[todaysDate.weekday()]
        daySuffix = 'th'

        if todaysDate.day == 1 or todaysDate.day == 21 or todaysDate.day == 31:
            daySuffix = 'st'
        elif todaysDate.day == 2 or todaysDate.day == 22:
            daySuffix = 'nd'
        elif todaysDate.day == 3 or todaysDate.day == 23:
            daySuffix = 'rd'
        else:
            daySuffix = 'th'

        Email = f'''<html>
                        <head><h1>Good Morning! Today is {dayOfWeek}, {monthName} {todaysDate.day}{daySuffix}, {todaysDate.year}</h1><br><h3>Here are the schedules for today</h3></head>'''
        Email += '''\
    <style>
        td {
            text-align: center;
        }
        .styled-table {
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 0.9em;
            font-family: sans-serif;
            min-width: 400px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
        }
        .styled-table thead tr {
            background-color: #0A84FF;
            color: #ffffff;
            text-align: left;
        }
        .styled-table th,
        .styled-table td {
            padding: 12px 15px;
        }
        .styled-table tbody tr {
            border-bottom: 1px solid #dddddd;
        }
        .styled-table tbody tr:nth-of-type(even) {
            background-color: #f3f3f3;
        }
        .styled-table tbody tr:last-of-type {
            border-bottom: 2px solid #0A84FF;
        }
    </style>
    <body>
        <table border=1 class="styled-table">
            <thead>
                <tr>
                    <td colspan="3" style="font-size: 26px;"> Automation </td>
                </tr>
                <tr>
                    <td> Name </td>
                    <td> Job </td>
                    <td> Location </td>
                </tr>
            </thead>
            <tbody>
'''
        for rowNum, row in enumerate(schedule):
            if rowNum == 0:
                continue
            elif rowNum == len(schedule) - 1:
                Email += '</tbody> </table> <br> <h3> Additional Notes: </h3>' + str(row[1])
                Email += f'<p>{messages}</p>'
                Email += '</body> </html>'
            else:
                Email += '<tr>'
                for colNum, col in enumerate(row):
                    if colNum == 2:
                        colorCode = list({i for i in colorKey if colorKey[i]==str(col)})
                        try:
                            Email += f'<td style="background-color: #{str(colorCode[0][2:])};">{str(col)}</td>'
                        except:
                            Email += f'<td>{str(col)}</td>'
                    else:
                        Email += f'<td>{str(col)}</td>'
                Email += '</tr>'

        return Email


