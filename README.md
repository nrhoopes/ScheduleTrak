# ScheduleTrak v0.1
ScheduleTrak is a locally hosted Excel schedule spreadsheet interpreter that allows you to build schedules
around your team and update people daily on where or what your technicians/sales reps/programmers/team members may be!
This keeps everyone in the loop of where your team members are located and what job they are working on, and the addition
of email addresses allows whoever you need to be notified at a time you set daily of the location of your team according
to a schedule you make! Enjoy the automation of updating your team on their schedules, without the need for annoying group texts!

# Python Version and Operating Systems
- Developed for Python v3.11.4
- Tested on Python v3.11.4, Windows 10
- GUI application developed using CustomTkinter

# Instructions for running release
1. Coming soon...

# Instructions for running (in current build)
1. Git clone the repository

2. Use command ```cd ScheduleTrak```

3. Running the runtime:
    * On Windows: ```py runtime/schedulerRuntime.py```
    * For launching the OPCUA server for Ignition alongside the runtime, use the included batch file (currently not fully implemented)

4. Running the application:
    * On Windows: ```py application/scheduleTrak.py```

Notes:
On first run of the runtime, the program will create a database in the directory that
schedulerRuntime.py is located.  This can be changed in the Runtime's driver file (```schedulerRuntime.py```) but also
requires updating in the ```__init__``` of ```scheduleTrakController.py```.

On first run of the application, you will need to set the time in which you would like your runtime to
send your emails out.  You can do this by selecting a time using the scroll box in the top right corner of the
app.  Assure you click 'Confirm Time' to send it to the database.  You will also need to include a path to
your excel file that contains your schedule.  Do note that the excel file MUST be formatted as the example,
yet colors and number of rows per week can be decided by you.

Also note that Emails will only be sent Mon-Fri, and only to emails that are included in your email list.

NOTE: Due to the use of HTML in the emails, GMAIL will currently immediately throw your email into the SPAM folder.  This is being
      worked on.  For now the only tested Email service that is confirmed working with the HTML is outlook.

NOTE: In order for your emails to be sent at the time you would like them to be, you MUST keep the runtime open on your computer,
      whether this be on a server or the computer you want to run the service, it must remain running at all times.

# Instructions
1. You can start the runtime and leave it sit on a server or computer somewhere and it will automatically send emails daily, MON-FRI at
the time desired by the user.
2. Format your Excel schedule as the example included.  Colors or number of rows are arbitrary and can be modified by the schedule admin.
3. Once you start the runtime up, you can also open the application, which can be opened and closed at will, and allows the user to
interact with the database and what information gets sent out to who.
4. Choose your time to send emails, select the path to your schedule, and add some emails to your list.  The ping column for the Email
list is whether or not you want that email to receive schedule updates (This feature can be used in case someone goes on vacation..).
5. You can also add extra messages to your daily updates by selecting a date on the calendar in the lefthand box, typing your message in
the Msg box, and clicking send.  You can send multiple messages in a day and they will all be compiled together on that day's message.
You can also schedule messages for further out if you wish.
6. Once you've done your setup, you can close out of the application and leave the runtime running in the background, and enjoy the
sweetness of an automated schedule notifier! No more group texts!
