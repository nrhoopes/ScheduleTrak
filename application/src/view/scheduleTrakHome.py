import customtkinter as ctk
import time
from datetime import date
from PIL import Image
from tkcalendar import Calendar
from .CustomCTKModules.ctk_timeselect import CTkTimeSelect
from tkinter import IntVar

class scheduleTrakHome:
    def __init__(self, mainFrame) -> None:
        self.homePageFrame = ctk.CTkFrame(mainFrame)
        self.homePageFrame.grid_columnconfigure((0, 1, 2), weight=1)
        self.homePageFrame.grid_rowconfigure((1), weight=1)

        self.emailCheckboxes = {}

        self.loadMessageBar()
        self.loadAddMessagePane()
        self.loadEmailListPane()
        self.loadRightSidePane()

        self.homePageFrame.pack(fill='both', expand=True)

    def loadMessageBar(self):
        self.messageFrame = ctk.CTkFrame(self.homePageFrame, fg_color='#1f6aa5')
        self.messageFrame.grid_columnconfigure((1), weight=1)

        self.welcomeLabel = ctk.CTkLabel(self.messageFrame, font=("Rockwell Bold Italic", 66), text="ScheduleTrak")
        self.welcomeLabel.grid(row=0, column=0, pady=10, padx=5)

        self.DTimageCTK = ctk.CTkImage(light_image=Image.open('src/img/denTechLogoDark.png'), dark_image=Image.open('src/img/denTechLogoLight.png'), size=(350, 100))

        self.logoLabel = ctk.CTkLabel(self.messageFrame, image=self.DTimageCTK, text="")
        self.logoLabel.grid(row=0, column=1, pady=10, padx=10, sticky='e')

        self.messageFrame.grid(row=0, column=0, sticky='new', padx=10, pady=10, columnspan=3)

    def loadAddMessagePane(self):
        self.addMessageFrame = ctk.CTkFrame(self.homePageFrame)
        self.addMessageFrame.grid_propagate(False)
        self.addMessageFrame.grid_columnconfigure((1), weight=1)
        self.addMessageFrame.grid_rowconfigure((2), weight=1)

        addMessageLabel = ctk.CTkLabel(self.addMessageFrame, text="Add Extra Message:", font=("", 24))
        addMessageLabel.grid(row=0, column=0, padx=(5, 0), pady=(5, 10), sticky="w", columnspan=2)

        self.pickDate = Calendar(self.addMessageFrame, selectmode='day', showweeknumbers=False, cursor="hand2", date_pattern='y-mm-dd', borderwidth=0, bordercolor='white')
        self.pickDate.grid(row=1, column=0, columnspan=2, pady=(0, 5))

        msgLabel = ctk.CTkLabel(self.addMessageFrame, text="Msg:")
        msgLabel.grid(row=2, column=0, sticky="ne", padx=(5, 0))

        self.messageBox = ctk.CTkTextbox(self.addMessageFrame)
        self.messageBox.grid(row=2, column=1, sticky="nesw", padx=5, pady=5)

        self.submitMessage = ctk.CTkButton(self.addMessageFrame, text="Send", width=10)
        self.submitMessage.grid(row=2, column=0, sticky="w")


        self.addMessageFrame.grid(row=1, column=0, sticky="nesw", pady=5, padx=5)

    def loadEmailListPane(self):
        self.emailListFrame = ctk.CTkScrollableFrame(self.homePageFrame)
        self.emailListFrame.columnconfigure((0), weight=1)

        emailTitle = ctk.CTkLabel(self.emailListFrame, font=("", 26), text='Email List:')
        emailTitle.grid(row=0, column=0, sticky="w")

        pingTitle = ctk.CTkLabel(self.emailListFrame, font=("", 12), text='Ping?')
        pingTitle.grid(row=0, column=1)

        self.addEmailButton = ctk.CTkButton(self.emailListFrame, font=("", 20), text='Add New Email')
        self.addEmailButton.grid(row=1, column=0, ipadx=10, columnspan=2)

        self.emailListFrame.grid(row=1, column=1, sticky="nesw", pady=5, padx=5)

    def loadRightSidePane(self):
        self.rightSideFrame = ctk.CTkFrame(self.homePageFrame, fg_color='#333333')
        self.rightSideFrame.grid_columnconfigure((0), weight=1)
        self.rightSideFrame.grid_rowconfigure((0, 1, 2), weight=1)
        self.rightSideFrame.grid_propagate(False)

        # #
        self.timeToSendFrame = ctk.CTkFrame(self.rightSideFrame)
        self.timeToSendFrame.grid_columnconfigure((1), weight=3)
        self.timeToSendFrame.grid_columnconfigure((2), weight=1)
        self.timeToSendFrame.grid_rowconfigure((0, 1), weight=1)
        timeToSendLabel = ctk.CTkLabel(self.timeToSendFrame, text="Time to send email:", font=('', 20))
        timeToSendLabel.grid(row=0, column=0, columnspan=3, padx=5, sticky="w")

        self.timeToSendWidget = CTkTimeSelect(self.timeToSendFrame, font=("", 16))
        self.timeToSendWidget.grid(row=1, column=1, pady=(0, 10), padx=(5,0), sticky="nesw")

        self.confirmTime = ctk.CTkButton(self.timeToSendFrame, text="Confirm Time")
        self.confirmTime.grid(row=1, column=2, pady=(0, 10), padx=(0, 5), sticky="nesw")

        # #
        self.timeToSendFrame.grid(row=0, column=0, sticky='nesw')

        #
        self.addPathFrame = ctk.CTkFrame(self.rightSideFrame)
        self.addPathFrame.grid_columnconfigure((0), weight=1)
        pathToExcelLabel = ctk.CTkLabel(self.addPathFrame, font=("", 20), text="Path to Excel Schedule:")
        pathToExcelLabel.grid(row=0, column=0, sticky="nw", padx=5, pady=(5, 10))

        self.pathToExcelEntry = ctk.CTkEntry(self.addPathFrame, font=("", 10))
        self.pathToExcelEntry.grid(row=1, column=0, padx=10, sticky="sew")

        self.selectFilepathButton = ctk.CTkButton(self.addPathFrame, text="Select File Path...")
        self.selectFilepathButton.grid(row=2, column=0, padx=10, sticky="new")

        #
        self.addPathFrame.grid(row=1, column=0, sticky="nesw", pady=(10, 0))

        self.timeFrame = ctk.CTkFrame(self.rightSideFrame)
        self.timeFrame.grid_columnconfigure((0), weight=1)
        self.timeFrame.grid_rowconfigure((0, 1), weight=1)

        self.dateLabel = ctk.CTkLabel(self.timeFrame, text="NO DATE FOUND", font=("", 20))
        self.dateLabel.grid(row=0, column=0, sticky="sew")
        self.timeLabel = ctk.CTkLabel(self.timeFrame, text="NO TIME FOUND", font=("", 20))
        self.timeLabel.grid(row=1, column=0, sticky="new")
        self.__updateClock()

        self.timeFrame.grid(row=2, column=0, sticky="nesw", pady=(10, 0))

        self.rightSideFrame.grid(row=1, column=2, sticky="nesw", pady=5, padx=5)

    def addEmailRow(self,
                    email: str,
                    ping: bool = 1):
        emailEntry = ctk.CTkEntry(self.emailListFrame, font=("", 13))
        emailEntry.insert(0, email)
        checkVar = IntVar()
        checkVar.set(ping)
        checkbox = ctk.CTkCheckBox(self.emailListFrame, variable=checkVar, onvalue=1, offvalue=0, text=" ", width=0)
        self.emailCheckboxes[email] = checkbox
        self.addEmailButton.grid_forget()
        self.addEmailButton.grid(row=len(self.emailCheckboxes)+1, column=0, columnspan=2)
        emailEntry.grid(row=len(self.emailCheckboxes), column=0, sticky="ew")
        checkbox.grid(row=len(self.emailCheckboxes), column=1, sticky="e", padx=(5, 0))
        emailEntry.configure(state='disabled')

    def __updateClock(self):
        newTime = time.strftime("%H:%M:%S %p")
        self.timeLabel.configure(text=newTime)

        today = date.today()
        month = today.strftime("%B")
        day = today.strftime("%d")
        year = today.strftime("%Y")

        self.dateLabel.configure(text=f"Today is {month} {day}, {year}")

        self.homePageFrame.after(1000, self.__updateClock)
