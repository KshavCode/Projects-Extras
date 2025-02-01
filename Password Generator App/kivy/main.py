from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from Generator import generate
from kivymd.uix.dialog import MDDialog
from pyperclip import copy
from kivymd.uix.button import MDFlatButton

class screen(Screen):
    def diss(self, button):
        self.dialog.dismiss()
    def copied(self, button):
        copy(self.password)
        button.text = "Copied"
        button.disabled = True
        
    def gen(self, val):
        CloseButton = MDFlatButton(text="Close", on_release=self.diss, font_size="15dp")
        try : 
            val = int(val)
            if val < 5 or val > 20:   
                self.dialog = MDDialog(title="ERROR!", text="The length should be between 5 and 20!", buttons=[CloseButton])
            else: 
                successButton = MDFlatButton(text="Copy to Clipboard", on_release=self.copied, font_size="15dp")
                self.password = generate(val)
                self.dialog = MDDialog(title="SUCCESS!", text=f"Your generated password is : \n{self.password}", buttons=[successButton,CloseButton])
        except ValueError:
            self.dialog = MDDialog(title="ERROR!", text="The length should be numerical!", buttons=[CloseButton])
        self.dialog.open()
class myapp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        return screen()

if __name__=="__main__":
    myapp().run()