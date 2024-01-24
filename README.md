# ScheduleTrak v0.2
ScheduleTrak is a locally hosted (by you) Excel Schedule Spreadsheet interpreter for allowing your team to keep 
tabs on one another.  The goal of the system is to keep everyone on your team (be it technicians, sales reps, programmers and more)
in the loop about what everyone should be working on for the day.

Include things like location, job description, and names of your team members, and have a nice daily schedule sent out
via Email updating whoever you need on where your team is and what they are doing!  No need for annoying group texts!

# Python Version and Operating Systems
- Developed for Python v3.11.4
- Tested on Python v3.11.4, Windows 10
- GUI application developed using CustomTkinter
- Internet connection required for the runtime to send emails

# Instructions for running release
1. Download the latest release

2. Extract all files to a location of your choice

3. Inside you will find two folders, application and runtime, each containing their respective programs

4. You will also find the ```setEmailSender.bat``` tool, which will assist you in setting up the email address to send the updates from. First time setup will require using this.

5. Create your team schedule using the template included.  It is important to follow the structure of the example, otherwise your program may not work or email updates may send incorrectly.

6. Launch the application to add emails to your list, set the time of day to send the work week update, and set the location of your schedule.

7. Launch the runtime on the machine where it will live, and verify it can access the database and the Excel sheet.

8. Enjoy the simplicity of Automation, without the need for group texts!

# Tips for running the release
1. Make sure to keep your schedule up-to-date and correctly formatted!  See the included example/template.  You can add as many weeks as you'd like, and you can add as many team member rows as you would like, just keep it within the same format.  You are limited the number of locations across the top, however colors are arbitrary, and as long as the colors match the key, they will display the correct location on your emails.  MAKE SURE YOU UPDATE THE DATES IF YOU TRY TO USE THE EXAMPLE AS AN EMAIL!!

2. ScheduleTrak will send emails based on the current date, so you will always see today's schedule!

3. If you don't want to use the ```setEmailSender.bat``` setup tool, make sure to setup these environment variables:
    i. py_outlook_user = your email address
    ii. py_outlook_pass = your email's password
    iii. py_outlook_sender = the email you would like to send from.  This is typically something like service@yourdomain.com, but could be anything.  If you do not need this, use your email address here.

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
