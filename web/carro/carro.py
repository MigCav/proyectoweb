class Carro:
    def __init__(self) -> None:
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')
        