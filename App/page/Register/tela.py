from ifront import IFrontRegister
import PySimpleGUI as sg


class Tela(IFrontRegister):
    __slots__ = ["__color"]

    def __init__(self) -> None:
        self.__color = "white"
        sg.theme_background_color(self.__color)

    def _front_end(self):
        bar_notification = [
            sg.Image(filename="App//img//barra de notificacao.png", pad=(0, (0, 50)))
        ]

        back_and_help = [
            sg.Image(
                filename="App//img//back.png",
                pad=(0, (0, 0)),
                background_color=self.__color,
                enable_events=True,
                key="btn_back",
            ),
            sg.Text("", pad=(135, (0, 0)), background_color=self.__color),
            sg.Image(
                filename="App//img//help.png",
                pad=(0, (0, 0)),
                background_color=self.__color,
                enable_events=True,
                key="btn_help",
            ),
        ]

        create_account = [
            [
                sg.Text(
                    "Create Account",
                    font="Jaldi 22 bold",
                    background_color=self.__color,
                    text_color="#FFA620",
                    pad=(0, (50, 0)),
                )
            ],
            [
                sg.Text(
                    "create a new account",
                    font="Jaldi 10 bold",
                    background_color=self.__color,
                    text_color="#535353",
                    pad=(0, (0, 30)),
                )
            ],
        ]

        name = [
             [
                [
                    sg.Text(
                        "Name",
                        font="Jaldi 10 bold",
                        background_color=self.__color,
                        text_color="#FFA620",
                        pad=(0, (0, 10)),
                    ),
                    sg.Text("", background_color=self.__color, pad=(140, (0, 10))),
                ],
                [
                    sg.Image(
                        filename="App//img//name.png",
                        background_color=self.__color,
                        pad=(20, (0, 5)),
                    ),
                    sg.Input(
                        "",
                        size=(25, 10),
                        background_color=self.__color,
                        font="Jaldi 12",
                        pad=(0, (0, 5)),
                        border_width=0,
                        text_color="#535353",
                        key="input_name",
                    ),
                        
                    sg.Image(
                        filename="App//img//invisivel.png",
                        background_color=self.__color,
                        pad=(30, (0, 5)),
                    ),
                ],
                [sg.HSep(pad=(20, (0, 20)))],
            ],
        ]
        email = [
            [
                [
                    sg.Text(
                        "Email",
                        font="Jaldi 10 bold",
                        background_color=self.__color,
                        text_color="#FFA620",
                        pad=(20, (0, 10)),
                    ),
                    sg.Text("", background_color=self.__color, pad=(142, (0, 10))),
                ],
                [
                    sg.Image(
                        filename="App//img//email.png",
                        background_color=self.__color,
                        pad=(20, (0, 5)),
                    ),
                    sg.Input(
                        "",
                        size=(25, 10),
                        background_color=self.__color,
                        font="Jaldi 13",
                        pad=(0, (0, 5)),
                        border_width=0,
                        text_color="#535353",
                        key="input_email",
                    ),
                        
                    sg.Image(
                        filename="App//img//invisivel.png",
                        background_color=self.__color,
                        pad=(30, (0, 5)),
                    ),
                ],
                [sg.HSep(pad=(20, (0, 20)))],
            ],
        ]
        phone = [
            [
                [
                    sg.Text(
                        "Phone",
                        font="Jaldi 10 bold",
                        background_color=self.__color,
                        text_color="#FFA620",
                        pad=(0, (0, 10)),
                    ),
                    sg.Text("", background_color=self.__color, pad=(140, (0, 10))),
                ],
                [
                    sg.Image(
                        filename="App//img//phone.png",
                        background_color=self.__color,
                        pad=(20, (0, 5)),
                    ),
                    sg.Input(
                        "",
                        size=(25, 10),
                        background_color=self.__color,
                        font="Jaldi 12",
                        pad=(0, (0, 5)),
                        border_width=0,
                        text_color="#535353",
                        key="input_phone",
                    ),
                        
                    sg.Image(
                        filename="App//img//invisivel.png",
                        background_color=self.__color,
                        pad=(30, (0, 5)),
                    ),
                ],
                [sg.HSep(pad=(20, (0, 20)))],
            ],
        ]
        password = [
            [
                sg.Text(
                    "Password",
                    font="Jaldi 10 bold",
                    background_color=self.__color,
                    text_color="#FFA620",
                    pad=(0, (0, 10)),
                ),
                sg.Text("", background_color=self.__color, pad=(125, (0, 10))),
            ],
            [
                sg.Image(
                    filename="App//img//password.png",
                    background_color=self.__color,
                    pad=(20, (0, 5)),
                ),
                sg.Input(
                    f"",
                    size=(25, 10),
                    password_char="*",
                    background_color=self.__color,
                    font="Jaldi 12",
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
                    pad=(30, (0, 5)),
                ),
            ],
            [sg.HSep(pad=(20, (0, 15)))],
        ]
        confirm_password = [
            [
                sg.Text(
                    "Confirm Password",
                    font="Jaldi 10 bold",
                    background_color=self.__color,
                    text_color="#FFA620",
                    pad=(0, (0, 10)),
                ),
                sg.Text("", background_color=self.__color, pad=(100, (0, 10))),
            ],
            [
                sg.Image(
                    filename="App//img//password.png",
                    background_color=self.__color,
                    pad=(20, (0, 5)),
                ),
                sg.Input(
                    f"",
                    size=(25, 10),
                    password_char="*",
                    background_color=self.__color,
                    font="Jaldi 12",
                    pad=(0, (0, 5)),
                    border_width=0,
                    text_color="#535353",
                    key="password-confirm",
                ),
                sg.Image(
                    filename="App//img//password-closed.png",
                    background_color=self.__color,
                    enable_events=True,
                    key="btn-password-closed-confirm",
                    pad=(30, (0, 5)),
                ),
                sg.Image(
                    filename="App//img//password-open.png",
                    background_color=self.__color,
                    enable_events=True,
                    visible=False,
                    key="btn-password-open-confirm",
                    pad=(30, (0, 5)),
                ),
            ],
            [sg.HSep(pad=(20, (0, 15)))],
        ]
        btn_create_account = [
            sg.Button(
                "Create Account",
                size=(15, 1),
                border_width=0,
                pad=(0, (30, 15)),
                font="Jaldi 20 bold",
                button_color="#FF9900",
                key="btn-create-account",
                mouseover_colors="black",
            )
        ]
        already_have_a_account_login = [
            [
                sg.Text(
                    "Already have a account?",
                    font="Jaldi 10",
                    background_color=self.__color,
                    text_color="#FFA620",
                    pad=(0, (20, 0)),
                ),
                sg.Text(
                    "Login",
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
            bar_notification,
            back_and_help,
            create_account,
            name,
            email,
            phone,
            password,
            confirm_password,
            btn_create_account,
            already_have_a_account_login,
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
