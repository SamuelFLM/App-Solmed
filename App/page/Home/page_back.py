from interface_back import InterfaceHomeBack
import PySimpleGUI as sg
from page_front import PageFront

class PageBack(InterfaceHomeBack):
    
    def __init__(self) -> None:
        self.window = PageFront()._front_end()
        
    def _back_end(self):
        
        while True:
            event, values = self.window.read(timeout=1)
              

            if event == sg.WIN_CLOSED:
                break
            
            # check box remember email
            if values['chk-remember-me'] and event == 'btn-login':
                with open('App\data\dt-temp.txt', 'w') as arquivo:
                    arquivo.write(f"{values['email']}\n")          
                              
            # validação login

            # validação esqueceu senha
            if event == "forget-password":
                print('esqueci senha')

            # validação cadastro
            if event == "sign-up":
                print("login")

            # validação open/closed senha
            if event == "btn-password-closed":
                self.window["btn-password-closed"].update(visible=False)
                self.window["btn-password-open"].update(visible=True)
                self.window["password"].update(password_char="")

            if event == "btn-password-open":
                self.window["btn-password-open"].update(visible=False)
                self.window["btn-password-closed"].update(visible=True)
                self.window["password"].update(password_char="*")

if __name__ == "__main__":
    PageBack()._back_end()
    
    