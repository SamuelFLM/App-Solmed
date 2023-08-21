from page.Register.main import MainRegister
from data.conexao_banco_de_dados import ConexaoBancoDeDados
from page.Login.main import MainLogin


class Main:
    def __init__(self) -> None:
        self.conexao = ConexaoBancoDeDados()
        self.tela_register = MainRegister(self.conexao)
        self.direct_register = self.tela_register
        self.tela_login = MainLogin(self.conexao, self.direct_register)

    def main(self):
        self.tela_login._main()


if __name__ == "__main__":
    Main().main()
