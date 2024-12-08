
class Animal:
    def __init__(self, idade=1, energia=100):
        self.idade = idade
        self.energia = energia


    def consumirEnergia(self):
        self.energia -= 1  
        if self.energia == 0:
            print('Energia acabou')

    def aniversario(self):
        self.idade += 1 
        if self.idade >= 100:
            print('morreu')
