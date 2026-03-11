import customtkinter as ctk

class Gui(ctk.CTk):
    button = ["Nie nasłuchuje", "Mów"]


    def __init__(self):
        super().__init__()
        
        self.title("Voice Recognizer")
        self.geometry("600x400")

        self.main = ctk.CTkFrame(self)
        self.main.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        self.label_text = ctk.StringVar()
        self.label_text.set(self.button[0])

        ctk.CTkLabel(self.main, textvariable=self.label_text,
                     font=ctk.CTkFont(size=24, weight="bold")).pack(pady=30)
        

        ctk.CTkButton(self.main, text="Zatwierdź",
                      command=self.control_listener).pack(pady=10)
        
    def control_listener(self):
        print(self.label_text.get() == self.button[0])
        if (self.label_text.get() == self.button[0]):
            self.label_text.set(self.button[1])
        else:
            self.label_text.set(self.button[0])
