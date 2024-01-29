import inicioSesion


class Main:

    def __init__(self) -> None:
        Main.run()

    @staticmethod
    def run() -> None:
        inicioSesion.InicioSesion.start()


if __name__ == '__main__':
    Main()
