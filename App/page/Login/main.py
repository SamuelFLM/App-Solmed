from iback import IBackLogin
import PySimpleGUI as sg
from tela import Tela

class Main(IBackLogin):
    
    def __init__(self) -> None:
        self.window = Tela()._front_end()
        
    def _main(self):
        
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
    Main()._main()
    
    