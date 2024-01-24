import customtkinter as ctk
import tkinter as tk
import re
from src.view.scheduleTrakHome import scheduleTrakHome
from tkinter import filedialog

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class scheduleTrakViewDriver:
    def __init__(self, sourcePath: str) -> None:
        self.sourcePath = sourcePath
        self.root = ctk.CTk()
        self.root.geometry("1050x500")
        self.root.title("ScheduleTrak")
        rootx = self.root.winfo_width()
        rooty = self.root.winfo_height()
        self.mainFrame = ctk.CTkFrame(self.root, width=rootx, height=rooty)
        self.Home = scheduleTrakHome(self.mainFrame, self.sourcePath)

        self.Home.addEmailButton.configure(command=lambda: self.addNewEmail())
        self.Home.selectFilepathButton.configure(command=self.browseFiles)
        self.Home.submitMessage.configure(command=self.messageSubmit)
        self.Home.confirmTime.configure(command=self.updateTime)

        self.mainFrame.pack(fill='both', expand=True, padx=15, pady=15)

    def addNewEmail(self):
        dialog = ctk.CTkInputDialog(text="Email Address to add:", title="Add New Email")
        try:
            email = dialog.get_input()
            if self.isValidEmail(email):
                if self.controller.insertNewEmail(email):
                    self.Home.addEmailRow(email)
                    self.Home.emailCheckboxes[email].configure(command=lambda i=email: self.upEmail(i))
                    tk.messagebox.showinfo(parent=self.root, title='Success!', message='Success! Email has been added to list!')
                else:
                    tk.messagebox.showwarning(parent=self.root, title='Error!', message='Something went wrong! :(')
            else:
                tk.messagebox.showwarning(parent=self.root, title='Error!', message=f'{email} is not a valid email address')
                return
        except TypeError:
            return

    def assignController(self, controller):
        self.controller = controller

        currentEmailList = self.controller.getEmails()
        for email in currentEmailList:
            self.Home.addEmailRow(email[0], email[1])

        for i in self.Home.emailCheckboxes:
            self.Home.emailCheckboxes[i].configure(command=lambda i=i: self.upEmail(i))

        timeForSend = self.controller.getTime().split(':')
        self.Home.timeToSendWidget.setHour(timeForSend[0])
        self.Home.timeToSendWidget.setMinute(timeForSend[1])

        excelPath = self.controller.getPath()
        self.Home.pathToExcelEntry.insert(0, excelPath)

    def browseFiles(self):
        self.filename = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"), ("All files","*.*")))
        self.Home.pathToExcelEntry.delete(0, 'end')
        self.Home.pathToExcelEntry.insert(0, self.filename)

        self.controller.updatePath(self.filename)

        tk.messagebox.showinfo(parent=self.root, title='Path Added!', message=f'File path "{self.filename}" has been successfully assigned.')

    def isValidEmail(self, email):
        email_regex = r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"  # Basic email format check
        return re.match(email_regex, email) is not None
    
    def messageSubmit(self):
        message = self.Home.messageBox.get("1.0", "end").strip('\n')
        date = self.Home.pickDate.get_date()
        self.controller.insertNewMessage(date, message)
        self.Home.messageBox.delete(0.0, 'end')

        tk.messagebox.showinfo(parent=self.root, title="Message Submitted", message=f"Your message has been successfully added for {date}")

    def launch(self):
        self.root.mainloop()

    def updateTime(self):
        newTime = self.Home.timeToSendWidget.getTime()
        if self.controller.updateTime(newTime):
            tk.messagebox.showinfo(parent=self.root, title="Time Updated!", message=f"The time to send has been successfully updated!  Your schedule updates will now send at {newTime} daily.")
        else:
            tk.messagebox.showwarning(parent=self.root, title="Error!", message="While updating the time, and error has occurred.  Your time of update will not change.")


    def upEmail(self, email):
        self.controller.updateEmail(email, self.Home.emailCheckboxes[email].get())
        print(f"updated email {email} to {self.Home.emailCheckboxes[email].get()}")