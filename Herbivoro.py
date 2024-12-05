from Animal import Animal

class Herbivoro(Animal):  # Herbivoro herda de Animal
    def __init__(self, tipo_planta="capim"):
        super().__init__()  # Chama o construtor da classe pai
        self.tipo_planta = tipo_planta  # Adiciona atributo exclusivo
        self.img = 'img/humano.webp'

herbiro = Herbivoro(tipo_planta='Jasmine')

herbiro.alimentar()