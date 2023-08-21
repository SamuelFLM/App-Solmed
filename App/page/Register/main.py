import re
import webbrowser
from .iback import IBackRegister
from .tela import Tela
import PySimpleGUI as sg
import pyautogui as bot


class MainRegister(IBackRegister):
    def __init__(self, conexao) -> None:
        self.window = Tela()._front_end()
        self.conexao = conexao

    def validar_nome(self, nome):
        padrao = r"^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$"
        resultado = re.match(padrao, nome)
        if bool(resultado):
            self.window["title_name"].update("Name", text_color="#FFA620")
            return True
        else:
            self.window["title_name"].update("*Erro", text_color="red")

    def validar_email(self, email):
        padrao = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{1,3}$"
        resultado = re.match(padrao, email)
        if bool(resultado):
            self.window["title_email"].update("Email", text_color="#FFA620")
            return True
        else:
            self.window["title_email"].update("*Erro", text_color="red")

    def valida_telefone(self, telefone):
        padrao = r"^(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})$"
        resultado = re.match(padrao, telefone)
        if bool(resultado):
            self.window["title_phone"].update("Phone", text_color="#FFA620")
            return True
        else:
            self.window["title_phone"].update("*Erro", text_color="red")

    def _main(self, main):
        while True:
            event, values = self.window.read(timeout=1)

            if event == sg.WIN_CLOSED:
                break

            name = values["input_name"]
            email = values["input_email"]
            phone = values["input_phone"]
            password = values["password"]
            password_confirm = values["password-confirm"]

            validacao_name = self.validar_nome(name)
            validacao_email = self.validar_email(email)
            validacao_phone = self.valida_telefone(phone)

            if event == "btn-create-account":
                validacao = ""
                if bool(name):
                    if bool(email) and validacao_name:
                        if bool(phone) and validacao_email:
                            if bool(password) and validacao_phone:
                                if bool(password_confirm) and (password == password_confirm):
                                    validacao = "V"
                                else:
                                    bot.confirm(
                                    title="ERRO",
                                    text="SENHAS DIFERENTES",
                                    buttons=["OK"],
                                )

                if validacao == "V":
                    self.conexao.registro(name, email, phone, password)
                    bot.confirm(
                        title="SUCESSO",
                        text="CADASTRO REALIZADO COM SUCESSO!",
                        buttons=["OK"],
                    )
                    self.window.close()
                    main._main()
                    break
                else:
                    bot.confirm(
                        title="ERRO",
                        text="POR FAVOR, PREENCHER DEMAIS INFORMAÇÔES",
                        buttons=["OK"],
                    )

            if event == "btn-password-closed":
                self.window["btn-password-closed"].update(visible=False)
                self.window["btn-password-open"].update(visible=True)
                self.window["password"].update(password_char="")

            if event == "btn-password-open":
                self.window["btn-password-open"].update(visible=False)
                self.window["btn-password-closed"].update(visible=True)
                self.window["password"].update(password_char="*")

            if event == "btn-password-closed-confirm":
                self.window["btn-password-closed-confirm"].update(visible=False)
                self.window["btn-password-open-confirm"].update(visible=True)
                self.window["password-confirm"].update(password_char="")

            if event == "btn-password-open-confirm":
                self.window["btn-password-open-confirm"].update(visible=False)
                self.window["btn-password-closed-confirm"].update(visible=True)
                self.window["password-confirm"].update(password_char="*")

            if event == "btn_back":
                self.window.close()
                main._main()
                break
            if event == "btn_help":
                webbrowser.open_new_tab("https://github.com/SamuelFLM/Bot-Whatsapp")


if __name__ == "__main__":
    MainRegister("")._main()
