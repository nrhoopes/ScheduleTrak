import customtkinter
from typing import Union, Callable, Tuple

class CTkTimeSelect(customtkinter.CTkFrame):
    def __init__(self, *args,
               width: int = 125,
               height: int = 32,
               font: Tuple[str, float] = ("", 13),
               command: Callable = None,
               **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.font = font                                          # Font of the text in the entry
        self.buttonSizes = (self.font[0], self.font[1]-5)         # Dynamic text size of the up and down arrows
        self.command = command                                    # command

        self.configure(fg_color=("gray78", "gray28"))

        self.grid_columnconfigure((1, 3), weight=0)     # Push the arrow buttons to the far right so they don't expand
        self.grid_columnconfigure((0, 2), weight=1)     # Expand the entry as much as possible
        self.grid_rowconfigure((0, 1), weight=1)        # Expand the height of the widget

        # Hour Select
        self.downHourButton = customtkinter.CTkButton(self, text='▼', font=self.buttonSizes, width=height-28, height=height-18,
                                                  command=self.downHourButtonCallback)
        self.downHourButton.grid(row=1, column=1, padx=0.5, pady=0.5, sticky="nesw")

        self.hourEntry = customtkinter.CTkEntry(self, width=width-(3*height), font=self.font, height=height-18, border_width=0, justify='center')
        self.hourEntry.grid(row=0, column=0, rowspan=2, padx=0.5, pady=0.5, sticky="nesw")
        self.hourEntry.bind("<MouseWheel>", self.onHourMousewheel) # Bind a dynamic mousewheel event

        self.upHourButton = customtkinter.CTkButton(self, text='▲', font=self.buttonSizes, width=height-28, height=height-18,
                                                command=self.upHourButtonCallback)
        self.upHourButton.grid(row=0, column=1, padx=0.5, pady=0.5, sticky="nesw")


        # Minute Select
        self.downMinuteButton = customtkinter.CTkButton(self, text='▼', font=self.buttonSizes, width=height-28, height=height-18,
                                                  command=self.downMinuteButtonCallback)
        self.downMinuteButton.grid(row=1, column=3, padx=0.5, pady=0.5, sticky="nesw")

        self.minuteEntry = customtkinter.CTkEntry(self, width=width-(3*height), font=self.font, height=height-18, border_width=0, justify='center')
        self.minuteEntry.grid(row=0, column=2, rowspan=2, padx=0.5, pady=0.5, sticky="nesw")
        self.minuteEntry.bind("<MouseWheel>", self.onMinuteMousewheel) # Bind a dynamic mousewheel event

        self.upMinuteButton = customtkinter.CTkButton(self, text='▲', font=self.buttonSizes, width=height-28, height=height-18,
                                                command=self.upMinuteButtonCallback)
        self.upMinuteButton.grid(row=0, column=3, padx=0.5, pady=0.5, sticky="nesw")

        # Insert zeroes as default value
        self.hourEntry.insert(0, "00")
        self.minuteEntry.insert(0, "00")
    
    # Format string to have a 0 in front of it
    def __formatZero(self, string):
        return "0" + str(string)

    # Callback for mousewheel event
    def onHourMousewheel(self, event):
        if event.delta > 0: # Scroll up
            self.upHourButtonCallback()
        else: # Scroll down
            self.downHourButtonCallback()

    def onMinuteMousewheel(self, event):
        if event.delta > 0: # Scroll up
            self.upMinuteButtonCallback()
        else: # Scroll down
            self.downMinuteButtonCallback()

    def upHourButtonCallback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.hourEntry.get()) + 1
            if value < 10 and value > -1:
                value = self.__formatZero(str(value))

            if int(value) >= 24:
                value = "00"
            
            self.hourEntry.delete(0, "end")
            self.hourEntry.insert(0, value)
        except ValueError:
            return
    
    def downHourButtonCallback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.hourEntry.get()) - 1
            if value < 10 and value > -1:
                value = self.__formatZero(str(value))

            if int(value) <= -1:
                value = "23"

            self.hourEntry.delete(0, "end")
            self.hourEntry.insert(0, value)
        except ValueError:
            return
        
    def upMinuteButtonCallback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.minuteEntry.get()) + 1
            if value < 10 and value > -1:
                value = self.__formatZero(str(value))

            if int(value) >= 60:
                value = "00"

            self.minuteEntry.delete(0, "end")
            self.minuteEntry.insert(0, value)
        except ValueError:
            return
    
    def downMinuteButtonCallback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.minuteEntry.get()) - 1
            if value < 10 and value > -1:
                value = self.__formatZero(str(value))

            if int(value) <= -1:
                value = "59"
            
            self.minuteEntry.delete(0, "end")
            self.minuteEntry.insert(0, value)
        except ValueError:
            return
        
    def getHour(self) -> Union[str, None]:
        try:
            return str(self.hourEntry.get())
        except ValueError:
            return None
        
    def setHour(self, value: str):
        self.hourEntry.delete(0, "end")
        self.hourEntry.insert(0, str(value))

    def getMinute(self) -> Union[str, None]:
        try:
            return str(self.minuteEntry.get())
        except ValueError:
            return None
        
    def setMinute(self, value: str):
        self.minuteEntry.delete(0, "end")
        self.minuteEntry.insert(0, str(value))

    def getTime(self) -> Union[str, None]:
        try:
            return str(self.hourEntry.get()) + ':' + str(self.minuteEntry.get())
        except ValueError:
            return None