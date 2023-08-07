from ifront import IFrontLogin
import PySimpleGUI as sg


class Tela(IFrontLogin):
    __slots__ = ["__color"]

    def __init__(self) -> None:
        self.__color = "white"
        sg.theme_background_color(self.__color)
        self.dados_salvos =  [""]
        
        with open('App\data\dt-temp.txt', 'r') as arquivos:
            for i, arquivo in enumerate(arquivos):
                self.dados_salvos[i] = str(arquivo).strip()
   
            
    def _front_end(self):
        barra_notificacao = [
            sg.Image(filename="App//img//barra de notificacao.png", pad=(0, (0, 50)))
        ]

        logo = [
            #[sg.Text("", background_color=self.__color, pad=(100, (0, 40))),],
            [sg.Image(
                filename="App//img//logo.png",
                background_color=self.__color,
                pad=(0, (0, 70)),
            ),]
           
        ]

        welcome_back = [
            [sg.Text(
                "Welcome back",
                font="Jaldi 20 bold",
                background_color=self.__color,
                text_color="#FFA620",
                pad=(0, (0, 0)),
            ),],
            [sg.Text(
                "Sign to continue",
                font="Jaldi 10 bold",
                background_color=self.__color,
                text_color="#535353",
                pad=(0, (0, 40)),
            ),]
        ]

        email = (
            [
                [
                    sg.Text(
                        "Email/Phone Number",
                        font="Jaldi 13 bold",
                        background_color=self.__color,
                        text_color="#FFA620",
                        pad=(0, (0, 10)),
                    ),
                    sg.Text("", background_color=self.__color, pad=(80, (0, 10))),
                ],
                [
                    sg.Image(
                        filename="App//img//email.png",
                        background_color=self.__color,
                        pad=(10, (0, 5)),
                    ),
                    sg.Input(
                        f"{self.dados_salvos[0]}",
                        size=(25, 10),
                        background_color=self.__color,
                        font="Jaldi 13",
                        pad=(0, (0, 5)),
                        border_width=0,
                        text_color="#535353",
                        key="email",
                    ),
                        
                    sg.Image(
                        filename="App//img//invisivel.png",
                        background_color=self.__color,
                        pad=(30, (0, 5)),
                    ),
                ],
                [sg.HSep(pad=(20, (0, 20)))],
            ],
        )
        password = [
            [
                sg.Text(
                    "Password",
                    font="Jaldi 13 bold",
                    background_color=self.__color,
                    text_color="#FFA620",
                    pad=(0, (0, 10)),
                ),
                sg.Text("", background_color=self.__color, pad=(120, (0, 10))),
            ],
            [
                sg.Image(
                    filename="App//img//password.png",
                    background_color=self.__color,
                    pad=(10, (0, 5)),
                ),
                sg.Input(
                    f"",
                    size=(25, 10),
                    password_char="*",
                    background_color=self.__color,
                    font="Jaldi 13",
                    pad=(0, (0, 5)),
                    border_width=0,
                    text_color="#535353",
                    key="password",
                ),
                sg.Image(
                    filename="App//img//password-closed.png",
                    background_color=self.__color,
                    enable_events=True,
                    key="btn-password-closed",
                    pad=(30, (0, 5)),
                ),
                sg.Image(
                    filename="App//img//password-open.png",
                    background_color=self.__color,
                    enable_events=True,
                    visible=False,
                    key="btn-password-open",
                    pad=(0, (0, 5)),
                ),
            ],
            [sg.HSep(pad=(20, (0, 15)))],
        ]
        remember_me_and_forget_password = [
            [
                sg.Checkbox(
                    "Remember me",
                    background_color=self.__color,
                    checkbox_color="white",
                    font="Jaldi 10 bold ",
                    key="chk-remember-me",
                    text_color="#FFA620",
                    pad=(20, (0, 0)),
                ),
                sg.Text("", background_color=self.__color, pad=(30, (0, 0))),
                sg.Text(
                    "Forget Password?",
                    font="Jaldi 10 bold",
                    background_color=self.__color,
                    text_color="#FFA620",
                    enable_events=True,
                    key="forget-password",
                    pad=(15, (0, 0)),
                    justification="r",
                ),
            ]
        ]
        login = [
            sg.Button(
                "Login",
                size=(13, 1),
                border_width=0,
                pad=(0, (50, 15)),
                font="Jaldi 20 bold",
                button_color="#FF9900",
                key="btn-login",
                mouseover_colors="black",
            )
        ]
        social_media = [
            [
                sg.Text(
                    "Or Login with",
                    font="Jaldi 10",
                    background_color=self.__color,
                    text_color="#FFA620",
                    pad=(46, (0, 15)),
                )
            ],
            [
                sg.Image(
                    filename="App//img//facebook 1.png",
                    background_color=self.__color,
                    pad=(20, (0, 0)),
                    key="facebook",
                ),
                sg.Image(
                    filename="App//img//instagram 1.png",
                    background_color=self.__color,
                    pad=(20, (0, 0)),
                    key="instagram",
                ),
                sg.Image(
                    filename="App//img//linkedin.png",
                    background_color=self.__color,
                    pad=(20, (0, 0)),
                    key="linkedin",
                ),
            ],
        ]
        rodape_sign_up = [
            [
                sg.Text(
                    "Dont't have account?",
                    font="Jaldi 10",
                    background_color=self.__color,
                    text_color="#FFA620",
                    pad=(0, (20, 0)),
                ),
                sg.Text(
                    "Sign up",
                    font="Jaldi 10 bold",
                    background_color=self.__color,
                    text_color="#FFA620",
                    enable_events=True,
                    key="sign-up",
                    pad=(0, (20, 0)),
                ),
            ],
        ]

        layout = [
            barra_notificacao,
            logo,
            welcome_back,
            email,
            password,
            remember_me_and_forget_password,
            login,
            social_media,
            rodape_sign_up,
        ]

        window = sg.Window(
            "Solmed",
            layout=layout,
            size=(390, 844),
            element_justification="c",
            icon="App//img//sol.ico",
        )

        return window


if __name__ == "__main__":
    Tela()._front_end()
