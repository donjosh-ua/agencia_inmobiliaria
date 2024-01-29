from client.controller import InicioSesion


class Main:

    def __init__(self) -> None:
        self.run()

    @classmethod
    def run(cls) -> None:
        InicioSesion.InicioSesion.start()


if __name__ == '__main__':
    Main()
